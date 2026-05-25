from PIL import Image
import numpy as np
from scipy.signal import convolve2d
import os

# Create output folder
os.makedirs("output", exist_ok=True)

# Load image
img = Image.open("image.jpg")

# Convert image to numpy array
img_array = np.array(img)

print("Image Shape:", img_array.shape)

# -----------------------------
# 1. GRAYSCALE
# -----------------------------
gray = np.mean(img_array, axis=2)

gray_img = Image.fromarray(gray.astype(np.uint8))

gray_img.save("output/grayscale.jpg")

print("Grayscale image saved!")

# -----------------------------
# 2. BRIGHTNESS
# -----------------------------
bright = img_array + 50

bright = np.clip(bright, 0, 255)

bright_img = Image.fromarray(bright.astype(np.uint8))

bright_img.save("output/bright.jpg")

print("Bright image saved!")

# -----------------------------
# 3. ROTATE
# -----------------------------
rotated = np.rot90(img_array)

rotated_img = Image.fromarray(rotated.astype(np.uint8))

rotated_img.save("output/rotated.jpg")

print("Rotated image saved!")

# -----------------------------
# 4. BLUR
# -----------------------------
kernel_blur = np.ones((3, 3)) / 9

blurred = convolve2d(gray, kernel_blur, mode='same')

blurred = np.clip(blurred, 0, 255)

blurred_img = Image.fromarray(blurred.astype(np.uint8))

blurred_img.save("output/blur.jpg")

print("Blurred image saved!")

# -----------------------------
# 5. EDGE DETECTION
# -----------------------------
kernel_edge = np.array([
    [-1, -1, -1],
    [-1,  8, -1],
    [-1, -1, -1]
])

edges = convolve2d(gray, kernel_edge, mode='same')

edges = np.clip(edges, 0, 255)

edge_img = Image.fromarray(edges.astype(np.uint8))

edge_img.save("output/edges.jpg")

print("Edge image saved!")

print("\nAll images processed successfully!")