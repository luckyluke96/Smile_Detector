import cv2

# Face classifier
face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
smile_detector = cv2.CascadeClassifier('haarscascade_smile.xml')

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

    # Detect faces first
    # MultiScale detects faces of every scale
    faces = face_detector.detectMultiScale(frame_grayscale)

    # Run smile detection within each of those faces
    for (x, y, w, h) in faces:

        # Draw rectangle around face
        # Rectangle will be drawn on color frame no frame_grayscale
        # (100, 200, 50) is RGB color of rectangle
        cv2.rectangle(frame, (x, y), (x+w, y+h), (100, 200, 50), 4)

    # Show current frame
    cv2.imshow('Smile Detector', frame)

    # Display updating each millisecond by itself
    cv2.waitKey(1)

# Cleanup
webcam.release()
cv2.destroyAllWindows()

print("No errors")
