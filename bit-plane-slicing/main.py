import cv2
import numpy as np
import matplotlib.pyplot as plt

def bit_plane_slicing(image_path):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    rows, cols = image.shape

    bit_planes = np.zeros((8, rows, cols), dtype=np.uint8)

    for i in range(8):
        bit_planes[i] = (image & (1 << i)) * 255

    plt.figure(figsize=(12, 8))
    plt.gray()

    for i in range(8):
        plt.subplot(2, 4, i + 1)
        plt.imshow(bit_planes[i], cmap='gray')
        plt.title(f'Bit Plane {i + 1}')

    plt.show()

image_path = "bit-plane-slicing.png"
bit_plane_slicing(image_path)
