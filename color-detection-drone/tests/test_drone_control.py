import unittest
from src.drone.tello_controller import TelloController
from src.drone.movement_commands import move_forward, move_backward, turn_left, turn_right

class TestDroneControl(unittest.TestCase):

    def setUp(self):
        self.controller = TelloController()

    def test_move_forward(self):
        result = move_forward()
        self.assertEqual(result, "Moving forward")

    def test_move_backward(self):
        result = move_backward()
        self.assertEqual(result, "Moving backward")

    def test_turn_left(self):
        result = turn_left()
        self.assertEqual(result, "Turning left")

    def test_turn_right(self):
        result = turn_right()
        self.assertEqual(result, "Turning right")

    def test_tello_connection(self):
        self.assertTrue(self.controller.connect(), "Failed to connect to Tello drone")

    def test_send_command(self):
        command = "takeoff"
        response = self.controller.send_command(command)
        self.assertIn(response, ["ok", "error"], "Unexpected response from Tello drone")

if __name__ == '__main__':
    unittest.main()