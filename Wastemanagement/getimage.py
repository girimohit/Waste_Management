import cv2
import time

def capture_image():
    # Open default camera (usually the built-in webcam)
    cap = cv2.VideoCapture(0)

    # Check if the camera is opened successfully
    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    start_time = time.time()
    while True:
        # Read a frame from the camera
        ret, frame = cap.read()

        # Check if the frame is read successfully
        if not ret:
            print("Error: Could not read frame.")
            break

        # Display the frame
        cv2.imshow('Camera Feed', frame)

        # Capture image after 3 seconds
        if time.time() - start_time > 3:
            # Save the frame as an image file
            cv2.imwrite('waste1.jpg', frame)
            print("Image captured successfully!")
            break

        # Check for key press to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera
    cap.release()

    # Close OpenCV windows
    cv2.destroyAllWindows()

if __name__ == "__main__":
    capture_image()
