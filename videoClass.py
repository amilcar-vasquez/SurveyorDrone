## to be called by testflight.py to run video streaming  and decoding 

#Import OpenCV Library
import cv2

class Video:
    
    def __init__(self):
        # Tello video stream address
        self.tello_video_address = 'udp://@0.0.0.0:11111'
        self.video_capture = cv2.VideoCapture(self.tello_video_address)
        self.video_capture.set(cv2.CAP_PROP_BUFFERSIZE, 1)
        
    def start_video(self):
        
        if not self.video_capture.isOpened():
            print("Error: Could not open video stream.")
            return
        
        print("Starting video stream. Press 'q' to exit.")
        
        while True:
            ret, frame = self.video_capture.read()
            if not ret:
                print("Error: Could not read frame.")
                break
            
            cv2.imshow('Tello Video Stream', frame)
            
            # Exit on 'q' key press
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        
        self.video_capture.release()
        cv2.destroyAllWindows() 
        
        
