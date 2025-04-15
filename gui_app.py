import tkinter as tk
from tkinter import scrolledtext
from nlp_processor import extract_entities, analyze_sentiment, recognize_intent
from datetime import datetime
import webbrowser
import pyjokes

class JarvisApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Jarvis - AI Assistant")

        # Input area
        self.entry = tk.Entry(root, width=50, font=("Arial", 14))
        self.entry.pack(pady=10)
        self.entry.bind("<Return>", self.process_input)

        # Output area
        self.output = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=20, font=("Arial", 12))
        self.output.pack()

        # Button
        self.send_button = tk.Button(root, text="Ask Jarvis", command=self.process_input)
        self.send_button.pack(pady=10)

    def respond(self, message):
        self.output.insert(tk.END, f"Jarvis: {message}\n")
        self.output.see(tk.END)

    def process_input(self, event=None):
        user_input = self.entry.get()
        self.output.insert(tk.END, f"You: {user_input}\n")
        self.entry.delete(0, tk.END)

        intent = recognize_intent(user_input)
        entities = extract_entities(user_input)
        sentiment = analyze_sentiment(user_input)

        if intent == "get_time":
            self.respond(f"The current time is {datetime.now().strftime('%H:%M:%S')}")
        elif intent == "get_date":
            self.respond(f"Today's date is {datetime.now().strftime('%d/%m/%Y')}")
        elif intent == "search_google":
            self.respond("Opening Google...")
            webbrowser.open("https://www.google.com")
        elif intent == "tell_joke":
            joke = pyjokes.get_joke()
            self.respond(joke)
        else:
            self.respond("Sorry, I didn't understand that.")

        if entities:
            self.respond(f"Entities detected: {entities}")
        if sentiment != 0:
            self.respond(f"Sentiment Score: {sentiment:.2f}")

if __name__ == "__main__":
    root = tk.Tk()
    app = JarvisApp(root)
    root.mainloop()
