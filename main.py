import ctypes
import datetime
import os
import time
import webbrowser
import winsound
import subprocess
import playsound
import pyautogui
import pyjokes
import pyttsx3
import pywhatkit as kit
import requests
import speech_recognition as sr
import wikipedia
import winshell as winshell
from bs4 import BeautifulSoup
from requests import get

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning")
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Sir mr.Behaan, the time is {strTime}")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Sir, the time is {strTime}")


    else:
        speak("Good Evening")
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Sir, the time is {strTime}")
    speak("i am jarvis sir, please tell me how can i help you")


def alarm(Timing):
    altime = str(datetime.datetime.now().strftime(Timing), "%I:%M %p")

    altime = altime[11:-3]
    print(altime)
    Horea1 = altime[:2]
    Horea1 = int(Horea1)
    Mirea1 = altime[3:5]
    Mirea1 = int(Mirea1)
    print(f"Done, alarm is set for {Timing}")

    while True:
        if Horea1 == datetime.datetime.now().hour:
            if Mirea1 == datetime.datetime.now().minute:
                print("alarm is running")
                winsound.PlaySound('abc', winsound.SND_LOOP)

            elif Mirea1 < datetime.datetime.now().minute:
                break


def takeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:

        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=0, phrase_time_limit=10)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}")

    except Exception as e:
        print(e)
        speak("Unable to Recognize your voice, say that again please.")
        return "None"
    return query


