def convert_bgr_to_hsv(bgr_color):
    """Convert BGR color to HSV color space."""
    import cv2
    return cv2.cvtColor(np.uint8([[bgr_color]]), cv2.COLOR_BGR2HSV)[0][0]

def is_color_in_range(hsv_color, lower_bound, upper_bound):
    """Check if the given HSV color is within the specified range."""
    return all(lower <= value <= upper for value, lower, upper in zip(hsv_color, lower_bound, upper_bound))

def draw_rectangle(frame, color, position, size):
    """Draw a rectangle on the frame for visualization."""
    x, y = position
    width, height = size
    cv2.rectangle(frame, (x, y), (x + width, y + height), color, 2)

def process_frame(frame, color_detector):
    """Process a video frame for color detection."""
    detected_color = color_detector.detect_color(frame)
    if detected_color:
        # Example: Draw a rectangle around detected color
        draw_rectangle(frame, (0, 255, 0), (50, 50), (100, 100))  # Placeholder values
    return frame

def load_hsv_ranges(file_path):
    """Load HSV ranges from a JSON file."""
    import json
    with open(file_path, 'r') as file:
        return json.load(file)