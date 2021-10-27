import cv2

# Face classifier
face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
smile_detector = cv2.CascadeClassifier('haarcascade_smile.xml')

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
    # minNeighbors determines how many detected smiles must be nearby
    faces = face_detector.detectMultiScale(frame_grayscale)

    # Run face detection within each of those faces
    for (x, y, w, h) in faces:

        # Draw rectangle around face
        # Rectangle will be drawn on color frame no frame_grayscale
        # (100, 200, 50) is RGB color of rectangle
        cv2.rectangle(frame, (x, y), (x+w, y+h), (100, 200, 50), 4)

        # Get the sub frame using numpy N-dim array slicing
        the_face = frame[y:y+h, x:x+w]

        # Change to grayscale
        face_grayscale = cv2.cvtColor(the_face, cv2.COLOR_BGR2GRAY)

        # Smiles only runs on face_grayscale
        smiles = smile_detector.detectMultiScale(face_grayscale, scaleFactor=1.7, minNeighbors=20)

        # Find all smiles inside of the face
        for (x_, y_, w_, h_) in smiles:

            # Draw rectangle around the smile
            # Rectangle will be drawn on color frame no frame_grayscale and (100, 200, 50) is RGB color of rectangle
            cv2.rectangle(the_face, (x_, y_), (x_+w_, y_+h_), (50, 50, 200), 4)

        # Label this face as smiling
        # if len(smiles) > 0:
        #     cv2.putText(frame, 'smiling', (x, y+h+40), fontScale=3,
        #     fontFace=cv2.FONT_HERSHEY_PLAIN, color=(255, 255, 255))

    # Show current frame
    cv2.imshow('Smile Detector', frame)

    # Display updating each millisecond by itself
    cv2.waitKey(1)

# Cleanup
webcam.release()
cv2.destroyAllWindows()

print("No errors")
