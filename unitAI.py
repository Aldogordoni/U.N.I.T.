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
from tkinter import filedialog, Text
import tkinter.scrolledtext


def runAI():
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
            frame.config(state='normal')
            frame.insert('end', message)
            frame.yview('end')
            frame.config(state='disabled')
            #text = tk.Label(frame, text=message,fg="#33C518", bg="#1C2833")
            #text.pack()
            print(f">> {voice_data.lower()}") # print what user said
            return voice_data.lower()

    # get string and make a audio file to be played
    #def speak(audio_string):
    #    tts = gTTS(text=audio_string, lang='en') # text to speech(voice)
    #    r = random.randint(1,20000000)
    #    audio_file = 'audio' + str(r) + '.mp3'
    #    tts.save(audio_file) # save as mp3
    #    playsound.playsound(audio_file) # play the audio file
    #    print(f"U.N.I.T: {audio_string}") # print what app said
    #    os.remove(audio_file) # remove audio file

    def speak(audio):
        engine.say(audio)
        message = "U.N.I.T: " + audio +"\n"
        frame.config(state='normal')
        frame.insert('end', message)
        frame.yview('end')
        frame.config(state='disabled')
        #text = tk.Label(frame, text=message,fg="#33C518", bg="#1C2833")
        #text.pack()
        print(f"U.N.I.T: {audio}\n")
        engine.runAndWait()

    def respond(voice_data):
        # 1: greeting
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

        # 3: greeting
        if there_exists(["how are you","how are you doing"]):
            speak(f"I'm very well, thanks for asking {person_obj.name}")

        # 4: time
        if there_exists(["what's the time","tell me the time","what time is it"]):
            time = ctime().split(" ")[3].split(":")[0:2]
            if time[0] == "00":
                hours = '12'
            else:
                hours = time[0]
            minutes = time[1]
            time = f'{hours} {minutes}'
            speak(time)

        # 5: search google
        if there_exists(["search for"]) and 'youtube' not in voice_data:
            search_term = voice_data.split("for")[-1]
            url = f"https://google.com/search?q={search_term}"
            webbrowser.get().open(url)
            speak(f'Here is what I found for {search_term} on google')

        # 6: search youtube
        if there_exists(["youtube"]):
            search_term = voice_data.split("for")[-1]
            url = f"https://www.youtube.com/results?search_query={search_term}"
            webbrowser.get().open(url)
            speak(f'Here is what I found for {search_term} on youtube')

        # 7: get stock price
        if there_exists(["price of"]):
            search_term = voice_data.lower().split(" of ")[-1].strip() #strip removes whitespace after/before a term in string
            stocks = {
                "apple":"AAPL",
                "microsoft":"MSFT",
                "facebook":"FB",
                "tesla":"TSLA",
                "bitcoin":"BTC-USD"
            }
            try:
                stock = stocks[search_term]
                stock = yf.Ticker(stock)
                price = stock.info["regularMarketPrice"]

                speak(f'price of {search_term} is {price} {stock.info["currency"]} {person_obj.name}')
            except:
                speak('oops, something went wrong')

        #8: get weather
        if there_exists(["weather"]):
            search_term = voice_data.split("for")[-1]
            url = "https://www.google.com/search?sxsrf=ACYBGNSQwMLDByBwdVFIUCbQqya-ET7AAA%3A1578847393212&ei=oUwbXtbXDN-C4-EP-5u82AE&q=weather&oq=weather&gs_l=psy-ab.3..35i39i285i70i256j0i67l4j0i131i67j0i131j0i67l2j0.1630.4591..5475...1.2..2.322.1659.9j5j0j1......0....1..gws-wiz.....10..0i71j35i39j35i362i39._5eSPD47bv8&ved=0ahUKEwiWrJvwwP7mAhVfwTgGHfsNDxsQ4dUDCAs&uact=5"
            webbrowser.get().open(url)
            speak("Here is what the weather is looking like")

        #10 stone paper scisorrs
        if there_exists(["play rock paper scissor"]):
            voice_data = record_audio("choose among rock paper or scissor")
            moves=["Rock", "Paper", "Scissor"]
        
            cmove=random.choice(moves)
            pmove=voice_data
            
            speak("Rock")
            speak("Paper")
            speak("Scissor")
            speak("Shoot!")
            speak("The computer chose " + cmove)
            speak("You chose " + pmove)
            #engine_speak("hi")
            if pmove==cmove:
                speak("the match is draw")
            elif pmove== "rock" and cmove== "scissor":
                speak("Player wins")
            elif pmove== "rock" and cmove== "paper":
                speak("Computer wins")
            elif pmove== "paper" and cmove== "rock":
                speak("Player wins")
            elif pmove== "paper" and cmove== "scissor":
                speak("Computer wins")
            elif pmove== "scissor" and cmove== "paper":
                speak("Player wins")
            elif pmove== "scissor" and cmove== "rock":
                speak("Computer wins")

        #11 toss a coin
        if there_exists(["toss","flip","coin"]):
            moves=["head", "tails"]   
            cmove=random.choice(moves)
            speak("It's " + cmove)

        #12 calc
        if there_exists(["plus","minus","multiply","divide","power","+","-","*","/"]):
            opr = voice_data.split()[1]

            if opr == '+':
                speak(int(voice_data.split()[0]) + int(voice_data.split()[2]))
            elif opr == '-':
                speak(int(voice_data.split()[0]) - int(voice_data.split()[2]))
            elif opr == 'multiply' or 'x':
                speak(int(voice_data.split()[0]) * int(voice_data.split()[2]))
            elif opr == 'divide':
                speak(int(voice_data.split()[0]) / int(voice_data.split()[2]))
            elif opr == 'power':
                speak(int(voice_data.split()[0]) ** int(voice_data.split()[2]))
            else:
                speak("Wrong Operator")
            
        #13 screenshot
        if there_exists(["capture","my screen","screenshot"]):
            myScreenshot = pyautogui.screenshot()
            r = random.randint(1,20000000)
            ssName = 'screenshot' + str(r) + '.png'
            myScreenshot.save('C:/Users/pc/Desktop/U.N.I.T. Project/screenshots/'+ssName)
        
        
        #14 to search wikipedia for definition
        if there_exists(["definition of"]):
            definition=record_audio("what do you need the definition of")
            url=urllib.request.urlopen('https://en.wikipedia.org/wiki/'+definition)
            soup=bs.BeautifulSoup(url,'lxml')
            definitions=[]
            for paragraph in soup.find_all('p'):
                definitions.append(str(paragraph.text))
            if definitions:
                if definitions[0]:
                    speak('im sorry i could not find that definition, please try a web search')
                elif definitions[1]:
                    speak('here is what i found '+definitions[1])
                else:
                    speak ('Here is what i found '+definitions[2])
            else:
                    speak("im sorry i could not find the definition for "+definition)

        if there_exists(["what is my exact location"]):
            url = "https://www.google.com/maps/search/Where+am+I+?/"
            webbrowser.get().open(url)
            speak("You must be somewhere near here, as per Google maps")

        if there_exists(["exit", "quit", "goodbye"]):
            speak("going offline")
            exit()
            


    time.sleep(1)

    person_obj = person()
    unit_obj = unit()


    #while(1):
    voice_data = record_audio() # get the voice input 
    respond(voice_data) # respond


root = tk.Tk()

canvas = tk.Canvas(root, height= 400, width=600, bg="#1A6BBC")
canvas.pack()

frame = tkinter.scrolledtext.ScrolledText(root, bg="#1C2833")
frame.place(relwidth=0.8, relheight=0.4, relx=0.1, rely=0.1)
frame.config(state='disabled')

buttonFrame = tk.Frame(bg="#1C2833")
buttonFrame.place(relwidth=0.5, relheight=0.1, relx=0.252, rely=0.7)

runProgram = tk.Button(buttonFrame, text="Talk to U.N.I.T", padx=10, pady = 5, fg = "#33C518", bg = "#1C2833", command = runAI)
runProgram.pack()


root.mainloop()
