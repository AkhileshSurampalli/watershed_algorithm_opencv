# Watershed Algorithm for Separating Touching Objects using OpenCV

## Overview

This project demonstrates the use of the Watershed Segmentation Algorithm to separate touching or overlapping objects in an image. A common challenge in computer vision is when multiple objects appear connected after thresholding and are detected as a single region. The watershed algorithm addresses this problem by identifying object centers and progressively separating connected regions.

In this implementation, touching tomatoes are used as an example, but the same approach can be applied to:

* Agricultural produce detection
* Cell segmentation in microscopy images
* Industrial object inspection
* Robotics perception systems
* Medical image analysis

---

## Problem Statement

When multiple objects touch each other, traditional segmentation techniques often produce a single connected component.

Example:

Before Segmentation:

(Tomato A touching Tomato B)

→ Detected as one object

Desired Output:

Tomato A → Object 1

Tomato B → Object 2

The Watershed Algorithm uses distance transforms and marker-based segmentation to separate these objects automatically.

---

## Methodology

### Step 1: Image Acquisition

The input image containing touching objects is loaded using OpenCV.

### Step 2: Preprocessing

The image is converted to grayscale and smoothed using Gaussian Blur to reduce noise.

Techniques used:

* Grayscale Conversion
* Gaussian Filtering

### Step 3: Thresholding

Otsu's thresholding converts the image into a binary mask separating foreground objects from the background.

### Step 4: Morphological Operations

Morphological opening removes small noise and dilation identifies the sure background region.

Operations used:

* Opening (Erosion + Dilation)
* Dilation

### Step 5: Distance Transform

The distance transform computes the distance of each foreground pixel from the nearest background pixel.

Object centers obtain the highest distance values, which serve as candidate markers.

### Step 6: Marker Extraction

Pixels above a selected threshold are identified as sure foreground regions.

Connected Component Analysis is then used to assign unique labels to each object center.

### Step 7: Watershed Segmentation

The watershed algorithm treats the image as a topographic surface.

Water starts filling from each marker and expands outward. When two regions meet, a boundary is created, effectively separating touching objects.

### Step 8: Visualization

The final boundaries are overlaid on the original image for visualization.

---

## Project Structure

```text
watershed_algorithm_opencv/
│
├── data/
│   └── tomatoes.jpg
│
├── src/
│   └── watershed.py
│
├── outputs/
│   └── watershed_output.jpg
│
├── requirements.txt
│
└── README.md
```

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd watershed_algorithm_opencv
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Requirements

```text
opencv-python
numpy
matplotlib
```

---

## Running the Project

Place your image inside the data folder and update the image path inside the script.

Run:

```bash
python src/watershed.py
```

The script will:

1. Load the image
2. Perform preprocessing
3. Compute the distance transform
4. Generate markers
5. Apply watershed segmentation
6. Display intermediate results
7. Save the final output image

---

## Results

The algorithm successfully separates touching objects by:

* Identifying object centers
* Generating unique markers
* Constructing watershed boundaries

This converts a single connected region into multiple individual object instances.

---

## Applications

### Agriculture

* Fruit counting
* Yield estimation
* Harvest automation

### Robotics

* Object perception
* Grasp planning
* Autonomous navigation

### Medical Imaging

* Cell segmentation
* Tissue analysis

### Industrial Inspection

* Counting overlapping products
* Quality control systems

---

## Future Improvements

Possible extensions include:

* Deep-learning-based instance segmentation using Mask R-CNN
* YOLO segmentation comparison

---

## References

* OpenCV Documentation
* Watershed Segmentation by Vincent and Soille
* Distance Transform in OpenCV
* Marker-Based Image Segmentation Techniques

---

## Author

Surampalli Akhilesh Gupta

Machine Learning Engineer | Robotics AI | Computer Vision | Sensor Fusion

