from .blur_methods import blur_image_numpy
import cv2


def blur_image(input_filename, output_filename=None):
    '''Blur an image specified by a file.
    Args:
        input_filename (string): Name of the file containing the image
                                 to be blurred.
        output_filename (string) [optional]: Name of the file to write
                                             the blurred image in.
    Returns:
        bimage (np.array): The blurred image as a 3D tensor.
    '''

    image = cv2.imread(input_filename)
    assert image is not None, f'Failed to read image at \'{input_filename}\'.'
    image = blur_image_numpy(image)

    if output_filename is not None:
        cv2.imwrite(output_filename, image)

    return image


def blur_subsection(input_filename, subsections, output_filename=None):
    '''Blur the an image in the given subsections.
    Args:
        input_filename (string): Name of the file containing the image
                                 to be blurred.
        subsections (list): A list of list-type objects of lenght 4 indicating
                            the starting row and columna of the upper right
                            corner of the bounding box as well as the height
                            and width of the box.
        output_filename (string) [optional]: Name of the file to write the
                                             blurred image in.
    Returns:
        bimage (np.array): The blurred image as a 3D tensor.
    '''

    image = cv2.imread(input_filename)
    assert image is not None, f'Failed to read image at \'{input_filename}\'.'
    for [row, column, height, width] in subsections:
        image[row:row + height, column:column + width, ] = \
                blur_image_numpy(
                        image[row:row + height, column:column + width, ])

    if output_filename is not None:
        cv2.imwrite(output_filename, image)

    return image
