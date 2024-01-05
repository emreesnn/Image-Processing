import cv2
import numpy as np
import matplotlib.pyplot as plt

def laplace_blur(image_path, kernel_size=3):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    laplace_kernel = np.array([[0, 1, 0],
                               [1, -4, 1],
                               [0, 1, 0]])

    blurred_image = cv2.filter2D(image, -1, laplace_kernel)

    plt.figure(figsize=(12, 6))

    plt.subplot(1, 2, 1)
    plt.imshow(image, cmap='gray')
    plt.title('Orjinal Görüntü')

    plt.subplot(1, 2, 2)
    plt.imshow(blurred_image, cmap='gray')
    plt.title(f'Laplace ile Blurlaştırma (Kernel Boyutu = {kernel_size})')

    plt.show()

image_path = "blurring-image.png"
laplace_blur(image_path, kernel_size=3)