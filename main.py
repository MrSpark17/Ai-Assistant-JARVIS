# main.py
from core.voice import speak, take_command
from core.system import get_time, get_date, get_battery, take_screenshot
from core.web import search_google, play_youtube, get_wikipedia_summary
from core.memory import remember, recall
from core.utils import greet

def run_jarvis():
    speak("Hello, I am Jarvis!")
    speak(greet())

    while True:
        query = take_command()
        if not query:
            continue

        if "time" in query:
            speak(f"The time is {get_time()}")
        elif "date" in query:
            speak(f"Today's date is {get_date()}")
        elif "battery" in query:
            speak(get_battery())
        elif "screenshot" in query:
            speak(take_screenshot())
        elif "google" in query:
            speak(search_google(query.replace("google", "").strip()))
        elif "youtube" in query:
            speak(play_youtube(query.replace("youtube", "").strip()))
        elif "wikipedia" in query:
            topic = query.replace("wikipedia", "").strip()
            speak(get_wikipedia_summary(topic))
        elif "remember" in query:
            note = query.replace("remember", "").strip()
            speak(remember(note))
        elif "do you remember" in query or "recall" in query:
            speak(recall())
        elif "exit" in query or "quit" in query:
            speak("Goodbye!")
            break
        else:
            speak("I did not understand that command.")

if __name__ == "__main__":
    run_jarvis()