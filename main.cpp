#include <stdio.h>
#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <iostream>

using namespace cv;
int main(int argc, char** argv)
{
    auto start = std::chrono::high_resolution_clock::now();
    std::string filename = "/home/pauls/opencv_projects/example/sample.mp4";
    VideoCapture capture(filename);
    Mat frame;

    if( !capture.isOpened() )
        throw "Error when reading " + filename;

    namedWindow( "w", 1);
    for( ; ; )
    {
        capture >> frame;
        if(frame.empty())
            break;
    //    imshow("w", frame);
    //    waitKey(20); // waits to display frame
    }
    auto stop = std::chrono::high_resolution_clock::now();
    //waitKey(0); // key press to close window
    // releases and window destroy are automatic in C++ interface

    auto duration = std::chrono::duration_cast<std::chrono::microseconds>(stop-start);
    std::cout << "Finished execution in [" << duration.count() << "] μs" << std::endl;

    return 0;
}

