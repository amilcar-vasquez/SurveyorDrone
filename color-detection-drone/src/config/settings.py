# Configuration settings for the color detection drone application

# Video settings
VIDEO_RESOLUTION = (640, 480)  # Width, Height
FRAME_RATE = 30  # Frames per second

# Color detection settings
USE_YOLO = False  # Set to True to use YOLO for object detection
COLOR_DETECTION_METHOD = 'opencv'  # Options: 'opencv', 'yolo'

# Tello drone settings
TELLO_ADDRESS = ('192.168.10.1', 8889)  # Drone IP address and port
COMMAND_TIMEOUT = 5  # Timeout for drone command responses

# GUI settings
WINDOW_TITLE = "Color Detection Drone"
WINDOW_SIZE = (800, 600)  # Width, Height

# Logging settings
LOGGING_ENABLED = True  # Enable or disable logging
LOG_FILE_PATH = "drone_log.txt"  # Path to the log file

# Additional settings can be added as needed for future features or configurations.