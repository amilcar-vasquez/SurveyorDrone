import sys
from PyQt5.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
                             QPushButton, QLabel, QTextEdit, QGridLayout)
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QFont
from .video_display import VideoDisplay

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Color Detection Drone Controller")
        self.setGeometry(100, 100, 1000, 700)
        
        # Create central widget and main layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QHBoxLayout(central_widget)
        
        # Create video display area
        self.video_display = VideoDisplay()
        main_layout.addWidget(self.video_display, 2)  # 2/3 of width
        
        # Create control panel
        control_panel = self.create_control_panel()
        main_layout.addWidget(control_panel, 1)  # 1/3 of width
        
        # Status label
        self.status_label = QLabel("Status: Disconnected")
        self.status_label.setStyleSheet("color: red; font-weight: bold;")
        
        # Create status bar
        self.statusBar().addWidget(self.status_label)
        
        # Timer for video updates (placeholder)
        self.video_timer = QTimer()
        self.video_timer.timeout.connect(self.update_video)
        
    def create_control_panel(self):
        """Create the drone control panel."""
        panel = QWidget()
        layout = QVBoxLayout(panel)
        
        # Connection controls
        layout.addWidget(QLabel("Connection"))
        self.connect_btn = QPushButton("Connect to Drone")
        self.connect_btn.clicked.connect(self.connect_drone)
        layout.addWidget(self.connect_btn)
        
        self.start_video_btn = QPushButton("Start Video")
        self.start_video_btn.clicked.connect(self.start_video)
        self.start_video_btn.setEnabled(False)
        layout.addWidget(self.start_video_btn)
        
        # Movement controls
        layout.addWidget(QLabel("Manual Controls"))
        movement_grid = QGridLayout()
        
        # Create movement buttons
        self.takeoff_btn = QPushButton("Takeoff")
        self.land_btn = QPushButton("Land")
        self.up_btn = QPushButton("↑")
        self.down_btn = QPushButton("↓")
        self.left_btn = QPushButton("←")
        self.right_btn = QPushButton("→")
        self.forward_btn = QPushButton("Forward")
        self.backward_btn = QPushButton("Backward")
        
        # Arrange buttons in grid
        movement_grid.addWidget(self.takeoff_btn, 0, 0, 1, 2)
        movement_grid.addWidget(self.land_btn, 0, 2, 1, 2)
        movement_grid.addWidget(self.up_btn, 1, 1)
        movement_grid.addWidget(self.left_btn, 2, 0)
        movement_grid.addWidget(self.right_btn, 2, 2)
        movement_grid.addWidget(self.down_btn, 3, 1)
        movement_grid.addWidget(self.forward_btn, 1, 3)
        movement_grid.addWidget(self.backward_btn, 3, 3)
        
        movement_widget = QWidget()
        movement_widget.setLayout(movement_grid)
        layout.addWidget(movement_widget)
        
        # Color detection controls
        layout.addWidget(QLabel("Color Detection"))
        self.color_detection_btn = QPushButton("Start Color Detection")
        self.color_detection_btn.clicked.connect(self.toggle_color_detection)
        self.color_detection_btn.setEnabled(False)
        layout.addWidget(self.color_detection_btn)
        
        # Log area
        layout.addWidget(QLabel("Command Log"))
        self.log_text = QTextEdit()
        self.log_text.setMaximumHeight(150)
        self.log_text.setReadOnly(True)
        layout.addWidget(self.log_text)
        
        # Connect button signals
        self.takeoff_btn.clicked.connect(lambda: self.log_command("Takeoff"))
        self.land_btn.clicked.connect(lambda: self.log_command("Land"))
        self.up_btn.clicked.connect(lambda: self.log_command("Move Up"))
        self.down_btn.clicked.connect(lambda: self.log_command("Move Down"))
        self.left_btn.clicked.connect(lambda: self.log_command("Move Left"))
        self.right_btn.clicked.connect(lambda: self.log_command("Move Right"))
        self.forward_btn.clicked.connect(lambda: self.log_command("Move Forward"))
        self.backward_btn.clicked.connect(lambda: self.log_command("Move Backward"))
        
        return panel
    
    def connect_drone(self):
        """Handle drone connection."""
        self.log_command("Attempting to connect to drone...")
        self.status_label.setText("Status: Connected")
        self.status_label.setStyleSheet("color: green; font-weight: bold;")
        self.connect_btn.setText("Disconnect")
        self.start_video_btn.setEnabled(True)
        self.color_detection_btn.setEnabled(True)
        
    def start_video(self):
        """Start video stream."""
        self.log_command("Starting video stream...")
        self.video_timer.start(33)  # ~30 FPS
        self.start_video_btn.setText("Stop Video")
        
    def update_video(self):
        """Update video display (placeholder)."""
        # This would be replaced with actual video feed from drone
        import numpy as np
        dummy_frame = np.random.randint(0, 255, (480, 640, 3), dtype=np.uint8)
        self.video_display.update_frame(dummy_frame)
        
    def toggle_color_detection(self):
        """Toggle color detection."""
        if self.color_detection_btn.text() == "Start Color Detection":
            self.log_command("Starting color detection...")
            self.color_detection_btn.setText("Stop Color Detection")
        else:
            self.log_command("Stopping color detection...")
            self.color_detection_btn.setText("Start Color Detection")
    
    def log_command(self, command):
        """Log command to the text area."""
        self.log_text.append(f"> {command}")
        self.log_text.verticalScrollBar().setValue(
            self.log_text.verticalScrollBar().maximum()
        )