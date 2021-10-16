import cv2

# Face classifier
face_detector = cv2.CascadeClassifier('haarscascade_frontalface_default.xml')

# Get webcam
webcam = cv2.VideoCapture(0)

# Loop for reading frames continuously
while True:

    # Read the current frame from webcam
    successful_frame_read, frame = webcam.read()

    # Check if there is an error
    if not successful_frame_read:
        break

    # Change to greyscale for performance reasons
    frame_grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Show the current frame
    cv2.imshow('Smile Detector ', frame)

    # Display updating each millisecond by itself
    cv2.waitKey(1)

# Cleanup
webcam.release()
cv2.destroyAllWindows()

print("No errors")
