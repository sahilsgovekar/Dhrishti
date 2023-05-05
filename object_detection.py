from face_emotion_detection import Face_emotion
from face_recognition import Face_recognition

import cv2
import cvlib as cv
from cvlib.object_detection import draw_bbox    
# from gtts import gTTS
# from playsound import playsound
import numpy as np
import time


class Object_detection():
    def __init__(self, speech) -> None:
        self.speech = speech
        self.face_emotion = Face_emotion()
        self.face_recognition = Face_recognition(speech)

    def find_objects(self, video):
        while True:
            found_items = []

            ret, frame = video.read()
            # time.sleep(100)
            bbox, label, conf = cv.detect_common_objects(frame)
            output_img = draw_bbox(frame, bbox, label, conf)

            cv2.imshow("object detection", output_img)

            for item in label:
                found_items.append(item)

            i = 0
            new_sentence = []
            for l in found_items:
                if i==0:
                    new_sentence.append(f"i found {l}")
                else:
                    new_sentence.append(f"and {l}")

                i += 1
                
            say_sentence = " ".join(new_sentence)

            # print(found_items)
            if 'person' in found_items:
                face_name = self.face_recognition.face_recog()
                emotion = self.face_emotion.emotion_detect()

                if face_name == 'no face':
                    say_sentence += f" and person is {emotion}"
                    self.speech.Text2Speech(f"unknown face detected, do you want to add it to database")
                    message = self.speech.Speech2Text()
                    if message == "yes":
                        self.face_recognition.face_taker()
                        self.face_recognition.face_trainer()

                else:
                    say_sentence += f" and {face_name} is is person and is {emotion}"

            # print(say_sentence)
            return say_sentence
    
    def getBrightness(self, cam):
        ret, frame = cam.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        avg = np.sum(frame)/(frame.shape[0]*frame.shape[1])
        avg=avg/255
        if(avg > 0.6):
            return ("Very bright", avg)
        if(avg > 0.4):
            return ("Bright", avg)
        if(avg>0.2):
            return ("Dim", avg)
        else:
            return ("Dark",avg)
        
    def object_find(self, cam):
        self.speech.Text2Speech("what object you want to find")
        obj_name = self.speech.Speech2Text()

        while True:
            found_items = []

            ret, frame = cam.read()
            # time.sleep(100)
            bbox, label, conf = cv.detect_common_objects(frame)
            output_img = draw_bbox(frame, bbox, label, conf)

            cv2.imshow("object detection", output_img)

            for item in label:
                found_items.append(item)
                if item == obj_name:
                    self.speech.Text2Speech("Item found, ahed of you")
                    break



# from speech import Speech
# s = Speech()
# o = Object_detection(s)
# cam = cv2.VideoCapture(0)
# print(o.find_objects(cam))


