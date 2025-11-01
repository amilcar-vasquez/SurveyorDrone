# File: /color-detection-drone/color-detection-drone/src/drone/tello_controller.py

import socket
import time
import sys
from .movement_commands import move_forward, move_backward, turn_left, turn_right
from vision.color_detector import ColorDetector

class TelloController:
    def __init__(self, address=('192.168.10.1', 8889)):
        self.address = address
        self.sock = self.setup_connection()
        self.color_detector = ColorDetector()

    def setup_connection(self):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.bind(('', 9000))
            sock.settimeout(5)
            print("Socket created and bound.")
            return sock
        except Exception as e:
            print(f"Error creating socket: {e}")
            sys.exit(1)

    def send_command(self, command):
        try:
            self.sock.sendto(command.encode('utf-8'), self.address)
            response, _ = self.sock.recvfrom(1024)
            print(f"<< {response.decode('utf-8')}")
            return response.decode('utf-8').strip().lower() != 'error'
        except socket.timeout:
            print("No response from drone.")
            return False
        except Exception as e:
            print(f"Error sending command '{command}': {e}")
            return False

    def execute_movement_based_on_color(self, frame):
        detected_color = self.color_detector.detect_color(frame)
        if detected_color:
            if detected_color == 'red':
                move_forward()
            elif detected_color == 'blue':
                move_backward()
            elif detected_color == 'green':
                turn_left()
            elif detected_color == 'yellow':
                turn_right()

    def close_connection(self):
        self.sock.close()
        print("Connection closed.")