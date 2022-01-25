import cv2
import imutils

HOGCV = cv2.HOGDescriptor()
HOGCV.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())


def detect(img_path):
    image = cv2.imread(img_path)
    image = imutils.resize(image, width=min(550, image.shape[1]))

    box_cordinates, weights = HOGCV.detectMultiScale(image,
                                                     winStride=(8, 8),
                                                     padding=(32, 32),
                                                     scale=1.08)

    person = 1
    for x, y, w, h in box_cordinates:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(image, f'osoba {person}', (x, y),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
        person += 1

    cv2.putText(image, f'Suma osob: {person - 1}', (40, 20),
                cv2.FONT_HERSHEY_DUPLEX, 0.8, (0, 255, 255), 2)
    cv2.imshow('Wynik', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return  image
