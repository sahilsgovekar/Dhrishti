import cv2
from deepface import DeepFace

class Face_emotion():
    def __init__(self) -> None:
        self.face_cascade = cv2.CascadeClassifier("packages/haarcascade_frontalface_default.xml")

    def emotion_detect(self, video):
        while video.isOpened():
            _, frame = video.read()
            gray =  cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            face = self.face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

            for x, y, w, h in face:
                img = cv2.rectangle(frame, (x,y), (x+w, y+h), (0,0,255), 1)
                try:
                    analyze = DeepFace.analyze(frame, actions=['emotion'])
                    analyzed_emotion = analyze['dominant_emotion']
                    # print(analyzed_emotion)
                    return analyzed_emotion
                except:
                    # print("no face detected")
                    return "not showing any significant emotion"

            cv2.imshow('video', frame)
            key =  cv2.waitKey(1)
            if key==ord('q'):
                break



