import cv2
import numpy as np
import matplotlib.pyplot as plt

def gaussian_filter(image_path, kernel_size=3, sigma=1.0):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    kernel = cv2.getGaussianKernel(kernel_size, sigma)
    kernel_2d = np.outer(kernel, kernel.transpose())

    filtered_image = cv2.filter2D(image, -1, kernel_2d)

    plt.figure(figsize=(12, 6))

    plt.subplot(1, 2, 1)
    plt.imshow(image, cmap='gray')
    plt.title('Orjinal Görüntü')

    plt.subplot(1, 2, 2)
    plt.imshow(filtered_image, cmap='gray')
    plt.title(f'Gaussian Filtre (Kernel Boyutu = {kernel_size}, Sigma = {sigma})')

    plt.show()

image_path = "gaussian-filter.png"
gaussian_filter(image_path, kernel_size=15, sigma=5.0)