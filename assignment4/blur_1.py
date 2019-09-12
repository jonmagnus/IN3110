import numpy as np
import cv2

def blur_image_python(image):
    '''Python blur function using pure python.
    Args:
        image (np.array): The image that will be blurred.
    Returns:
        bimage (np.array): The blurred version of the input image.
    '''
    
    image_ = np.pad(image,1,mode='edge')[...,1:-1]
    height, width, channels = image_.shape
    height -= 2; width -= 2
    bimage = np.empty([height,width,channels],dtype=np.uint8)
    
    dh = [1,1,1,0,0,0,-1,-1,-1]
    dw = [1,0,-1,1,0,-1,1,0,-1]
    
    for h in range(height):
        for w in range(width):
            for c in range(channels):
                intensity = 0.
                for i in range(9):
                    intensity += image_[h + dh[i],w + dw[i],c]
                bimage[h,w,c] = intensity/9.

    return bimage

if __name__ == '__main__':
    image = cv2.imread('beatles.jpg')
    #image = cv2.resize(image,(0,0),fx=.5,fy=.5)
    image_ = blur_image_python(image)
    cv2.imwrite('blurred_image.jpg',image_)
