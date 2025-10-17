# Author: D'Alesseo Requena 
# Date: 2025-10-17
# Description: This code tests the fight mechanics of the TLW004 drone model.


# Hardware Components Used:
# - TLW004 Drone Model

# Software Libraries Used:
import cmd
import socket
import time
import sys
from turtle import delay

# Tello connection setup
tello_address = ('192.168.10.1', 8889) 
print("Connecting to Tello Drone...")

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
    sock.bind(('', 9000))
    sock.settimeout(5)  # Set timeout for responses
    print("Socket created and bound.")
except Exception as e:
    print(f"Error creating socket: {e}")
    sys.exit(1)

def send(cmd, delay=3): 
    try:
        print(f">> {cmd}") 
        sock.sendto(cmd.encode('utf-8'), tello_address)
        
        # Wait for response to confirm drone is connected
        try:
            response, addr = sock.recvfrom(1024)
            print(f"<< {response.decode('utf-8')}")
            
            if response.decode('utf-8').strip().lower() == 'error':
                print("Drone returned error. Stopping execution.")
                sock.close()
                sys.exit(1)
                
        except socket.timeout:
            print("No response from drone. Drone may not be connected.")
            print("Stopping execution.")
            sock.close()
            sys.exit(1)
            
        time.sleep(delay)
        
    except Exception as e:
        print(f"Error sending command '{cmd}': {e}")
        print("Drone not found or connection failed. Stopping execution.")
        sock.close()
        sys.exit(1)

# Mission Sequence 
try:
    send("command")          
    send("takeoff")         
    send("land")             
except KeyboardInterrupt:
    print("\nOperation interrupted by user.")
finally:
    sock.close()
    print("Connection closed.")