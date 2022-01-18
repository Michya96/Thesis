import speech_recognition as sr
import gtts
from playsound import playsound
from scraper import getTasks
from scraper import function_sound
import datetime
import wikipedia
# import os
import time



def speak(text):
    tts = gtts.gTTS(text, lang='en')
    tts.save('C:/Users/michj/Desktop/hello.mp3')
    function_sound()
    # os.remove('C:/Users/michj/Desktop/hello.mp3')

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
            while 'stop' not in statement:
                statement = takeCommand().lower()
                if 'tasks' in statement:
                    tasks = getTasks()
                    speak(f'You have {len(tasks)} tasks')
                    for i in tasks:
                        print(i)
                        speak(i)
                    break

                elif 'date' in statement:
                    date = datetime.datetime.now()
                    print(f'{date}')
                    break

                elif 'time' in statement:
                    time=datetime.datetime.now().strftime("%H:%M:%S")
                    print(f'It is {time} right now')
                    speak(f'It is {time} right now')
                    break

                elif 'what is' in statement:
                    statement = statement.replace("what is", "")
                    if statement == "":
                        break
                    results = wikipedia.summary(statement, sentences=3) 
                    speak("According to Wikipedia")
                    print(results)
                    speak(results)
                    break

        