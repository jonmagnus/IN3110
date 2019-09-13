import cv2
import argparse
import os

from blur_1 import blur_image_python
from blur_2 import blur_image_numpy
from blur_3 import blur_image_numba


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Blur an image using the '
                                     + 'mean value of a 3*3 kernel')
    parser.add_argument('image', type=str, help='an image to blur')
    parser.add_argument('-o', '--outfile', type=str, metavar='FILENAME')
    parser.add_argument('-m', '--method', type=str,
                        help='the method used to produce the blurred image. '
                        + 'Default is set to \'numpy\'.')
    args = parser.parse_args()

    image = args.image
    if not os.path.exists(image):
        raise ValueError(f'Image file not found: '
                         + 'Could\'t find file \'{image}\'.')

    image = cv2.imread(image)
    if image is None:
        raise ValueError('Failed to read image.')

    method = args.method
    if method is None:
        method = 'numpy'

    methods = {
            'python': blur_image_python,
            'numpy': blur_image_numpy,
            'numba': blur_image_numba
            }

    if method not in methods:
        raise ValueError(f'Method \'{method}\' not found.')

    method = methods[method]
    image = method(image)
    print(image.shape)
    filename = args.outfile
    if filename is None:
        filename = 'a.jpg'
    cv2.imwrite(filename, image)
