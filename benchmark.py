import sys
import pathlib
import subprocess
import csv
from datetime import datetime

opencv_root_dir = '/home/pauls/opencv/4.7.0/'

def generate_filename():
    return 'benchmark-results/benchmark-results_' + datetime.now().strftime('%m-%d-%Y_%H:%M:%S') + '.csv'

def output_result_to_csv(results):
    header = ['Build', 'Execution time (μs)']

    csv_file = generate_filename()
    with open(csv_file, 'w+') as f:
        writer = csv.DictWriter(f, fieldnames=header)
        writer.writeheader()
        writer.writerows(results)
    print(f'Saved benchmark results in {csv_file}')

def get_execution_micros(out):
    res = out.split('\n')[-2]
    avg_exec_time = res.split('[')[1].split('μs')[0].strip()
    return int(avg_exec_time)

def benchmark(build, num_of_executions):
    benchmark_results = []
    for i in range(num_of_executions):
        out = subprocess.run(['./benchmark.sh', '1'], check=True, capture_output=True)
        execution_micros = get_execution_micros(out.stdout.decode('utf-8'))
        benchmark_results.append({'Build': build, 'Execution time (μs)': execution_micros})
        print(f'Build {build} took {execution_micros} μs for execution #{i}')
    print("")
    return benchmark_results

def update_cmake(build):
    cmake_config = 'CMakeLists.txt'
    lines = curr_build = None
    new_build = opencv_root_dir + build
    with open(cmake_config, 'r') as f:
        lines = f.readlines()
        for line in lines:
            if 'REQUIRED PATHS' in line:
                curr_build = line.strip().split('REQUIRED PATHS ')[1].replace(')', '')
                print(f'\nCurrent build: {curr_build}\nReplacing with: {new_build}\n')

    with open(cmake_config, 'w') as f:
        for line in lines:
            line = line.replace(curr_build, new_build)
            f.write(line)

def get_opencv_builds():
    opencv_dir = pathlib.Path(opencv_root_dir)
    opencv_builds = [str(item).split('/')[-1] for item in opencv_dir.iterdir() if str(item) != opencv_root_dir + 'opencv-4.7.0']
    print(f'Found {len(opencv_builds)} builds: {opencv_builds}\n')
    
    return opencv_builds

"""

 For every openCV build, install it, update the CMakeLists.txt file,
 recompile the example, run the benchmark, and save the results to a csv file.

"""
def main():
    opencv_builds = get_opencv_builds()
    num_of_executions = 15 if len(sys.argv) == 1 else int(sys.argv[1])
    benchmark_results = []

    for build in opencv_builds:
        subprocess.run(['./install-build.sh', opencv_root_dir + build], check=True)
        update_cmake(build)
        benchmark_results = benchmark_results + benchmark(build, num_of_executions)

    output_result_to_csv(benchmark_results)


if __name__ == '__main__':
    main()

