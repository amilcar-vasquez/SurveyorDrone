class ColorDetector:
    def __init__(self, color_ranges):
        self.color_ranges = color_ranges

    def detect_color(self, frame):
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        detected_colors = {}

        for color_name, (lower, upper) in self.color_ranges.items():
            mask = cv2.inRange(hsv_frame, lower, upper)
            if cv2.countNonZero(mask) > 0:
                detected_colors[color_name] = mask

        return detected_colors

    def draw_detections(self, frame, detected_colors):
        for color_name, mask in detected_colors.items():
            contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            for contour in contours:
                if cv2.contourArea(contour) > 500:  # Minimum area to consider
                    x, y, w, h = cv2.boundingRect(contour)
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                    cv2.putText(frame, color_name, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        return frame

import cv2

def main():
    color_ranges = {
        'red': (np.array([0, 100, 100]), np.array([10, 255, 255])),
        'green': (np.array([40, 100, 100]), np.array([80, 255, 255])),
        'blue': (np.array([100, 100, 100]), np.array([140, 255, 255])),
    }

    color_detector = ColorDetector(color_ranges)

    cap = cv2.VideoCapture(0)  # Change to video stream source if needed

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        detected_colors = color_detector.detect_color(frame)
        frame_with_detections = color_detector.draw_detections(frame, detected_colors)

        cv2.imshow('Color Detection', frame_with_detections)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()