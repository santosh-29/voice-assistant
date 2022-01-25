import os
import sys
import random
import webbrowser
import datetime
import subprocess
import playsound
import wolframalpha
import speech_recognition as sr
from gtts import gTTS

r = sr.Recognizer()
def record_audio():
    with sr.Microphone() as source:
        print('Speak now..')
        audio = r.listen(source,phrase_time_limit=5)
        try:
            text = r.recognize_google(audio)
            print('You:', text)
            if text.lower()=="exit":
                sys.exit()
            return text.lower()
        except sr.UnknownValueError:
            print('Assistant: Sorry,can you please speak again')
            speak('Sorry,Can you please speak again')
            t=record_audio()
            return t
        except sr.RequestError:
            print('Sorry,the service is down.')
            speak('Sorry,the service is down.')

def speak(text_data):
    num=random.random()
    speech=gTTS(text_data,lang='en',slow=False)
    print('Assistant:\tspeaking....')
    file=str(num)+'.mp3'
    speech.save(file)
    playsound.playsound(file,True)
    os.remove(file)

def search(find):

    if "maps" in find:
        speak("which place do you want me to search?")
        text = ''
        text = text + str(record_audio())
        speak("Opening Google Maps\nsearching Location")
        s = text.split()
        webbrowser.open("https://www.google.com/maps/place/" + '+'.join(s))
    elif "google" in find:
        speak("what do you want me to search?")
        text=''
        text=text+str(record_audio())
        speak("Opening Google Chrome")
        webbrowser.open("http://www.google.com/search?q="+text)
    elif "youTube" in find:
        speak("what do you want me to search?")
        text=''
        text=text+str(record_audio())
        speak("Opening Youtube\nsearching video")
        s=text.split()
        webbrowser.open("https://www.youtube.com/results?search_query="+ '+'.join(s))
    elif "wikipedia" in find:
        speak("what do you want me to search?")
        text = ''
        text = text + str(record_audio())
        speak("Opening Wikipedia")
        s = text.split()
        webbrowser.open("https://en.wikipedia.org/wiki/"+'_'.join(s))
    elif "amazon" in find:
        speak("Opening Amazon")
        webbrowser.open("https://www.amazon.in")
    elif "flipkart" in find:
        speak("what do you want me to search?")
        text = ''
        text = text + str(record_audio())
        speak("Opening Flipkart")
        s = text.split()
        webbrowser.open("https://www.flipkart.com/search?q="+'_'.join(s))
    elif "facebook" in find:
        speak("Opening Facebook")
        webbrowser.open("https://www.facebook.com/")
    elif "insta" in find:
        speak("Opening instagram")
        webbrowser.open("https://www.instagram.com/")
    elif "tiktok" in find:
        speak("Sorry I hate Tiktok but for your purpose opening tiktok")
        webbrowser.open("https://www.tiktok.com/trending/?lang=en")
    else:
        speak("Here is what I found on web")
        webbrowser.open("http://www.google.com/search?q="+find)

def open_application(a_name):
    apps={"powerpoint":"Microsoft PowerPoint 2010","word":"Microsoft Word 2010","excel":"Microsoft Excel 2010","outlook":"Microsoft Outlook 2010"}
    var=0
    for i in apps:
        if i in  a_name:
            os.startfile("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office\\"+apps[i])
            var=1
    if var==1:
        pass
    elif "calculator" in a_name:
        speak("Opening calculator")
        subprocess.Popen("C:\\Windows\\System32\\calc.exe")
    elif "notepad" in a_name:
        speak("Opening Notepad")
        subprocess.Popen("C:\\Windows\\System32\\notepad.exe")
    elif "wordpad" in a_name:
        speak("Opening Wordpad")
        subprocess.Popen("C:\\Windows\\System32\\write.exe")

    else:
        print("Sorry,couldn't open file or file doesn't exist")
        speak("Sorry,couldn't open file or file doesn't exist")

def action():
    #speak("What's your name buddy?")
    #name=record_audio()
    speak("How can I help you?")
    task=record_audio()
    work=task.lower().split()
    actions=["maps","google","youtube","wikipedia","amazon","flipkart","facebook","insta","tiktok","website" ]
    flag=0
    for i in actions:
        if ("open" in work) and (i in work):
            search(' '.join(work))
            flag=1
    if flag==1:
        pass
    elif "search" in task:
        search(task)
    elif "open" in task:
        open_application(task.lower())
    elif ("time" in task) and ("what" in task):
        time_now=datetime.now().time()
        print("The time is",time_now)
        speak("The time is"+str(time_now))
    elif("day" in task) and ("today" in task):
        tday=datetime.datetime.today()
        print("Today is "+str(tday.day)+" "+str(tday.month)+" "+str(tday.year))
        speak("Today is "+str(tday.day)+" "+str(tday.month)+" "+str(tday.year))
    elif ("made you" in task) or ("programmed you" in task) or ("prepared you" in task):
        speak("I was prepared by Santosh Kumar")
    elif("who are you" in task):
        speak("Python bot is my name.Helping you is my game.")
    elif("what" in task) and ("you do" in task):
        speak("I can search web,open popular websites,open some applications of your windows device,do your tasks")
    elif("calculate" in task):
        ind=task.lower().split().index("calculate")
        cal=task[ind+1:]
        if len(cal)<2:
            cal=record_audio()
        client=wolframalpha.Client('TP44EV-WGGY4A5YAG')
        res=client.query(cal)
        speak((next(res.results).text))
        print((next(res.results).text))

    else:
        try:
            client = wolframalpha.Client('TP44EV-WGGY4A5YAG')
            res = client.query(task)
            speak((next(res.results).text))
            print((next(res.results).text))
        except:
            pass
        finally:
            speak("Here is what I found on web")
            webbrowser.open("http://www.google.com/search?q="+task)
    print("\nWake me up if you need any help")

def wake_word():
    wake_word="computer"
    print('\nSay something...', end='')
    while True:
        print('\nSpeak...', end='')
        with sr.Microphone() as source:
            audio = r.listen(source, phrase_time_limit=5)
            try:
                text = r.recognize_google(audio)
                print('\nYou:', text)
            except sr.UnknownValueError:
                print('.',end='')
                text=""
            except sr.RequestError:
                print('\nSorry,the service is down.')
                speak('Sorry,the service is down.')
            if text.count(wake_word) > 0:
                speak("Hey!\nI'm there")
                print("\nAssistant: Hey! I'm there")
                action()
            if (text=="exit"):
                break
wake_word()
