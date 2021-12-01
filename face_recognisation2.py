import cv2,os
import csv
import numpy as np

def TakeImage():
    i=0
    if(i==0):
        cam=cv2.VideoCapture(0)
        face_classifier=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        sampleNum=0
        while(True):
            ret, img=cam.read()
            gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces=face_classifier.detectMultiScale(gray,1.3,3)

            for(x,y,w,h) in faces:
                cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
                sampleNum=sampleNum+1
                cv2.imwrite("TrainingImage\ "+str(sampleNum) + "sanu.jpg", gray[y:y+h,x:x+w])
                cv2.imshow('frame',img)

            if cv2.waitkey(100) & 0xFF == ord('q'):
                break
            elif sampleNum>60:
                break
        cam.release()
        cv2.destroyAllWindows()
    else:
        print("no")
TakeImage()
