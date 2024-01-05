import cv2
import numpy as np
import matplotlib.pyplot as plt

def average_filter(image_path, kernel_size=3):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    kernel = np.ones((kernel_size, kernel_size), np.float32) / (kernel_size**2)

    filtered_image = cv2.filter2D(image, -1, kernel)

    plt.figure(figsize=(12, 6))

    plt.subplot(1, 2, 1)
    plt.imshow(image, cmap='gray')
    plt.title('Orjinal Görüntü')

    plt.subplot(1, 2, 2)
    plt.imshow(filtered_image, cmap='gray')
    plt.title(f'Ortalama Filtre (Kernel Boyutu = {kernel_size})')

    plt.show()

image_path = "mean-filter-image.png"
average_filter(image_path, kernel_size=9)