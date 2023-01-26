cmake_minimum_required(VERSION 3.0.0)
project(opencvtest VERSION 0.1.0)

include(CTest)
enable_testing()

find_package( OpenCV REQUIRED PATHS /home/pauls/opencv/4.7.0/opencv-4.7.0-build-amdblas-amdfftw-ipp-tbb-eigen-openmp-gcc)
include_directories( ${OpenCV_INCLUDE_DIRS} )

add_executable(opencvtest main.cpp)

target_link_libraries( opencvtest ${OpenCV_LIBS} )

set(CPACK_PROJECT_NAME ${PROJECT_NAME})
set(CPACK_PROJECT_VERSION ${PROJECT_VERSION})
include(CPack)

