import openai
openai.api_key = "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"

class Audio_chatbot:
    def __init__(self, speech) -> None:
        self.speech = speech

    def have_conversation(self): 
        messages = []
        self.speech.Text2Speech(f"whome you want to have mentoring session with, for ex psychatrist, physotherepist etc")
        system_msg = self.speech.Speech2Text()
        messages.append({"role": "system", "content": system_msg})

        self.speech.Text2Speech("Your new assistant is ready!, go ahed with conversation")
        cond = ''
        while cond != "quit":
            message = self.speech.Speech2Text()
            if message == "quit":
                cond = "quit"
                break
            messages.append({"role": "user", "content": message})
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages)
            reply = response["choices"][0]["message"]["content"]
            messages.append({"role": "assistant", "content": reply})
            print("\n" + reply + "\n")
            self.speech.Text2Speech(reply)
# from speech import Speech
# s = Speech()
# a = Audio_chatbot(s)
# a.have_conversation()