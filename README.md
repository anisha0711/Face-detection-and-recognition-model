# Face Detection and Recognition Model

## Model Description:
This model is a comprehensive system built using Python, Computer Vision library OpenCV and machine learning techniques. The model consists of two main components: face detection and face recognition.

### Face Detection:
The face detection component locates and identifies human faces within images or video streams. Once a face is detected, bounding boxes are drawn around the detected faces, providing visual cues for their location.

### Face Recognition:
The face recognition component recognizes individual faces within the detected regions. Extract features from the detected faces, such as texture and patterns, and generates histograms that represent these features. These histograms are then compared against a database of known faces, allowing the model to identify and classify each detected face.

## Languages and Technologies Used:
- Python (3x)
- OpenCV library
- Machine Learning and Computer Vision

## Algorithms Used:
### Haar Cascade Algorithm:
The Haar Cascade algorithm is a machine learning-based approach used for object detection in images. It works by training a cascade classifier with positive and negative images of the target object. This classifier then scans the input image at different scales and detects the presence of the object based on predefined features called Haar-like features. In our project, the Haar Cascade algorithm is utilized for face detection, enabling us to locate faces within an image or video stream.

### LBPH (Local Binary Patterns Histograms) Algorithm:
LBPH is a texture-based approach used for image recognition and classification. It operates by dividing the image into regions and extracting local binary patterns from each region. These patterns are then converted into histograms, which serve as feature vectors for classification. In our project, the LBPH algorithm is employed for face recognition, allowing us to identify and differentiate between different faces detected by the Haar Cascade algorithm.

By combining these two algorithms, this system is capable of accurately detecting and recognizing faces in various settings and conditions.

## Installations
```
pip install opencv-python
pip install face
pip install opencv-contrib-python
pip install pillow
pip install numpy
```

## Usage

Happy coding! 🚀👩‍💻👨‍💻
