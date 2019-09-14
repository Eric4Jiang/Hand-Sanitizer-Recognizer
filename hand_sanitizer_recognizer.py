import cv2
import numpy as np
import sys
import os

# Change this to your PATH
sanitizer_cascade = cv2.CascadeClassifier("/Users/eric/Dropbox/PersonalProjects/CvProjects/hand_sanitizer_recognizer/data/cascade.xml")

# cap = cv2.VideoCapture(1)
cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)


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
    #x, y, w, h = rect
        #roi_gray = gray[y:y+h, x:x+w]
        # print ("Found sanitizer")
        # cv2.rectangle(resize, (x,y), (x+w, y+h), (255, 255, 0), 2)
        # cv2.imwrite("test/"+str(pic_num)+'.jpg', roi_gray)
        #print ("wrote ", pic_num)
        #pic_num += 1

    clustered_rects, _ = cv2.groupRectangles(rects, 1, 0)
    for rect in clustered_rects:
        x, y, w, h = rect
        cv2.rectangle(resize, (x,y), (x+w, y+h), (255, 255, 0), 2)
    
    cv2.imshow('frame', resize)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
