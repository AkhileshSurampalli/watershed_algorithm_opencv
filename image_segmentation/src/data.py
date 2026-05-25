
import cv2
import numpy as np
import matplotlib.pyplot as plt

IMAGE_PATH = "C:/Users/suram/OneDrive/Desktop/YT_MLOps/two-tomatoes-on-a-wood-floor-EFNY6P.jpg"

image = cv2.imread(IMAGE_PATH)

if image is None:
    raise FileNotFoundError(f"Could not load image :{IMAGE_PATH}")

original = image.copy()


# Convert image from RGB to BGR for visualization
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)