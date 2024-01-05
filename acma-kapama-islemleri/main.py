import cv2
import numpy as np
import matplotlib.pyplot as plt

def image_opening_closing(input_image_path):
    # Read the input image
    img = cv2.imread(input_image_path, cv2.IMREAD_GRAYSCALE)

    # Define a kernel for morphological operations
    kernel = np.ones((10, 10), np.uint8)

    # Perform image opening
    opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

    # Perform image closing
    closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

    # Display the images using plt.subplot
    plt.figure(figsize=(10, 5))

    plt.subplot(1, 3, 1)
    plt.title('Original Image')
    plt.imshow(img, cmap='gray')
    plt.axis('off')

    plt.subplot(1, 3, 2)
    plt.title('Image Closing')
    plt.imshow(opening, cmap='gray')
    plt.axis('off')

    plt.subplot(1, 3, 3)
    plt.title('Image Opening')
    plt.imshow(closing, cmap='gray')
    plt.axis('off')

    plt.show()

# Example usage
input_image_path = 'img.png'
image_opening_closing(input_image_path)