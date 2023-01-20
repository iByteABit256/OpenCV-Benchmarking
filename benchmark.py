import pathlib

opencv_root_dir = '/home/pauls/opencv/4.7.0/'

def get_opencv_builds():
    opencv_dir = pathlib.Path(opencv_root_dir)
    opencv_builds = [str(item).split('/')[-1] for item in opencv_dir.iterdir() if str(item) != opencv_root_dir + 'opencv-4.7.0']
    print(f'Found {len(opencv_builds)} builds: {opencv_builds}')
    
    return opencv_builds

def update_cmake(build):
    cmake_config = 'CMakeLists.txt'
    lines = curr_build = None
    new_build = opencv_root_dir + build
    with open(cmake_config, 'r') as f:
        lines = f.readlines()
        for line in lines:
            if 'OpenCV_DIR' in line:
                curr_build = line.strip().split('OpenCV_DIR ')[1].replace(')', '')
                print(f'Current build: {curr_build}\nReplacing with {new_build}')

    with open(cmake_config, 'w') as f:
        for line in lines:
            line = line.replace(curr_build, new_build)
            f.write(line)



"""

 For every openCV build, update the CMakeLists.txt file,
 recompile the example, run the benchmark, and save the results to a csv file.

"""
opencv_builds = get_opencv_builds()

for build in opencv_builds:
    update_cmake(build)

