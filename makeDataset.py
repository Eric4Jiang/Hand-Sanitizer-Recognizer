import numpy as np
import cv2
import os
import sys

# My paths
# /Users/eric/Dropbox/AttendanceCheck/DataSet/
# /Users/eric/opencv/data/haarcascades/haarcascade_frontalface_default.xml

if len(sys.argv) == 1:
    print ("Using default paths...")
    datasetPath = "/Users/eric/Dropbox/AttendanceCheck/DataSet/"
    haarcascadesPath = "/Users/eric/opencv/data/haarcascades/haarcascade_frontalface_default.xml"
elif len(sys.argv) != 3:
    print ("Arguments required: path/to/dataset path/to/haarcasecades_frontalface")
    sys.exit(0)
else:
    datasetPath = sys.argv[1]
    haarcascadesPath = sys.argv[2]

# Train face detection software
face_cascade = cv2.CascadeClassifier(haarcascadesPath)
# start camera
cap = cv2.VideoCapture(0)
# resize camera resolution
w = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
h = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# image specs
saveDir = datasetPath
ext = ".png"

imNum = 0
nameOfPerson = input("Enter name of person: ")

# make folder for new person
imFolder = saveDir + "/" + nameOfPerson
if not os.path.exists(imFolder):
    os.makedirs(imFolder)

# start taking images of students
while(1):
    #Capture frame-by-frame
    ret, frame = cap.read()
    # Convert to gray
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # press g to take picture of student
    if cv2.waitKey(30) == ord('g'):
        # name images
        imName = nameOfPerson + str(imNum)
        imPath = saveDir + "/" + nameOfPerson + "/" + imName + ext
        while os.path.isfile(imPath):
            imNum += 1
            imName = nameOfPerson + str(imNum)
            imPath = saveDir + "/" + nameOfPerson + "/" + imName + ext

        # Detect the face in the image
        faces = face_cascade.detectMultiScale(gray)
        if len(faces) > 0:
            cv2.imwrite(imPath, gray)
            cv2.imshow("Face", gray)
            cv2.waitKey(0)
            imNum += 1
    
    # display image being saved
    cv2.imshow("Image", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# release camera
cap.release()
cv2.destroyAllWindows()
