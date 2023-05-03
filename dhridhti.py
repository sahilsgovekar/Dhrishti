from speech import Speech
from face_emotion_detection import Face_emotion
from object_detection import Object_detection

import cv2


speech = Speech()
face_emotion = Face_emotion()
object_detection = Object_detection()

cam = cv2.VideoCapture(0)

# message = speech.Speech2Text()
# print(message)
# speech.Text2Speech(f"you said {message}")
# emotion = face_emotion.emotion_detect(cam)
# print(emotion)


mes = object_detection.find_objects(cam)
# print(mes)
speech.Text2Speech(mes)
