import cv2
import numpy as np

IMAGE_SIZE = (224, 224)

def normalize_image(image_path):
    """
    Read an image, resize it, and normalize pixel values.
    """

    image = cv2.imread(image_path)

    if image is None:
        raise ValueError("Unable to load image.")

    image = cv2.resize(image, IMAGE_SIZE)

    image = image.astype(np.float32) / 255.0

    return image


if __name__ == "__main__":
    print("Normalization module ready.")