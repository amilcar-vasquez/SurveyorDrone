def move_forward(drone, distance):
    """Move the drone forward by a specified distance."""
    print(f"Moving forward {distance} meters.")
    # Implement the command to move the drone forward
    drone.send_command(f"forward {distance}")

def move_backward(drone, distance):
    """Move the drone backward by a specified distance."""
    print(f"Moving backward {distance} meters.")
    # Implement the command to move the drone backward
    drone.send_command(f"back {distance}")

def turn_left(drone, angle):
    """Turn the drone left by a specified angle."""
    print(f"Turning left {angle} degrees.")
    # Implement the command to turn the drone left
    drone.send_command(f"cw {angle}")

def turn_right(drone, angle):
    """Turn the drone right by a specified angle."""
    print(f"Turning right {angle} degrees.")
    # Implement the command to turn the drone right
    drone.send_command(f"ccw {angle}")

def hover(drone):
    """Make the drone hover in place."""
    print("Hovering in place.")
    # Implement the command to make the drone hover
    drone.send_command("stop")