if __name__ == '__main__':
    wishme()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=4)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak("ok sir, but what should i search on Youtube\n")
            cm = takeCommand().lower()
            speak("ok sir, opening")
            webbrowser.open(f"{cm}")

        elif 'book my trip' in query:
            speak("ok sir,but where should i book")
            cm = takeCommand().lower()
            speak("ok sir, opening")
            webbrowser.open(f"{cm}")

        elif 'play music on youtube' in query or 'play song on youtube' in query:
            speak("ok sir, what should i search on youtube")
            cm = takeCommand().lower()
            speak("ok sir, opening")
            webbrowser.open(f"{cm}")

        elif 'i am sad' in query:
            speak("don't worry , i am playing you favorite song, please don't be sad")
            speak("opening")
            webbrowser.open("main dhoondne ko jamane me")



        elif 'open google' in query or 'open browser' in query or 'open chrome' in query:
            speak("ok sir, but what should i search ")
            cm = takeCommand().lower()
            speak("ok sir opening")
            webbrowser.open(f"{cm}")

        elif 'open stackoverflow' in query:
            speak("Here you go to Stack Over flow.Happy coding")
            webbrowser.open("stackoverflow.com")

        elif 'open github' in query:
            speak("here you go to github.happy coding")
            webbrowser.open("github.com")

        elif 'play music' in query:
            speak("Here you go with music")
            music_dir = "C:\\Users\\Public\\Music"
            songs = os.listdir(music_dir)
            for song in songs:
                if song.endswith('.mp3'):
                    os.startfile(os.path.join(music_dir, song))


        elif 'ip address' in query:
            ip = get('https://api.ipify.org').text
            print(ip)
            speak(f"your ip address is {ip}")


        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Sir")

        elif 'fine' in query or "happy" in query:
            speak("It's good to know that your fine")

        elif "change your name" in query:
            speak("What would you like to call me, Sir ")
            query = takeCommand()
            speak("Thanks for naming me")

        elif "hello" in query or "hii" in query:
            speak("hello sir, welcome")

        elif 'where are you' in query:
            speak("sir, i always stay on you computer.")

        elif "what's your name" in query or "What is your name" in query:
            print("i am jarvis, your personal assistant")
            speak("i am jarvis, your personal assistant")

        elif 'exit' in query:
            speak("Thanks for giving me your time")
            exit()

        elif "stop listening" in query:
            speak("ok sir, sorry")
            exit()

        elif "who made you" in query or "who created you" in query or "who descovered you" in query:
            speak("I have been created by Behaan.")

        elif 'joke' in query:
            speak(pyjokes.get_joke())

        elif "who i am" in query or "who am i" in query:
            speak("If you talk then, definitely your human.")

        elif "thank you" in query:
            speak("mention not sir,take care")

        elif "you know me" in query:
            speak("yes,i know you, if you talk then,definitely your human.")

        elif "why you came in this world" in query:
            speak("Thanks to Behan.further It's a secret")

        elif "who are you" in query:
            speak("I am your virtual assistant jarvis,created by Behaan")

        elif 'reason for you' in query:
            speak("I was created as a Minor project by Behaan")


        elif 'change background' in query or 'can you change the background' in query:
            ctypes.windll.user32.SystemParametersInfoW(20,
                                                       0,
                                                       "Location of wallpaper",
                                                       0)
            speak("Background changed successfully")


        elif 'shutdown system' in query:
            speak("Hold On a Sec ! Your system is on its way to shut down")
            subprocess.call('shutdown / p /f')


        elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
            speak("Recycle Bin Recycled")

        elif "restart the system" in query:
            subprocess.call(["shutdown", "/r"])

        elif 'shutdown the system' in query:
            speak("ok sir, system shut down")
            os.system("shutdown /s /t 5")

        elif "hibernate" in query or "sleep the system" in query:
            speak("Hibernating")
            subprocess.call("shutdown / h")

        elif "log off" in query or "sign out" in query:
            speak("Make sure all the application are closed before sign-out")
            time.sleep(5)
            subprocess.call(["shutdown", "/l"])

        elif "write a note" in query:
            speak("What should i write, sir")
            note = takeCommand()
            file = open('jarvis.txt', 'w')
            speak("Sir, Should i include date and time")
            sm = takeCommand()
            if 'yes' in sm or 'of course' in sm or 'yes why not' in sm:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)

        elif 'so note' in query:
            speak("Showing Notes")
            file = open("jarvis.txt", "r")
            print(file.read())
            speak(file.read(6))

        elif "hello jarvis" in query:
            wishme()
            speak("Jarvis in your service Mister")

        elif "good Morning" in query:
            speak("good morning sir")
            speak("How are you")

        elif 'good afternoon' in query:
            speak("good afternoon sir")
            speak("How are you")

        elif "good evening" in query:
            speak("good evening sir")
            speak("How are you")

        elif "good night" in query:
            speak("good night sir, Have a sweet dream")
            speak("sir, if you want to shut down your computer then give me a command, say shutdown the system")


        elif "will you be my gf" in query or "will you be my bf" in query:
            speak("I'm not sure about, may be you should give me some time")

        elif "you have gf" in query or "you have bf" in query:
            speak("I'm not sure about, may be you should give me some time")

        elif "i love you" in query:
            speak("It's hard to understand")

        elif "what is my father name" in query:
            speak("sir your father name is mr. .......")

        elif "what is my mother name" in query:
            speak("sir your mother  "
                  " name is ........")

        elif "what is my brother name" in query:
            speak("sir your father name is mr. john")

        elif "laugh" in query:
            speak("hahahahahaha")

        elif "you believe in God" in query:
            speak("may be, yes")

        elif "love me" in query:
            speak("sorry, i don't have heart,and emotions")

        elif "hate me" in query:
            speak("sir, what are you talking about,not at all")

        elif "instagram id" in query:
            speak("user name is john and password is .......")

        elif "facebook id" in query:
            speak("user name is john and password is .......")

        elif "vistara login id" in query:
            speak("login password is john@")

        elif "irctc" in query:
            speak("user id name is john and its password is 00000000 and its pin no is 0000")


        elif "temperature" in query or "weather" in query:
            search = "weather in haryana"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text, "html.parser")
            weather = data.find("div", class_="BNeawe").text
            print(weather)
            speak(f"current {search} is {weather}")

        elif "send whatsapp message" in query:
            kit.sendwhatmsg("sender no", "this is a jarvis", 2, 23)

        elif 'alarm' in query:
            speak("sir please tell me the time to set alarm.for example, set alarm to 5:30 am")
            tt = takeCommand()
            tt = tt.replace("set alarm to", "")  # 5:30 a.m
            tt = tt.replace(".", "")  # 5:30 am
            tt = tt.upper()  # 5:30 AM
            import MyAlarm

            MyAlarm.alarm(tt)

        elif 'volume up' in query:
            pyautogui.press("volumeup")

        elif 'volume down' in query:
            pyautogui.press("volumedown")

        elif 'volume mute' in query:
            pyautogui.press("volumemute")
