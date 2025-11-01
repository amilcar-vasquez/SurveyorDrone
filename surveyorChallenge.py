import socket
import time

# --- Tello connection details ---
TELLO_IP = '192.168.10.1'
TELLO_PORT = 8889
ADDR = (TELLO_IP, TELLO_PORT)

# --- Create UDP socket ---
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', 9000))  # our local port

def send_cmd(cmd, delay=3):
    """Send command to Tello and wait briefly."""
    print(f">> {cmd}")
    sock.sendto(cmd.encode('utf-8'), ADDR)
    time.sleep(delay)

try:
    # --- 1. SDK mode ---
    send_cmd("command", 2)

    # --- 2. Take off ---
    send_cmd("takeoff", 6)

    # --- 3. Fly to Target A (simulate center) ---
    send_cmd("forward 50", 5)   # move forward 50cm
    send_cmd("cw 360", 6)       # spin 360 degrees

    # --- 4. Target B: Move, climb, and take photo (simulate) ---
    send_cmd("right 80", 5)     # fly right toward Target B
    send_cmd("up 50", 3)        # ascend to specific altitude
    print("📸 Simulating photo capture at Target B")
    time.sleep(2)

    # --- 5. Obstacle maneuver (flip) ---
    send_cmd("forward 50", 4)
    send_cmd("flip f", 4)       # flip forward to clear imaginary obstacle

    # --- 6. Land at Target D ---
    send_cmd("back 50", 5)
    send_cmd("land", 6)

    print("✅ Mission completed successfully!")

except KeyboardInterrupt:
    print("\n🛑 Emergency stop")
    send_cmd("emergency")
finally:
    sock.close()
