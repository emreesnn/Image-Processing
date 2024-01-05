import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

def contraharmonic_mean_filter(image, neighborhood_size, Q):
    padded_image = np.pad(image, pad_width=neighborhood_size, mode='reflect')
    result = np.zeros_like(image, dtype=np.float64)

    for i in range(neighborhood_size, padded_image.shape[0] - neighborhood_size):
        for j in range(neighborhood_size, padded_image.shape[1] - neighborhood_size):
            neighborhood = padded_image[i - neighborhood_size:i + neighborhood_size + 1, j - neighborhood_size:j + neighborhood_size + 1]
            numerator = np.sum(np.power(neighborhood, Q + 1))
            denominator = np.sum(np.power(neighborhood, Q))
            result[i - neighborhood_size, j - neighborhood_size] = numerator / denominator if denominator != 0 else 0

    return result.astype(np.uint8)

image_path = "img.png"
original_image = np.array(Image.open(image_path).convert('L'))

neighborhood_size = 3
Q = 1.5

filtered_image = contraharmonic_mean_filter(original_image, neighborhood_size, Q)

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(original_image, cmap='gray')
plt.title('Original Image')

plt.subplot(1, 2, 2)
plt.imshow(filtered_image, cmap='gray')
plt.title('Contraharmonic Mean Filtered Image')

plt.show()