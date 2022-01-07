import speech_recognition as sr
import pyttsx3
from scraper import getTasks
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
#from ecapture import ecapture as ec
import wolframalpha
import json
import requests

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice','voices[0].id')

def speak(text):
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio=r.listen(source)
        try:
            statement=r.recognize_google(audio,language='en-in')
            print(f"user said:{statement}\n")

        except Exception as e:
            # speak("Pardon me, please say that again")
            return "None"
        return statement

print("Loading your personal assistant PI")
speak("Loading your personal assistant pi")

if __name__=='__main__':


    while True:
        statement = takeCommand().lower()
        if statement=='hello pi' or statement=='hello by' or statement=='hello pie' :
            speak("What can i do for you?")
            while statement != 'stop':
                statement = takeCommand().lower()
                if statement=='read to-do list':
                    speak("Task number one is this and number two is that")
                    break
                elif statement=='something':
                    tasks = getTasks()
                    print(tasks)
                    for i in tasks:
                        print(i)
                    # speak(f'You have {len(tasks)} tasks')
                    speak(tasks)
                    break
