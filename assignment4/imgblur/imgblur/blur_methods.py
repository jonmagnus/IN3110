'''
A copy of blur_1.py at the root of the assignment directory.
'''
import numpy as np


def blur_image_numpy(image):
    '''Blur function using a numpy functionality.
    Args:
        image (np.array): The image that will be blurred.
    Returns:
        bimage (np.array): The blurred version of the input image.
    '''

    image_ = np.pad(image, 1, mode='edge')[..., 1:-1]
    height, width, channels = image_.shape
    height -= 2
    width -= 2
    assert np.all(np.array([height, width, channels]) > 0), \
        'Negative dimensions of image array: {}'.format(
                [height, width, channels])
    bimage = np.zeros([height, width, channels], dtype=np.float32)

    dh = [1, 1, 1, 0, 0, 0, -1, -1, -1]
    dw = [1, 0, -1, 1, 0, -1, 1, 0, -1]

    for i in range(9):
        bimage += image_[1 + dh[i]:1 + height + dh[i],
                         1 + dw[i]:1 + width + dw[i], :]
    bimage /= 9.
    bimage = bimage.astype(np.uint8)

    return bimage
