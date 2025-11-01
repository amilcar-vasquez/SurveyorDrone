from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel
from PyQt5.QtCore import pyqtSignal, QObject

class ControlPanel(QWidget):
    command_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.label = QLabel("Control Panel")
        layout.addWidget(self.label)

        self.takeoff_button = QPushButton("Take Off")
        self.takeoff_button.clicked.connect(self.take_off)
        layout.addWidget(self.takeoff_button)

        self.land_button = QPushButton("Land")
        self.land_button.clicked.connect(self.land)
        layout.addWidget(self.land_button)

        self.forward_button = QPushButton("Move Forward")
        self.forward_button.clicked.connect(self.move_forward)
        layout.addWidget(self.forward_button)

        self.backward_button = QPushButton("Move Backward")
        self.backward_button.clicked.connect(self.move_backward)
        layout.addWidget(self.backward_button)

        self.left_button = QPushButton("Turn Left")
        self.left_button.clicked.connect(self.turn_left)
        layout.addWidget(self.left_button)

        self.right_button = QPushButton("Turn Right")
        self.right_button.clicked.connect(self.turn_right)
        layout.addWidget(self.right_button)

        self.setLayout(layout)

    def take_off(self):
        self.command_signal.emit("takeoff")

    def land(self):
        self.command_signal.emit("land")

    def move_forward(self):
        self.command_signal.emit("move_forward")

    def move_backward(self):
        self.command_signal.emit("move_backward")

    def turn_left(self):
        self.command_signal.emit("turn_left")

    def turn_right(self):
        self.command_signal.emit("turn_right")