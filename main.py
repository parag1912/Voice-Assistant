import pyttsx3 as p
import speech_recognition as sr
import datetime
from News import *
from wiki import *
from weather import *
from YT_auto import *

engine = p.init()

# rate = engine.getProperty('rate')
engine.setProperty('rate',160)

voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)
# engine.setProperty('voice', voices[0].id)

def speak(text):
    engine.say(text)
    # engine.say("Hello sir , my name is jarvis , for just a rather very intelligent system")
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>0 and hour<12:
        return ("morning")
    elif hour>=12 and hour<16:
        return ("afternoon")
    else:
        return ("evening")

today_date  = datetime.datetime.now()

r = sr.Recognizer()

speak("Hello sir , I'm your voice assistant . How are you?")
# speak("Today is"+ today_date.strftime("%d") + "of" + today_date.strftime("%B")
#       + ",and its currently" + (today_date.strftime("%I")) + (today_date.strftime("%M")) + (today_date.strftime("%p")))
#
# speak("Temperature in mumbai is " + str(temp())+"degree celcius "+ "and with" + str(des()))

with sr.Microphone() as source:
    r.energy_threshold = 10000
    r.adjust_for_ambient_noise(source,1.2)
    print("listening")
    audio = r.listen(source)
    text = r.recognize_google(audio)
    print(text)

if "what" and "about" and "you" in text:
    speak("I am also having a good say sir")
    speak("What can I do for you")

with sr.Microphone() as source:
    r.energy_threshold = 10000
    r.adjust_for_ambient_noise(source,1.2)
    print("listening")
    audio = r.listen(source)
    text2 = r.recognize_google(audio)
    print(text2)

if "information"  in text2 :
    speak("sure sir , you need information related to which topic")

    with sr.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source, 1.2)
        print("listening")
        audio = r.listen(source)
        infor = r.recognize_google(audio)
    speak("searching {} im wikipedia".format(infor))
    print("searching {} im wikipedia".format(infor))
    assist = infow()
    assist.get_info(infor)

elif "play" and "video" in text2:
    speak("You want me to play which video?")
    with sr.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source, 1.2)
        print("listening")
        audio = r.listen(source)
        vid = r.recognize_google(audio)
        print("Playing {} on youtube".format(vid))
        speak("Playing {} on youtube".format(vid))

        assist = music()
        assist.play(vid)

elif "news" in text2:
    print("sure sir ,now i will read the news for you ")
    speak("sure sir ,now i will read the news for you ")

    arr = news()
    for i in range(len(arr)):
        print(arr[i])
        speak(arr[i])




