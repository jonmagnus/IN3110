import numpy as np
cimport numpy as np
import cv2


def blur_image_python(np.ndarray image):
    '''Python blur function using pure python.
    Args:
        image (np.array): The image that will be blurred.
    Returns:
        bimage (np.array): The blurred version of the input image.
    '''

    image_ = np.pad(image, 1, mode='edge')[..., 1:-1]
    cdef int height, width, channels
    height, width, channels = image_.shape
    height -= 2
    width -= 2
    bimage = np.empty([height, width, channels], dtype=np.uint8)

    cdef list dh, dw
    dh = [1, 1, 1, 0, 0, 0, -1, -1, -1]
    dw = [1, 0, -1, 1, 0, -1, 1, 0, -1]

    cdef int h, w, c
    cdef float intensity
    for h in range(height):
        for w in range(width):
            for c in range(channels):
                intensity = 0.
                for i in range(9):
                    intensity += image_[h + dh[i] + 1, w + dw[i] + 1, c]
                bimage[h, w, c] = intensity/9.

    return bimage

image = cv2.imread('beatles.jpg')
image_ = blur_image_python(image)
cv2.imwrite('blurred_image.jpg', image_)
