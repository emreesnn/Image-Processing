import cv2
import numpy as np
import matplotlib.pyplot as plt

def add_salt_and_pepper_noise(image, salt_prob, pepper_prob):
    noisy_image = np.copy(image)

    salt_pixels = np.random.rand(*image.shape) < salt_prob
    noisy_image[salt_pixels] = 1

    pepper_pixels = np.random.rand(*image.shape) < pepper_prob
    noisy_image[pepper_pixels] = 0

    return noisy_image

original_image = cv2.imread('img.png', cv2.IMREAD_GRAYSCALE)

original_image = original_image / 255.0

salt_probability = 0.01
pepper_probability = 0.01

noisy_image = add_salt_and_pepper_noise(original_image, salt_probability, pepper_probability)

plt.subplot(1, 2, 1)
plt.imshow(original_image, cmap='gray')
plt.title('Original Image')

plt.subplot(1, 2, 2)
plt.imshow(noisy_image, cmap='gray')
plt.title('Noisy Image')

plt.show()