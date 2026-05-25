import numpy as np
import cv2
from thresholding import thresh


kernel = np.ones((3,3), np.uint8)

# Removing small noise
opening = cv2.morphologyEx(
    thresh,
    cv2.MORPH_OPEN,
    kernel,
    iterations=2
)

# Dilate to get clear background
clear_bg = cv2.dilate(opening, kernel, iterations=3)

# Distance transform
dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 5)

# Normalize for visualization
dist_norm = cv2.normalize(dist_transform, None, 0, 1.0, cv2.NORM_MINMAX)

# Finding sure foreground
_, clear_fg = cv2.threshold(
    dist_transform,
    0.4 * dist_transform.max(),
    255,
    0
)

clear_fg = np.uint8(clear_fg)

# Unknown region
unknown = cv2.subtract(clear_bg, clear_fg)

# Connected components (seed markers)
num_labels, markers = cv2.connectedComponents(clear_bg)

# Add 1 so background is not 0
markers = markers + 1

# mark unknown regions as 0
markers[unknown == 255] = 0

