import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread('img.png')

smoothed_image = cv2.GaussianBlur(image, (5, 5), 0)

kernel = np.array([[-1, -1, -1],
                   [-1, 9, -1],
                   [-1, -1, -1]])
sharpened_image = cv2.filter2D(image, -1, kernel)

plt.subplot(131), plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB)), plt.title('Original')
plt.subplot(132), plt.imshow(cv2.cvtColor(smoothed_image, cv2.COLOR_BGR2RGB)), plt.title('Smoothed')
plt.subplot(133), plt.imshow(cv2.cvtColor(sharpened_image, cv2.COLOR_BGR2RGB)), plt.title('Sharpened')
plt.show()