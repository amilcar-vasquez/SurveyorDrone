import unittest
from src.drone.tello_controller import TelloController
from src.vision.color_detector import ColorDetector
from src.vision.video_stream import VideoStream

class TestIntegration(unittest.TestCase):

    def setUp(self):
        self.tello_controller = TelloController()
        self.color_detector = ColorDetector()
        self.video_stream = VideoStream()

    def test_color_detection_and_movement(self):
        # Start the video stream
        self.video_stream.start()
        
        # Simulate a frame capture
        frame = self.video_stream.get_frame()
        
        # Detect color in the frame
        detected_color = self.color_detector.detect_color(frame)
        
        # Check if the detected color triggers a movement command
        if detected_color == "red":
            movement_command = self.tello_controller.move_forward()
        elif detected_color == "blue":
            movement_command = self.tello_controller.turn_left()
        else:
            movement_command = None
        
        # Assert that a movement command was issued for recognized colors
        self.assertIsNotNone(movement_command, "Movement command should not be None for recognized colors.")
        
        # Stop the video stream
        self.video_stream.stop()

    def tearDown(self):
        self.tello_controller.disconnect()

if __name__ == '__main__':
    unittest.main()