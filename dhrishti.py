from speech import Speech
from face_emotion_detection import Face_emotion
from object_detection import Object_detection
from voise_assisted_upi import Voise_assisted_upi
from face_recognition import Face_recognition
from audio_chatbot import Audio_chatbot
import weather

import cv2
import datetime

speech = Speech()
face_emotion = Face_emotion()
object_detection = Object_detection(speech)
upi_transaction = Voise_assisted_upi(speech)
face_recognition = Face_recognition(speech)
audio_chatbot = Audio_chatbot(speech)

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
        if userin == 'drishti' or userin == 'dhrishti' or 'd':
            listening = True
            speech.Text2Speech("i an awake")
    
    else:
        userin = speech.Speech2Text()

        if userin == "object detect" or userin == "o":
            mes = object_detection.find_objects(cam)
            speech.Text2Speech(mes)
        
        elif userin == 'object find' or userin == 'f':
            object_detection.object_find(cam)

        elif userin == 'time' or userin == 't':
            currentDT = datetime.datetime.now()
            speech.Text2Speech("The time is {} hours and {} minutes".format(currentDT.hour, currentDT.minute))
        
        elif userin == 'brightness' or userin == 'b':
            brightness = object_detection.getBrightness(cam=cam)
            speech.Text2Speech(f"It is {brightness} here")

        elif userin == 'chatbot' or userin == 'c':
            audio_chatbot.have_conversation()
        
        elif userin == 'pay' or userin == 'p':
            upi_transaction.make_payment()

        elif userin == 'weather' or userin == 'w':
            weather_report = weather.weather()
            speech.Text2Speech(weather_report)






