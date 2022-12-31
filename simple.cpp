#include <stdio.h>
#include <opencv2/opencv.hpp>

using namespace cv;
int main(int argc, char** argv )
{
    auto start = std::chrono::high_resolution_clock::now();
    Mat image;
    std::string image_path = "/home/pauls/opencv_projects/example/lenna.png";
    std::cout << "Diplaying " << image_path << std::endl;
    image = imread(image_path);
    if ( !image.data )
    {
        printf("No image data \n");
        return -1;
    }
    namedWindow("Display Image", WINDOW_AUTOSIZE );
    imshow("Display Image", image);
    auto stop = std::chrono::high_resolution_clock::now();
    waitKey(0);

    auto duration = std::chrono::duration_cast<std::chrono::microseconds>(stop-start);
    std::cout << "Finished execution in " << duration.count() << " ms" << std::endl;

    return 0;
}

