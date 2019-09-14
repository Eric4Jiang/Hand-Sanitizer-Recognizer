import cv2
import numpy as np
import sys
import os


if len(sys.argv) == 3:
    haarcascades_path = sys.argv[1]
    eye_cascade_path = sys.argv[2]
else:
    print ("Using default paths...")
    haarcascades_path = "/Users/eric/opencv/data/haarcascades/haarcascade_frontalface_default.xml"
    # haarcascades_path = "/Users/eric/opencv/data/lbpcascades/lbpcascade_frontalface.xml"
    eye_cascade_path = '/Users/eric/opencv/data/haarcascades/haarcascade_eye.xml'

# Change this to your PATH
sanitizer_cascade = cv2.CascadeClassifier("/Users/eric/Dropbox/PersonalProjects/CvProjects/hand_sanitizer_recognizer/data/cascade.xml")
face_cascade = cv2.CascadeClassifier(haarcascades_path)
eye_cascade = cv2.CascadeClassifier(eye_cascade_path)

# cap = cv2.VideoCapture(1)
cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

pic_num = 5000

#`for img in os.listdir("/Users/eric/Desktop/eye_cascade/test"):
#`    if img == ".DS_Store":
#`        continue
#`
#`    img = img[0:len(img)-4]
#`    num = int(img)
#`    pic_num = max(num, pic_num)
#`
#`print (pic_num)
#`pic_num += 1

while(cap.isOpened()):
    ret, frame = cap.read()
    
    resize = cv2.resize(frame, (640, 480))
    gray = cv2.cvtColor(resize, cv2.COLOR_BGR2GRAY)

    sanitizers = sanitizer_cascade.detectMultiScale(
        gray,
        scaleFactor=1.4, 
        minNeighbors=50, 
        minSize=(20,20), 
        maxSize=(300, 300),
    )
    
    rects = []
    # neg mining
    for rect in sanitizers:
        rects.append(rect)
        rects.append(rect)
        x, y, w, h = rect
        #roi_gray = gray[y:y+h, x:x+w]
        # print ("Found sanitizer")
        # cv2.rectangle(resize, (x,y), (x+w, y+h), (255, 255, 0), 2)
        # cv2.imwrite("test/"+str(pic_num)+'.jpg', roi_gray)
        #print ("wrote ", pic_num)
        #pic_num += 1

    clustered_rects, _ = cv2.groupRectangles(rects, 1, 0)
    for rect in clustered_rects:
    # for rect in rects:
        x, y, w, h = rect
        cv2.rectangle(resize, (x,y), (x+w, y+h), (255, 255, 0), 2)
    
    # first find faces and search for eyes on detected faces
    # will reduce processing time -> smaller window (face) to traverse eyes for
#    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
#    for (x, y, w, h) in faces:
#        # cv2.rectangle(frame, (x, y), (x + w, y + h), (255,0,0), 2)
#        roi_gray = gray[y:y+h, x:x+w]
#        roi_color = frame[y:y+h, x:x+w]
#        eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 10)
        #for (ex,ey,ew,eh) in eyes:
        #    cv2.rectangle(roi_color, (ex,ey), (ex+ew, ey+eh), (0,255,0), 2)

    # cv2.imwrite("test/"+str(pic_num)+'.jpg', frame)

    # pic_num += 1
    # print(pic_num)
    cv2.imshow('frame', resize)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
