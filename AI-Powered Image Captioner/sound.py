import pyttsx3

def say(caption):
    engine = pyttsx3.init()
    engine.say(caption)
    engine.runAndWait()