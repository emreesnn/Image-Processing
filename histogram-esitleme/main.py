import cv2
import numpy as np
import matplotlib.pyplot as plt

def histogram_equalization(image_path):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    equalized_image = cv2.equalizeHist(image)

    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.imshow(image, cmap='gray')
    plt.title('Orjinal Görüntü')

    plt.subplot(1, 2, 2)
    plt.imshow(equalized_image, cmap='gray')
    plt.title('Histogram Eşitleme Sonrası')

    plt.show()

image_path = "histogram-image.png"
histogram_equalization(image_path)
