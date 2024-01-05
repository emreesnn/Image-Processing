import cv2
import numpy as np
import matplotlib.pyplot as plt


def color_based_segmentation(image_path, lower_bound, upper_bound):
    image = cv2.imread(image_path)

    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    mask = cv2.inRange(image_rgb, lower_bound, upper_bound)

    segmented_image = cv2.bitwise_and(image_rgb, image_rgb, mask=mask)

    plt.figure(figsize=(12, 6))

    plt.subplot(1, 3, 1)
    plt.imshow(image_rgb)
    plt.title('Orijinal Görüntü')

    plt.subplot(1, 3, 2)
    plt.imshow(mask, cmap='gray')
    plt.title('Renk Tabanlı Maske')

    plt.subplot(1, 3, 3)
    plt.imshow(segmented_image)
    plt.title('Renk Tabanlı Bölütlenmiş Görüntü')

    plt.show()

image_path_color = "img_1.png"

lower_bound = np.array([100, 0, 0], dtype=np.uint8)
upper_bound = np.array([255, 140, 255], dtype=np.uint8)

color_based_segmentation(image_path_color, lower_bound, upper_bound)
