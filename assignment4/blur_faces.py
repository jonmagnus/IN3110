import imgblur
import cv2
import matplotlib.pyplot as plt

if __name__ == '__main__':
    image = cv2.imread('beatles.jpg')
    faceCascade = cv2.CascadeClassifier(
            'haarcascade_frontalface_default.xml')
    faces = faceCascade.detectMultiScale(
            image,
            scaleFactor=1.025,
            minNeighbors=5,
            minSize=(30, 30)
            )
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    plt.subplot(1, 2, 1)
    plt.imshow(image)

    subsections = [[r, c, h, w] for i in range(300) for c, r, w, h in faces]
    image = imgblur.blur_subsection('beatles.jpg', subsections)
    faceCascade = cv2.CascadeClassifier(
            'haarcascade_frontalface_default.xml')
    faces = faceCascade.detectMultiScale(
            image,
            scaleFactor=1.025,
            minNeighbors=5,
            minSize=(30, 30)
            )
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    plt.subplot(1, 2, 2)
    plt.imshow(image)
    plt.show()
