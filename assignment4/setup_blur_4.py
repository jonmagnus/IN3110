from distutils.core import setup
from Cython.Build import cythonize

setup(
        ext_modules = cythonize('blur_4.pyx')
)

if __name__ == '__main__':
    exit()
    import cv2
    from blur_4 import blur_image_python
    image = cv2.imread('beatles.jpg')
    image_ = blur_image_python(image)
    cv2.imwrite('blurred_image.jpg', image_)
