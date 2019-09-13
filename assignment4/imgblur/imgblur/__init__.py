from .blur_methods import blur_image_numpy

def blur_image(input_filename, output_filename=None):
    '''Blur an image specified by a file.
    Args:
        input_filename (string): Name of the file containing the image to be blurred.
        output_filename (string) [optional]: Name of the file to write the blurred image in.
    Returns:
        bimage (np.array): The blurred image as a 3D tensor.
    '''
    
    image = cv2.imread(input_filename)
    assert image is not None, f'Failed to read image at \'{input_filename}\'.'
    image = blur_image_numpy(image)
    
    if output_filename is not None:
        cv2.imwrite(output_filename, image)
    
    return image
