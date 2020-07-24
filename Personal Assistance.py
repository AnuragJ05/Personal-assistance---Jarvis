import speech_recognition as sr
import datetime
import time
from time import ctime
import webbrowser
import pyttsx3
from ecapture import ecapture as ec
import wikipedia
import random
from gtts import gTTS
import os
import playsound

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

""""
def speak(audio_string):
    tts= gTTS(text=audio_string, lang='en')
    r= random.randint(1,1000000)
    audio_file = 'audio-'+ str(r) +'.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)
    """
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("Hey this is your personal assistant. Please tell me how may I help you")

def record(ask = False):
    r = sr.Recognizer()
    voice_data = None
    with sr.Microphone() as source :
        print("Listening...")
        r.pause_threshold = 1
        if ask:
            speak(ask)
        audio = r.listen(source)
        try:
            voice_data = r.recognize_google(audio, language='en-in')

        except Exception as e:
            print('Sorry, I did not get that. Speak again')
            voice_data = ''
        return voice_data
def play_game():
    choices = ['stone', 'paper', 'scissor']
    speak('Lets play game.........Now, ')
    you_choose = record('Choose from stone, paper and scissor...... ')
    jarvis_choose = random.choice(choices)
    while you_choose not in choices:
        speak('Say again')
        you_choose = record('Choose from stone, paper and scissor.... ')
    speak('Jarvis choose ' + jarvis_choose)
    speak('you choose ' + you_choose)

    if you_choose == choices[0] and jarvis_choose == choices[2]:
        speak('You win, Jarvis loss')
    elif you_choose == choices[1] and jarvis_choose == choices[0]:
        speak('You win, Jarvis loss')
    elif you_choose == choices[2] and jarvis_choose == choices[1]:
        speak('You win, Jarvis loss')
    elif jarvis_choose == choices[0] and you_choose == choices[2]:
        speak('Jarvis win, you loss')
    elif jarvis_choose == choices[1] and you_choose == choices[0]:
        speak('Jarvis win, you loss')
    elif jarvis_choose == choices[2] and you_choose == choices[1]:
        speak('Jarvis win, you loss')
    elif jarvis_choose == you_choose:
        speak('The match is draw')


def respond(voice_data):
    print("Recognizing...")

    if 'what is your name' in voice_data:
        speak('My name is Jarvis')

    elif "how are you" in voice_data or "how are you doing" in voice_data:
        speak("I'm Fine, thanks for asking ")

    elif 'time' in voice_data:
        speak(ctime())

    elif "open google" in voice_data:
        ask = record('What do you want to search')
        url= 'https://google.com/search?q=' + ask
        webbrowser.get().open(url)
        speak('Here is what I found for '+ ask)

    elif "open youtube" in voice_data:
        ask = record('What do you want to watch')
        url= "https://www.youtube.com/results?search_query=" + ask
        webbrowser.get().open(url)
        speak('Here is what I found for '+ ask)

    elif "wikipedia" in voice_data:
        ask = record('What do you want to know')
        results = wikipedia.summary(ask,sentences=5,)
        speak('Here is what I found  ')
        speak("According to Wikipedia  ")
        speak(results)

    elif "game" in voice_data:
        f=True
        while f:
            play_game()
            ask = record('Do you want to play again ..??')
            if 'yes' in ask:
                play_game()
            else:
                f=False
                break

    elif 'find location' in voice_data:
        ask = record('What is the location you want to search')
        url= 'https://google.nl/maps/place/' + ask + '/&amp;'
        webbrowser.get().open(url)
        speak('Here is the location of '+ ask)

    elif "camera" in voice_data or "take a photo" in voice_data:
        ec.capture(0, "Jarvis Camera ", "img.jpg")

    elif "music" in voice_data or "song" in voice_data:
        ask = record('What do you want to hear')
        url = 'https://gaana.com/song/' + ask
        webbrowser.get().open(url)
        speak('Here is your song ' + ask)

    elif 'goodbye' in voice_data:
        speak('Thank you and have a nice day')
        exit()

    else :
        speak('Speak Again')


if __name__=="__main__":
    time.sleep(0.1)
    wishMe()
    while 1:
        voice_data = record().lower()
        if voice_data != '' :
            respond(voice_data)