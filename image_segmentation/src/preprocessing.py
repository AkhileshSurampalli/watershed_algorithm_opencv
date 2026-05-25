from image_segmentation.src.data import image
import cv2

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Gaussian blur to remove noise
blur = cv2.GaussianBlur(gray, (7, 7), 0)

