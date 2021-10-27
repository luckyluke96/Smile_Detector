import socket
import time
import cv2

host, port = "127.0.0.1", 25001
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, port))

# Face classifier
face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
smile_detector = cv2.CascadeClassifier('haarcascade_smile.xml')

# Get webcam
webcam = cv2.VideoCapture(0)

def sendSmile():
    startPos[1] +=1 #increase x by one
    posString = ','.join(map(str, startPos)) #Converting Vector3 to a string, example "0,0,0"
    print(posString)

    # smileDetectedString = 'InitAction'
    # sock.sendall(smileDetectedString.encode("UTF-8"))
    sock.sendall(posString.encode("UTF-8"))
    receivedData = sock.recv(1024).decode("UTF-8") #receiveing data in Byte fron C#, and converting it to String
    print(receivedData)

startPos = [0, 0, 0] #Vector3   x = 0, y = 0, z = 0
while True:
    successful_frame_read, frame = webcam.read()
    if not successful_frame_read:
        break
    frame_grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(frame_grayscale)


    for (x, y, w, h) in faces:

        cv2.rectangle(frame, (x, y), (x+w, y+h), (100, 200, 50), 4)

        the_face = frame[y:y+h, x:x+w]
        face_grayscale = cv2.cvtColor(the_face, cv2.COLOR_BGR2GRAY)
        smiles = smile_detector.detectMultiScale(face_grayscale, scaleFactor=1.7, minNeighbors=20)

        for (x_, y_, w_, h_) in smiles:
            cv2.rectangle(the_face, (x_, y_), (x_+w_, y_+h_), (50, 50, 200), 4)
            sendSmile()

    # cv2.imshow('Smile Detector', frame)
    # cv2.waitKey(1)

    # if not faces:
    #     print("empty")
    # else:
    #     print("full")
    # print("hi daniel")

    # # time.sleep(0.5) #sleep 0.5 sec
    # startPos[0] +=1 #increase x by one
    # posString = ','.join(map(str, startPos)) #Converting Vector3 to a string, example "0,0,0"
    # print(posString)

    # # sock.sendall(posString.encode("UTF-8")) #Converting string to Byte, and sending it to C#
    # testString = "Daniel ist cool"
    