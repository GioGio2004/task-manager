import speech_recognition as sr
import pyttsx3

from gmail import send_email
from reading_and_writing import Readeandwrite

# Initialize recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

task  = []

while True:
    try:
        with sr.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            print("Listening...")
            audio = recognizer.listen(mic)
            
            # Recognize speech using Google Web Speech API
            text = recognizer.recognize_google(audio)
            text = text.lower()
            
            print(f"Recognized: {text}")

            # adding text to a list and sending it as a task via gmail
            task.append(text)
            print(task)
            modyfied_task = ". ".join(task)
            print(modyfied_task)

            
            # Optional: Use text-to-speech to read back the recognized text
            engine.say(f"You said: {text}")
            engine.runAndWait()

            # recorecting text
            if text == "change last line":
                task.pop()
                task.pop()

            # quite the caht
            if text == "quit" or text == "quit chat" or text == "exit":
                send_email(modyfied_task)
                print("main has been send seccesfully")
                break
            

            def documenting_text():
                subject = "task"
                reader = Readeandwrite(subject, modyfied_task)
                reader.write()
                reader.read()

            if "write" in modyfied_task:
                documenting_text()

    except sr.UnknownValueError:
        print("Sorry, I did not understand that.")
        recognizer = sr.Recognizer()
        continue
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        break


# i need to add this

# subject = "task"
# content = "pytho classes and different things"

# from reading_and_writing import Readeandwrite

# reader = Readeandwrite(text, subject)
# reader.write()
