#!/bin/bash

# Number of executions
if [ -z "$1" ]; then
	SAMPLE_SIZE=15
else
	SAMPLE_SIZE=$1
fi

# Loop counter
COUNTER=0

# Aggragated time
TOTAL_TIME=0

# Compile example
rm -rf build/*
cmake -S . -B build/
cd build
cmake --build .
cd ..

# Benchmark
while [ $COUNTER -lt $SAMPLE_SIZE ]; do
	# Execution time
	TIME=$(./build/opencvtest | cut -d [ -f 2 | cut -d ] -f 1)
	echo "Execution #${COUNTER}: ${TIME} μs"

	TOTAL_TIME=$((TOTAL_TIME+TIME))
	let COUNTER=COUNTER+1
done

# Average execution time
AVG_TIME=$((TOTAL_TIME/SAMPLE_SIZE))

# Convert to seconds
AVG_TIME_SECONDS=$(bc -l <<< 'scale=4; '$AVG_TIME'/1000000')

echo "Average execution time was [${AVG_TIME} μs, ${AVG_TIME_SECONDS} s] for ${SAMPLE_SIZE} executions"

