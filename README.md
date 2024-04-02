# Facial Recognition with OpenCV

This Python script uses OpenCV to perform facial recognition on a live video feed from the default camera (usually the webcam).

## Dependencies

- OpenCV: This script uses OpenCV for image processing and facial recognition. You can install it with pip:

```bash
pip install opencv-python
```

## How it works

1. The script first loads the Haar Cascade classifier for frontal face detection provided by OpenCV.

2. It then starts capturing video from the default camera (camera index 0).

3. For each frame of the video:

   - The frame is converted to grayscale, as the face detection algorithm works on grayscale images.

   - The face detection algorithm is run on the grayscale image, which returns a list of rectangles where faces are detected.

   - For each detected face, a rectangle is drawn on the original (colored) frame, and the face region is saved.

   - The original frame, with rectangles drawn around detected faces, is displayed in a window titled 'img'.

   - If a face was detected in the frame, the last detected face is displayed in a separate window titled 'Last face'.

4. The script continues processing frames and displaying results until the user presses the 'Esc' key.

## Usage

To run the script, simply execute the Python file in your terminal:

```bash
python facialrecognition.py
```

Press the 'Esc' key to stop the script.
