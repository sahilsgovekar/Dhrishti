import speech_recognition as sr
import pyttsx3

class Speech:
    def __init__(self) -> None:
        # initilise speech to text
        self.s2t = sr.Recognizer()

        # initilise text to speech 
        self.t2s = pyttsx3.init()
        self.voice = self.t2s.getProperty('voices')
        self.t2s.setProperty('voice', self.voice[1].id)

    def Speech2Text(self) -> str:
        with sr.Microphone() as source:
            self.s2t.adjust_for_ambient_noise(source)
            print("mic reaady")

            listned_text = self.s2t.listen(source, phrase_time_limit=3)

            try:
                converted_text = self.s2t.recognize_google(listned_text)
                # print(converted_text)
                return converted_text.lower()
            except:
                # print("error")
                return "error in recognition"
            
    def Text2Speech(self, message):
        self.t2s.say(message)
        self.t2s.runAndWait()
        return
