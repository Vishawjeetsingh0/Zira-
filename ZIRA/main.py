import site
import webbrowser
import os
from re import search

import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import smtplib
import sys

from speech_recognition import Recognizer

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[1].id)


def speak(audio: object) -> object:
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("goog morning! sir")

    elif hour >= 12 and hour < 18:
        speak("good afternoon!sir")

    else:
        speak("good evening!sir!")

    speak("i am zeera how may i help you ")


def takeCommand():
    # it takes microphone input from the user and returns string out put

    r: Recognizer = sr.Recognizer()
    with sr.Microphone() as source:

        speak("I am Listening ")
        print("Listening... :)")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("recognizing....")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)

        speak("please say again ... :)")
        print("Please say again ... :)")
        return "None"
    return query


def sendemail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password-here')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()


if __name__ == '__main__':
    wishMe()
    while True:
        query = takeCommand().lower()

        # logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('searching wikipedia....')
            query = query.replace("wikipedia", " ")
            results = wikipedia.summary(query, sentences=2)
            speak('according to wikipedia')
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open youtube' in query:
            webbrowser.open("google.com")

        elif 'open youtube' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir = 'C:\music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir,the time is {strTime}")

        elif 'open code' in query:
            codepath = "C:\\Users\\vishw\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)

        elif 'open brave' in query:
            codepath = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
            os.startfile(codepath)
        elif 'open whatsapp' in query:
            codepath = "C:\\Windows.old\\Users\\vishw\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
            os.startfile(codepath)

        elif 'add numbers' in query:
            speak('Give me two numbers')
            print('Give me two numbers =')
            a = int(input())
            b = int(input())
            print(a + b)
            speak('your answer is printed above')

        elif 'subtract numbers' in query:

            speak('Give me two numbers')

            print('Give me two numbers =')
            a = int(input())
            b = int(input())
            print(a - b)
            speak('your answer is printed above')

        elif 'multiply numbers' in query:

            speak('Give me two numbers')

            print('Give me two numbers =')
            a = int(input())
            b = int(input())
            print(a * b)
            speak('your answer is printed above')

        elif 'devide numbers' in query:

            speak('Give me two numbers')

            print('Give me two numbers =')
            a = int(input())
            b = int(input())
            print(a / b)
            speak('your answer is printed above')

        elif 'email to vishwjeet' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "vishwjeetsingh7068@gmail.com"
                sendemail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("sorry !! its not man :(")

        elif 'search on google' in query:
            try:
                speak("what do you want to search?")
                content = takeCommand()
                to = "google.com"
                webbrowser.open(to)

                speak("here is your search")
            except Exception as e:
                print(e)
                speak("I am not able to search")






