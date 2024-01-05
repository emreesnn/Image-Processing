import cv2
import numpy as np
import matplotlib.pyplot as plt

def contrast_stretching_color(image_path, min_out=0, max_out=255):
    # Renkli görüntüyü oku
    image = cv2.imread(image_path)

    # Renk kanallarını ayrı ayrı işle
    stretched_channels = []
    for channel in cv2.split(image):
        min_in = np.min(channel)
        max_in = np.max(channel)
        stretched_channel = ((channel - min_in) / (max_in - min_in)) * (max_out - min_out) + min_out
        stretched_channel = np.clip(stretched_channel, min_out, max_out).astype(np.uint8)
        stretched_channels.append(stretched_channel)

    # Renkli görüntüyü birleştir
    stretched_image = cv2.merge(stretched_channels)

    # Görüntülerin yan yana gösterimi için subplot kullanma
    plt.figure(figsize=(12, 6))

    # Orjinal renkli görüntü
    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title('Orjinal Görüntü')

    # Kontrast germe sonrası renkli görüntü
    plt.subplot(1, 2, 2)
    plt.imshow(cv2.cvtColor(stretched_image, cv2.COLOR_BGR2RGB))
    plt.title('Kontrast Germe Sonrası')

    plt.show()

# Örnek olarak bir renkli görüntü yolu verelim
image_path_color = "contrast-stretching-image.png"
contrast_stretching_color(image_path_color)
