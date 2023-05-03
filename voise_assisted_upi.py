

class Voise_assisted_upi():
    def __init__(self, speech) -> None:
        self.speech = speech
    
    def make_payment(self):
        self.speech.Text2Speech("say amoount to be transferred")
        try:
            amount = self.speech.Speech2Text()
        except:
            self.speech.Text2Speech("restart the transaction")
        
        self.speech.Text2Speech("say phone number of the client")
        try:
            phno = self.speech.Speech2Text()
        except:
            self.speech.Text2Speech("restart the transaction")
        
        self.speech.Text2Speech("Payment initiating")
        self.speech.Text2Speech(f"{amount} rupees transferred to {phno}")


