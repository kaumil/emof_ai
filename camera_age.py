import cv2
from model_age import predict_emotion
import numpy as np

rgb = cv2.VideoCapture('a12.mpg')
facec = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
font = cv2.FONT_HERSHEY_SIMPLEX

def __get_data__():
    """
    __get_data__: Gets data from the VideoCapture object and classifies them
    to a face or no face. 
    
    returns: tuple (faces in image, frame read, grayscale frame)
    """
    _, fr = rgb.read()
    gray = cv2.cvtColor(fr, cv2.COLOR_BGR2GRAY)
    faces = facec.detectMultiScale(gray, 1.3, 3)
    
    return faces, fr, gray

def start_app():
    
    ix = 0
    count_frame=0
    while True:
        count_frame += 1

        faces, fr, gray_fr = __get_data__()

        if count_frame%5!=0:
            continue

        ix+=1
        for (x, y, w, h) in faces:
            fc = gray_fr[y:y+h, x:x+w]
            #print(fc)
            fc = cv2.cvtColor(fc,cv2.COLOR_GRAY2BGR)
            roi = cv2.resize(fc, (48, 48))
            #print(roi[np.newaxis, :].shape)
            pred = predict_emotion(roi[np.newaxis, :])
            
            cv2.putText(fr, pred, (x, y), font, 1, (255, 255, 0), 2)
            cv2.rectangle(fr,(x,y),(x+w,y+h),(255,0,0),2)

        if cv2.waitKey(1) == 27:
            break
        cv2.imshow('Filter', fr)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    print("called")
    start_app()
