import numpy as np
import cv2


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
    bimage = np.zeros([height, width, channels], dtype=np.float32)

    dh = [1, 1, 1, 0, 0, 0, -1, -1, -1]
    dw = [1, 0, -1, 1, 0, -1, 1, 0, -1]

    for i in range(9):
        bimage += image_[1 + dh[i]:1 + height + dh[i],
                         1 + dw[i]:1 + width + dw[i], :]
    bimage /= 9.
    bimage = bimage.astype(np.uint8)

    return bimage


if __name__ == '__main__':
    image = cv2.imread('beatles.jpg')
    image_ = blur_image_numpy(image)
    cv2.imwrite('blurred_image.jpg', image_)
