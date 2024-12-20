# Face Recognition Attendance System

An automated attendance system that uses facial recognition to track attendance and generate CSV reports. The system captures video from a webcam, recognizes faces, and maintains attendance records in real-time.

## Features

- Real-time face detection and recognition
- Automated attendance marking
- Daily CSV report generation
- Simple and intuitive user interface
- Support for multiple face recognition
- Visual feedback with bounding boxes and names

## Prerequisites

Before running this system, make sure you have the following installed:

- Python 3.6 or higher
- OpenCV (`cv2`)
- face_recognition library
- NumPy
- A working webcam

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/Face-Recognition-Attendance-System.git
cd Face-Recognition-Attendance-System
```

2. Install the required packages:
```bash
pip install opencv-python
pip install face-recognition
pip install numpy
```

## Project Structure

```
Face-Recognition-Attendance-System/
│
├── main.py                 # Main application file
├── itachi.jpg             # Sample known face
├── kakashi.jpg            # Sample known face
└── YYYY-MM-DD.csv         # Generated attendance report
```

## Usage

1. Add known faces:
   - Place clear, front-facing photos of people in the project directory
   - Update the `known_face_encodings` and `known_face_names` lists in the code with new entries

2. Run the system:
```bash
python main.py
```

3. System operation:
   - The webcam will activate and begin detecting faces
   - Recognized faces will be highlighted with a green box
   - Names will be displayed below the face boxes
   - Attendance is automatically marked in a CSV file
   - Press 'q' to quit the application

## Attendance Records

- Attendance is recorded in a CSV file named with the current date (YYYY-MM-DD.csv)
- Each entry contains:
  - Name of the recognized person
  - Time of recognition
- A person's attendance is marked only once per session

## Customization

You can modify the following aspects of the system:

1. Recognition Parameters:
   - Adjust frame resize factors (`fx` and `fy`) for performance
   - Modify recognition tolerance in `compare_faces`

2. Visual Elements:
   - Change bounding box colors
   - Modify text size and font
   - Adjust box dimensions

## Troubleshooting

Common issues and solutions:

1. Camera not detected:
   - Check if your webcam is properly connected
   - Verify webcam permissions
   - Try changing the camera index in `VideoCapture(0)`

2. Face not recognized:
   - Ensure proper lighting
   - Use clear, front-facing reference photos
   - Check if face is within camera frame

3. Performance issues:
   - Reduce frame resolution
   - Ensure sufficient system resources
   - Close other resource-intensive applications

## Contributing

Feel free to contribute to this project by:
1. Forking the repository
2. Creating a new branch
3. Making your changes
4. Submitting a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- OpenCV team for computer vision tools
- face_recognition library developers
- NumPy contributors