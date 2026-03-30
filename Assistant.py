import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import wikipedia
import requests
import time
import tkinter as tk

#  INIT 
engine = pyttsx3.init('sapi5')
engine.setProperty('rate', 170)
engine.setProperty('volume', 1.0)

# SPEAK 
def speak(text):
    output_text.insert(tk.END, "Assistant: " + text + "\n")
    output_text.see(tk.END)

    engine.stop()
    engine.say(text)
    engine.runAndWait()

# TAKE COMMAND 
def take_command():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        output_text.insert(tk.END, "Listening...\n")
        root.update()

        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio, language='en-IN')
        output_text.insert(tk.END, "You: " + command + "\n")
        return command.lower()
    except:
        speak("Sorry, I didn't catch that")
        return "none"
    

#  MAIN LOGIC  
def run_assistant():
    command = take_command()

    if command == "none":
        return

    if any(word in command for word in ["hello", "hi", "hey"]):
        speak("Hello Nawal, how can I help you?")

    elif "time" in command:
        speak(datetime.datetime.now().strftime("Time is %H:%M"))

    elif "date" in command:
        speak(str(datetime.date.today()))

    elif "google" in command:
        speak("Opening Google")
        webbrowser.open("https://google.com")

    elif "youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://youtube.com")

    elif "whatsapp" in command:
        speak("Opening WhatsApp")
        webbrowser.open("https://web.whatsapp.com")

    elif "search" in command:
        speak("What should I search?")
        query = take_command()
        webbrowser.open(f"https://google.com/search?q={query}")

    elif "wikipedia" in command:
        speak("What should I search?")
        query = take_command()
        try:
            result = wikipedia.summary(query, sentences=2)
            speak(result)
        except:
            speak("No results found")


    elif "exit" in command:
        speak("Goodbye Nawal")
        root.quit()

    else:
        speak("Sorry, I didn't understand")

#  UI 
root = tk.Tk()
root.title("Voice Assistant - Nawal")
root.geometry("500x400")

# Title
title = tk.Label(root, text="Voice Assistant", font=("Arial", 18))
title.pack(pady=10)

# Output box
output_text = tk.Text(root, height=15, width=60)
output_text.pack(pady=10)

# Button
start_btn = tk.Button(root, text="🎤 Start Listening", command=run_assistant, bg="green", fg="white")
start_btn.pack(pady=10)

# START 
speak("Voice assistant started")

root.mainloop()