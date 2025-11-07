// Minimal stub of stb_image API so the project compiles when the real stb_image.h is not present.
// This stub does NOT implement image loading. It returns nullptr from stbi_load so
// your program will exit with the existing error handling. Replace this file with
// the real stb_image.h (https://github.com/nothings/stb) to enable actual image loading.

#ifndef STB_IMAGE_STUB_H
#define STB_IMAGE_STUB_H

#include <cstddef>

#ifdef __cplusplus
extern "C" {
#endif

// Minimal API
unsigned char* stbi_load(const char* filename, int* x, int* y, int* channels_in_file, int desired_channels) {
    (void)filename; (void)x; (void)y; (void)channels_in_file; (void)desired_channels;
    return nullptr; // indicate failure; caller should handle
}

void stbi_image_free(void* retval_from_stbi_load) {
    (void)retval_from_stbi_load;
}

#ifdef __cplusplus
}
#endif

#endif // STB_IMAGE_STUB_H
