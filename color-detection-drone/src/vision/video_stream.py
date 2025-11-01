import cv2
import numpy as np
from src.vision.color_detector import ColorDetector

class VideoStream:
    def __init__(self, drone_controller):
        self.drone_controller = drone_controller
        self.cap = cv2.VideoCapture(0)  # Change to appropriate video source if needed
        self.color_detector = ColorDetector()

    def start_stream(self):
        while True:
            ret, frame = self.cap.read()
            if not ret:
                print("Failed to grab frame")
                break

            detected_color = self.color_detector.detect_color(frame)
            self.perform_action_based_on_color(detected_color)

            cv2.imshow("Drone Video Stream", frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        self.cap.release()
        cv2.destroyAllWindows()

    def perform_action_based_on_color(self, color):
        if color == "red":
            self.drone_controller.move_forward()
        elif color == "blue":
            self.drone_controller.turn_left()
        elif color == "green":
            self.drone_controller.turn_right()
        elif color == "yellow":
            self.drone_controller.move_backward()
        else:
            print("No recognized color detected.")

