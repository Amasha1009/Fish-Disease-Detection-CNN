import cv2
import os

IMAGE_SIZE = (224, 224)

def resize_image(image_path):
    image = cv2.imread(image_path)
    if image is None:
        return None
    return cv2.resize(image, IMAGE_SIZE)


print("Image resize preprocessing script")