'''A module that blurs images using a 3x3 averaging kernel.

Can be run from the command line to blur a specified image.
Uses numpy vectorized operations as its implementation.
'''

import sys
import os
import numpy as np
import cv2


def blur_image_numpy(image):
    '''Blur function using numpy functionality.
    Args:
        image (np.array): The image that will be blurred.
    Returns:
        bimage (np.array): The blurred version of the input image.
    '''

    image_ = np.pad(image, 1, mode='edge')[..., 1:-1]
    image_ = np.array(image_, dtype=np.uint32)
    height, width, channels = image_.shape
    bimage = np.empty([height-2, width-2, channels], dtype=np.uint8)

    #make slices that correspond to each relative neighbor.
    northwest = image_[0:height-2, 0:width-2]
    north = image_[0:height-2, 1:width-1]
    northeast = image_[0:height-2, 2:width]
    west = image_[1:height-1, 0:width-2]
    center = image_[1:height-1, 1:width-1]
    east = image_[1:height-1, 2:width]
    southwest = image_[2:height, 0:width-2]
    south = image_[2:height, 1:width-1]
    southeast = image_[2:height, 2:width]

    #if you sum each slice elementwise, you get all neighbors for
    #each sum iteration.
    bimage = (northwest + north + northeast + \
            west + center + east + southwest + south + southeast) / 9
    bimage = bimage.astype(np.uint8)

    return bimage

if __name__ == '__main__':
    if len(sys.argv) == 2:
        inputfile = sys.argv[1]
        if os.path.isfile(inputfile):
            image = cv2.imread(inputfile)
            image_ = blur_image_numpy(image)
            cv2.imwrite('blurred_image.jpg', image_)
        else:
            print(f'File {inputfile} does not exist.')
    else:
        print('Usage: blur_1.py inputfile')
