import cv2
import numpy as np
import matplotlib.pyplot as plt

def bit_plane_slicing(image_path):
    # Görüntüyü oku
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Görüntünün boyutlarını al
    rows, cols = image.shape

    # Bit plane'leri saklamak için boş bir dizi oluştur
    bit_planes = np.zeros((8, rows, cols), dtype=np.uint8)

    # Her bir bit plane'i elde et
    for i in range(8):
        bit_planes[i] = (image & (1 << i)) * 255

    # Bit plane'leri görselleştir
    plt.figure(figsize=(12, 8))
    plt.gray()

    for i in range(8):
        plt.subplot(2, 4, i + 1)
        plt.imshow(bit_planes[i], cmap='gray')
        plt.title(f'Bit Plane {i + 1}')

    plt.show()

# Örnek olarak bir görüntü yolu verelim
image_path = "bit-plane-slicing.png"
bit_plane_slicing(image_path)
