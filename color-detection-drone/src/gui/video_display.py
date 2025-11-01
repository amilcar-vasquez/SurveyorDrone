import cv2
from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QImage, QPixmap

class VideoDisplay(QLabel):
    def __init__(self):
        super().__init__()
        self.setFixedSize(640, 480)  # Set the size of the video display

    def update_frame(self, frame):
        """Update the video display with a new frame."""
        if frame is not None:
            # Convert the frame from BGR to RGB format
            rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            h, w, ch = rgb_image.shape
            bytes_per_line = ch * w
            q_image = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
            self.setPixmap(QPixmap.fromImage(q_image))

    def clear_display(self):
        """Clear the video display."""
        self.clear()