NumPy Image Editor

A beginner-friendly image processing project built using Python, NumPy, Pillow, and SciPy.
This project demonstrates how images are represented as arrays and how basic image processing operations work behind the scenes in AI and Computer Vision.

Features

✅ Convert image to grayscale
✅ Adjust image brightness
✅ Rotate image
✅ Apply blur effect
✅ Detect edges in images

Technologies Used
Python
NumPy
Pillow
SciPy
Project Structure
numpy-image-editor/
│
├── main.py
├── image.jpg
├── requirements.txt
├── README.md
├── output/
│   ├── grayscale.jpg
│   ├── bright.jpg
│   ├── rotated.jpg
│   ├── blur.jpg
│   └── edges.jpg
How It Works

Images are converted into NumPy arrays where each pixel is represented by RGB values.

This project performs operations directly on those arrays using:

Array manipulation
Matrix operations
Broadcasting
Convolution kernels

These concepts are widely used in:

Artificial Intelligence
Computer Vision
Deep Learning
Image Processing
Installation

Clone the repository:

git clone https://github.com/YOUR_USERNAME/numpy-image-editor.git

Move into the project folder:

cd numpy-image-editor

Install dependencies:

pip install -r requirements.txt
Run the Project
python main.py
