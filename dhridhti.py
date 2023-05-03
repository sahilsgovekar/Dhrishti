from speech import Speech
from face_emotion_detection import Face_emotion
from object_detection import Object_detection
from voise_assisted_upi import Voise_assisted_upi

import cv2
import datetime

speech = Speech()
face_emotion = Face_emotion()
object_detection = Object_detection()
upi_transaction = Voise_assisted_upi(speech)

cam = cv2.VideoCapture(0)

# message = speech.Speech2Text()
# print(message)
# speech.Text2Speech(f"you said {message}")
# emotion = face_emotion.emotion_detect(cam)
# print(emotion)


# mes = object_detection.find_objects(cam)
# # print(mes)
# speech.Text2Speech(mes)

# upi_transaction.make_payment()

listening = False

while True:
    if not listening:
        userin = speech.Speech2Text()
        if userin == 'Drishti' or userin == 'Dhrishti':
            listening = True
            speech.Text2Speech("i an awake")
    
    else:
        userin = speech.Speech2Text()

        if userin == 'time':
            currentDT = datetime.datetime.now()
            speech.Text2Speech("The time is {} hours and {} minutes".format(currentDT.hour, currentDT.minute))






