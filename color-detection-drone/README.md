# Color Detection Drone Project

This project integrates a Tello drone with color detection capabilities using OpenCV and YOLO. The application features a graphical user interface (GUI) that allows users to control the drone and visualize the video stream while detecting specific colors to perform movements.

## Project Structure

```
color-detection-drone
├── src
│   ├── main.py                  # Entry point for the application
│   ├── drone
│   │   ├── __init__.py
│   │   ├── tello_controller.py  # Manages drone connection and movement commands
│   │   └── movement_commands.py  # Defines movement commands for the drone
│   ├── vision
│   │   ├── __init__.py
│   │   ├── color_detector.py     # Implements color detection using OpenCV
│   │   ├── video_stream.py       # Handles video streaming from the drone
│   │   └── yolo_detector.py      # Integrates YOLO for advanced object detection
│   ├── gui
│   │   ├── __init__.py
│   │   ├── main_window.py        # Sets up the main GUI window
│   │   ├── control_panel.py      # Provides user controls for the drone
│   │   └── video_display.py      # Displays the video stream in the GUI
│   ├── config
│   │   ├── __init__.py
│   │   ├── settings.py           # Configuration settings for the application
│   │   └── color_ranges.py       # Defines color ranges for detection
│   └── utils
│       ├── __init__.py
│       └── helpers.py            # Utility functions for various tasks
├── models
│   ├── yolo
│   │   └── weights.pt            # Pre-trained weights for the YOLO model
│   └── color_calibration
│       └── hsv_ranges.json       # Calibrated HSV color ranges for detection
├── tests
│   ├── __init__.py
│   ├── test_color_detection.py    # Unit tests for color detection functionality
│   ├── test_drone_control.py      # Unit tests for drone control commands
│   └── test_integration.py        # Integration tests for component interactions
├── requirements.txt               # Lists project dependencies
├── setup.py                       # Packaging information for the application
├── config.yaml                    # Configuration settings in YAML format
└── README.md                      # Documentation for the project
```

## Features

- **Color Detection**: Detects specific colors in the video stream using OpenCV.
- **Object Detection**: Integrates YOLO for advanced object detection capabilities.
- **Drone Control**: Sends movement commands to the Tello drone based on detected colors.
- **Graphical User Interface**: Provides an intuitive interface for users to control the drone and view the video stream.

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd color-detection-drone
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Ensure that the Tello drone is powered on and connected to the same network as your computer.

## Usage

To run the application, execute the following command:
```
python src/main.py
```

Follow the on-screen instructions to control the drone and utilize the color detection features.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE.md file for more details.