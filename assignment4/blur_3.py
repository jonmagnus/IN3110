'''A module that blurs images using a 3x3 averaging kernel.

Can be run from the command line to blur a specified image.
Uses numba C-loops as its implementation.
'''

import sys
import os
import numpy as np
import cv2
import numba as nb


@nb.njit
def convolve_padded_image(image, bimage):
    '''Numba accelerated nested for-loops for applying the blurr-convolution.
    Args:
        image (np.aarray): The padded version of the image to be blurred.
        bimage (np.array): The array that should be overwritten by the
                           blurred image.
    Returns:
        bimage (np.array): The array that should be overwritten by the
                           blurred image.
    '''
    height, width, channels = bimage.shape
    height_offsets = [1, 1, 1, 0, 0, 0, -1, -1, -1]
    width_offsets = [1, 0, -1, 1, 0, -1, 1, 0, -1]

    for h in range(height):
        for w in range(width):
            for c in range(channels):
                intensity = 0.
                for i in range(9):
                    intensity += image[h + height_offsets[i] + 1, \
                    w + width_offsets[i] + 1, c]
                bimage[h, w, c] = intensity/9.

    return bimage


def blur_image_numba(image):
    '''Python blur function using pure python.
    Args:
        image (np.array): The image that will be blurred.
    Returns:
        bimage (np.array): The blurred version of the input image.
    '''

    image_ = np.pad(image, 1, mode='edge')[..., 1:-1]
    height, width, channels = image_.shape
    height -= 2
    width -= 2
    bimage = np.empty([height, width, channels], dtype=np.uint8)
    bimage = convolve_padded_image(image_, bimage)

    return bimage

if __name__ == '__main__':
    if len(sys.argv) == 2:
        inputfile = sys.argv[1]
        if os.path.isfile(inputfile):
            image = cv2.imread(inputfile)
            image_ = blur_image_numba(image)
            cv2.imwrite('blurred_image.jpg', image_)
        else:
            print(f'File {inputfile} does not exist.')
    else:
        print('Usage: blur_1.py inputfile')
