import imgblur
import numpy as np


def test_blur_image_reduced_max():
    '''Test if blurring decreases the maximum intensity.'''
    np.random.seed(1)
    image = np.random.randint(0, 255, size=[480, 640, 3], dtype=np.uint8)
    bimage = imgblur.blur_methods.blur_image_numpy(image[...])
    assert image.max() > bimage.max(), 'Maximum intensity did not decrease.'


def test_blur_is_average():
    '''Test if the value of each inner pixel is the average
    the values in the surrounding pixels.
    '''
    np.random.seed(1)
    imgsize = [480, 640, 3]
    image = np.random.randint(0, 255, size=imgsize, dtype=np.uint8)
    bimage = imgblur.blur_methods.blur_image_numpy(image[...])
    dh = [1, 1, 1, 0, 0, 0, -1, -1, -1]
    dw = [1, 0, -1]*3
    for height in range(1, imgsize[0] - 1):
        for width in range(1, imgsize[1] - 1):
            for channels in range(1, imgsize[-1] - 1):
                s = 0,
                for i in range(9):
                    s += image[height + dh[i], width + dw[i], channels]
                assert bimage[height, width, channels] == s // 9, \
                    'Internal pixels were not blurred correctly.'
