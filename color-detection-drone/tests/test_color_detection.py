import unittest
from src.vision.color_detector import ColorDetector
import cv2
import numpy as np

class TestColorDetector(unittest.TestCase):

    def setUp(self):
        self.color_detector = ColorDetector()

    def test_color_detection_red(self):
        # Create a red image
        red_image = np.zeros((100, 100, 3), dtype=np.uint8)
        red_image[:] = [0, 0, 255]  # OpenCV uses BGR format

        detected_color = self.color_detector.detect_color(red_image)
        self.assertEqual(detected_color, 'red')

    def test_color_detection_green(self):
        # Create a green image
        green_image = np.zeros((100, 100, 3), dtype=np.uint8)
        green_image[:] = [0, 255, 0]  # OpenCV uses BGR format

        detected_color = self.color_detector.detect_color(green_image)
        self.assertEqual(detected_color, 'green')

    def test_color_detection_blue(self):
        # Create a blue image
        blue_image = np.zeros((100, 100, 3), dtype=np.uint8)
        blue_image[:] = [255, 0, 0]  # OpenCV uses BGR format

        detected_color = self.color_detector.detect_color(blue_image)
        self.assertEqual(detected_color, 'blue')

    def test_color_detection_no_color(self):
        # Create a black image
        black_image = np.zeros((100, 100, 3), dtype=np.uint8)

        detected_color = self.color_detector.detect_color(black_image)
        self.assertEqual(detected_color, 'none')

if __name__ == '__main__':
    unittest.main()