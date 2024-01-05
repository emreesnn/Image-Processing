import cv2
import numpy as np
import matplotlib.pyplot as plt

def gaussian_blur(image_path, kernel_size=3):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    blurred_image = cv2.GaussianBlur(image, (kernel_size, kernel_size), 0)

    plt.figure(figsize=(12, 6))

    plt.subplot(1, 2, 1)
    plt.imshow(image, cmap='gray')
    plt.title('Orjinal Görüntü')

    plt.subplot(1, 2, 2)
    plt.imshow(blurred_image, cmap='gray')
    plt.title(f'Gaussian Blurlaştırma (Kernel Boyutu = {kernel_size})')

    plt.show()

image_path = "image1.png"
gaussian_blur(image_path, kernel_size=9)