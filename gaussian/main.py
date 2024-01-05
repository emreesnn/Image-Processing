import cv2
import numpy as np
import matplotlib.pyplot as plt

def gaussian_blur(image_path, kernel_size=3):
    # Görüntüyü oku
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Gaussian blurlaştırma işlemi
    blurred_image = cv2.GaussianBlur(image, (kernel_size, kernel_size), 0)

    # Görüntülerin yan yana gösterimi için subplot kullanma
    plt.figure(figsize=(12, 6))

    # Orjinal görüntü
    plt.subplot(1, 2, 1)
    plt.imshow(image, cmap='gray')
    plt.title('Orjinal Görüntü')

    # Gaussian blurlaştırma ile elde edilmiş görüntü
    plt.subplot(1, 2, 2)
    plt.imshow(blurred_image, cmap='gray')
    plt.title(f'Gaussian Blurlaştırma (Kernel Boyutu = {kernel_size})')

    # Görüntüleri göster
    plt.show()

# Örnek olarak bir görüntü yolu verelim
image_path = "image1.png"
gaussian_blur(image_path, kernel_size=9)  # Kernel boyutunu istediğiniz şekilde ayarlayabilirsiniz
