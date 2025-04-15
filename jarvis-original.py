import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
import wikipedia
import smtplib
import os
import pyautogui
import psutil
import pyjokes

engine = pyttsx3.init()

engine.say("Hello, how are you?")
engine.runAndWait()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"The current time is {Time}")

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    day = int(datetime.datetime.now().day)
    speak(f"The current date is {day}/{month}/{year}")

def wishme():
    speak("Hello, how are you?! This is Jarvis AI Assistant")
    time()
    date()

    hour = int(datetime.datetime.now().hour)
    
    if hour >= 6 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}\n")
        return query
    except Exception as e:
        print("Say that again")
        return ""

def sendEmail(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("your_email@gmail.com", "your_password")
    server.sendmail("your_email@gmail.com", to, content)
    server.close()

def screenshot():
    img = pyautogui.screenshot()
    img.save("screenshot.png")

def cpu():
    cpu_usage = psutil.cpu_percent(interval=1)
    speak(f"The CPU usage is {cpu_usage}%")
    battery = psutil.sensors_battery()
    speak(f"The battery is {battery.percent}%")

def jokes():
    speak(pyjokes.get_joke())
    print(pyjokes.get_joke())

if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()
        
        if 'time' in query:
            time()

        elif 'date' in query:
            date()

        elif 'open youtube' in query:
            speak("Opening YouTube...")
            webbrowser.open("https://www.youtube.com")

        elif 'open google' in query:
            speak("Opening Google...")
            webbrowser.open("https://www.google.com")

        elif 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(result)
            speak(result)

        elif 'send email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "recipient_email@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry, I am not able to send this email")

        elif 'search in google' in query:
            speak("What should I search for?")
            cm = takeCommand().lower()
            query = query.replace("search in google", "")
            webbrowser.open(f"https://www.google.com/search?q={query}")

        elif 'remember that' in query:
            speak("What should I remember?")
            data = takeCommand()
            with open("memory.txt", "a") as f:
                f.write(data + "\n")
            speak("I will remember that")

        elif 'do you know anything' in query:
            remember = open("memory.txt", "r")
            speak("You know that" + remember.read())

        elif 'joke' in query:
            jokes()

        elif 'screenshot' in query:
            speak("Taking screenshot...")
            screenshot()
            speak("Screenshot has been saved")

        elif 'cpu' in query:
            cpu()

        elif 'offline' in query:
            speak("Shutting down...")
            exit()