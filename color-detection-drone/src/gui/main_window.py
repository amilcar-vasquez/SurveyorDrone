from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
from .control_panel import ControlPanel
from .video_display import VideoDisplay

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Color Detection Drone Control")
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.control_panel = ControlPanel()
        self.video_display = VideoDisplay()

        self.layout.addWidget(self.control_panel)
        self.layout.addWidget(self.video_display)

        self.show()