#include <iostream>
#include <fstream>
#include <string>
#include <chrono>
#define STB_IMAGE_IMPLEMENTATION
#include "stb_image.h"

using namespace std;
using namespace std::chrono;

unsigned char* loadImageRGBA(const string& filename, int& width, int& height, int& channels) {
    unsigned char* data = stbi_load(filename.c_str(), &width, &height, &channels, 4);
    if (!data) {
        cerr << "Failed to load image: " << filename << endl;
        exit(1);
    }
    cout << "Image loaded: " << filename << " (" << width << "x" << height << "), RGBA channels.\n";
    return data;
}
// mana ini yang di run
void saveToCSV(const unsigned char* data, int width, int height, const string& outputFile) {
    ofstream file(outputFile);
    if (!file.is_open()) {
        cerr << "Could not create output file: " << outputFile << endl;
        return;
    }
    file << "x,y,R,G,B,A\n";
    const unsigned char* ptr = data;
    for (int y = 0; y < height; ++y) {
        for (int x = 0; x < width; ++x) {
            int r = *(ptr++), g = *(ptr++), b = *(ptr++), a = *(ptr++);
            file << x << "," << y << "," << r << "," << g << "," << b << "," << a << "\n";
        }
    }
    file.close();
    cout << "RGBA data saved to: " << outputFile << endl;
}

// ...existing code...
int main() {
    auto start = high_resolution_clock::now();

    // Use local path relative to the executable
    string imagePath = "input.png";     // Place input.png in same folder as .cpp file
    string outputCSV = "output.csv";    // Output will be created in same folder
    int width = 0, height = 0, channels = 0;
// ...existing code...

    unsigned char* imgData = loadImageRGBA(imagePath, width, height, channels);
    saveToCSV(imgData, width, height, outputCSV);
    stbi_image_free(imgData);

    auto end = high_resolution_clock::now();
    auto duration_ms = duration_cast<milliseconds>(end - start).count();

    cout << "Processing time: " << duration_ms / 1000.0 << " seconds.\n";
    return 0;
}
