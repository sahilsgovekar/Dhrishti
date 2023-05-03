from face_emotion_detection import Face_emotion

import cv2
import cvlib as cv
from cvlib.object_detection import draw_bbox    
from gtts import gTTS
from playsound import playsound
import time


class Object_detection():
    def __init__(self) -> None:
        self.face_emotion = Face_emotion()

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
                emotion = self.face_emotion.emotion_detect(video)

                say_sentence += f" and person is {emotion}"

            # print(say_sentence)
            return say_sentence