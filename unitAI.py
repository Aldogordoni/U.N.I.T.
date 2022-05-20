from tkinter.ttk import LabelFrame
import speech_recognition as sr # recognise speech
#import playsound # to play an audio file
from gtts import gTTS # google text to speech
import random
from time import ctime # get time details
import webbrowser # open browser
import yfinance as yf # to fetch financial data
import pyttsx3
import ssl
import certifi
import time
import os # to remove created audio files
import bs4 as bs
import pyautogui
import urllib.request
import tkinter as tk
from tkinter import *
import tkinter.scrolledtext



def runAI():
    runProgram.destroy
    engine = pyttsx3.init(driverName = 'sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 125)

    class person:
        name = ''
        def setName(self, name):
            self.name = name

    
    
    class unit:
        name = 'UNIT'
        def setName(self, name):
            self.name = name

    def there_exists(terms):
        for term in terms:
            if term in voice_data:
                return True

    r = sr.Recognizer() # initialise a recogniser
    # listen for audio and convert it to text:
    def record_audio(ask=False):
        with sr.Microphone() as source: # microphone as source
            if ask:
                speak(ask)
            audio = r.listen(source)  # listen for the audio via source
            voice_data = ''
            try:
                voice_data = r.recognize_google(audio)  # convert audio to text
            except sr.UnknownValueError: # error: recognizer does not understand
                speak('I did not get that')
            except sr.RequestError:
                speak('Sorry, the service is down') # error: recognizer is not connected
            message = (f">> {voice_data.lower()} \n")
            #text = tk.Label(frame, text=message,fg="#e8e8e8",bg="#141414")
            #text.grid(row=0,column=0)
            print(f">> {voice_data.lower()}") # print what user said
            return voice_data.lower()

    def speak(audio):
        engine.say(audio)
        message = audio +"\n"
        text = tk.Label(frame, text=message,fg="#e8e8e8",bg="#141414")
        text.grid(row=0,column=0)
        #text = tk.Label(frame, text=message,fg="#33C518", bg="#1C2833")
        #text.pack()
        print(f"U.N.I.T: {audio}\n")
        engine.runAndWait()

    def respond(voice_data):
        # greeting
        if there_exists(['hey','hi','hello']):
            greetings = [f"hey, how can I help you {person_obj.name}", f"hey, what's up? {person_obj.name}", f"I'm listening {person_obj.name}", f"how can I help you? {person_obj.name}", f"hello {person_obj.name}"]
            greet = greetings[random.randint(0,len(greetings)-1)]
            speak(greet)

        # 2: name
        if there_exists(["what is your name","what's your name","tell me your name"]):
            if person_obj.name:
                speak(f"my name is {unit_obj.name}, {person_obj.name}")
            else:
                speak("my name is UNIT, pretty cool right? What's yours?")

        if there_exists(["my name is"]):
            person_name = voice_data.split("is")[-1].strip()
            speak(f"okay, i will remember that {person_name}")
            person_obj.setName(person_name) # remember name in person object

        # greeting
        if there_exists(["how are you","how are you doing"]):
            speak(f"I'm very well, thanks for asking {person_obj.name}")

        # time
        if there_exists(["what's the time","tell me the time","what time is it"]):
            time = ctime().split(" ")[3].split(":")[0:2]
            if time[0] == "00":
                hours = '12'
            else:
                hours = time[0]
            minutes = time[1]
            time = f'{hours} {minutes}'
            speak("it's "+time)

        # toss a coin
        if there_exists(["toss","flip","coin"]):
            moves=["head", "tails"]   
            cmove=random.choice(moves)
            speak("It's " + cmove)

        # exit
        if there_exists(["exit", "quit", "goodbye"]):
            speak("going offline")
            exit()
            


    time.sleep(0.5)

    person_obj = person()
    print(person_obj.name + "---")
    unit_obj = unit()


    #while(1):
    voice_data = record_audio() # get the voice input 
    respond(voice_data) # respond

    


root = tk.Tk()

canvas = tk.Canvas(root, height= 400, width=600, bg="#141414")
canvas.pack()

frame = LabelFrame(canvas, padx=100, pady=100, bg="#141414")
frame.pack()

runProgram = tk.Button(frame, text="Talk to U.N.I.T", padx=10, pady = 5, fg = "#e8e8e8", bg = "#1C2833", command = runAI)
runProgram.grid(row=1,column=0,pady=50)


root.mainloop()

