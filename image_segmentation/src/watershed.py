import os
import sys
import cv2

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from image_segmentation.src.data import image
from image_segmentation.src.data import image_rgb
from preprocessing import gray
from thresholding import thresh
from morphological import dist_norm
from morphological import markers
from morphological import clear_fg
import numpy as np
import matplotlib.pyplot as plt


markers = cv2.watershed(image, markers)

# Boundary marked with -1
image[markers == -1] = [255, 0, 0]

# Count objects

# Total tomatoes
num_objects = len(np.unique(markers)) - 2

print(f"Detected Objects: {num_objects}")

# Visualization

fig, ax = plt.subplots(2, 3, figsize=(15, 10))

ax[0, 0].imshow(image_rgb)
ax[0, 0].set_title("Original Image")
ax[0, 0].axis("off")

ax[0, 1].imshow(gray, cmap="gray")
ax[0, 1].set_title("Gray Image")
ax[0, 1].axis("off")

ax[0, 2].imshow(thresh, cmap="gray")
ax[0, 2].set_title("Threshold")
ax[0, 2].axis("off")

ax[1, 0].imshow(dist_norm, cmap="jet")
ax[1, 0].set_title("Distance Transform")
ax[1, 0].axis("off")

ax[1, 1].imshow(clear_fg, cmap="gray")
ax[1, 1].set_title("Sure Foreground")
ax[1, 1].axis("off")

ax[1, 2].imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
ax[1, 2].set_title("Watershed Result")
ax[1, 2].axis("off")

plt.tight_layout()
plt.show()
