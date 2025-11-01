import sys
import cv2
from src.gui.main_window import MainWindow
from src.vision.video_stream import VideoStream
from src.vision.color_detector import ColorDetector
from src.drone.tello_controller import TelloController

def main():
    # Initialize the Tello drone controller
    tello_controller = TelloController()

    # Start the video stream from the drone
    video_stream = VideoStream(tello_controller)
    color_detector = ColorDetector()

    # Create the main GUI window
    app = MainWindow(video_stream, color_detector)

    # Start the video stream in a separate thread
    video_stream.start()

    # Run the application
    try:
        app.run()
    except KeyboardInterrupt:
        print("Shutting down...")
    finally:
        video_stream.stop()
        tello_controller.close()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()