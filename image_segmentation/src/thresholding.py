import cv2
from preprocessing import blur

# Otsu thresholding
_, thresh = cv2.threshold(
    blur,
    0, 255,
    cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU
)

# Invert if background/object are reversed
threshold = 255 - thresh