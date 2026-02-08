import pyttsx3

def text_to_audio(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 160)   # speech speed
    engine.setProperty('volume', 1.0)

    engine.say(text)
    engine.runAndWait()

    return "Audio generated successfully 🔊"
