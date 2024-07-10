import speech_recognition as s
import pyttsx3

sr = s.Recognizer()

print("I am your script and I am listening to you...")

try:
    with s.Microphone() as m:
        audio = sr.listen(m)
        query = sr.recognize_google(audio, language="en-IN")
        print(query)
except Exception as e:
    print(f" Error : {str(e)}")
