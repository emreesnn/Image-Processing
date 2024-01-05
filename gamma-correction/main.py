import cv2
import numpy as np
import matplotlib.pyplot as plt

def gamma_correction(image_path, gamma=1.0):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    corrected_image = np.power(image / 255.0, gamma) * 255.0
    corrected_image = np.clip(corrected_image, 0, 255).astype(np.uint8)

    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.imshow(image, cmap='gray')
    plt.title('Orjinal Görüntü')

    plt.subplot(1, 2, 2)
    plt.imshow(corrected_image, cmap='gray')
    plt.title(f'Gamma Düzeltme (Gamma={gamma})')

    plt.show()

image_path = "gamma.png"
gamma_correction(image_path, gamma=0.4)
