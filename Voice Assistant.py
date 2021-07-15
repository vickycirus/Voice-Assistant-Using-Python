from googletrans import Translator  
import pyttsx3#output voice
import speech_recognition as sr #speech recognition
import datetime
import wikipedia 
import webbrowser #to open webpage
import os
import smtplib#mail
import time
import random
from PyDictionary import PyDictionary#to find meaning
dictionary=PyDictionary()
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
i=0
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  
    if(i==0):
        speak("I am Cirus. Please tell me how may I help you")    
    else:
        speak("I am Scarlett. Please tell me how may I help you")       
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('vikramchiluka18@gmail.com', 'glbyexertfqtsfoq')
    server.sendmail('vikramchiluka18@gmail.com', to, content)
    server.close()
def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak("what do you want to search in wikipedia")
            query2 = takeCommand().lower()
            speak('Searching Wikipedia...')
            try:
                results = wikipedia.summary(query2, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            except:
                speak("error while searching")    
        elif 'introduction' in query:
            speak("I can change my voice")
            print("I can change my voice if you say change voice")
            speak("I can search anything in wikipedia")
            print("I can search anything in wikipedia if you say wikipedia")
            speak("I can send mail")
            print("I can send mail if you say mail")
            speak("i can translate any language to english")
            print("i can translate any language to english if you say translate")
            speak("i can say any meaning ")
            print("i can say any meaning if you say meaning")
            speak("i can open your gmail. youtube. google")
            print("i can open your gmail if you say open inbox")
            print("say open google to open google")
            print("say open youtube to open youtube")
            speak("i can play a song")
            print("i can play a song if you say play song")
            speak("i can say time ")
            print("i can say time if you say time")
            speak("say quit to stop")
        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com/")
            time.sleep(10)
        elif 'open google' in query:
            webbrowser.open("https://www.google.com/")
            time.sleep(10)
        elif 'open inbox' in query:
            webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
            time.sleep(20)
        elif ('time' or'what is the time' )  in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
            time.sleep(4)
        elif 'quit'  in query:
            speak("Thank you")
            quit()
        elif 'play song' in query:
            music_dir='F:\\newsongs'
            songs = os.listdir(music_dir)
            speak("enjoy the song  thank you!!")
            print(songs)    
            k=(random.randrange(0,len(songs)))
            os.startfile(os.path.join(music_dir, songs[k]))  
            time.sleep(30)
            quit()
        elif 'mail' in query:
            try:
                speak("enter email id")
                print("enter email id:")
                email_id=input()
                to=email_id
                speak("What should I say?")
                content = takeCommand()   
                sendEmail(to, content)
                speak("Email has been sent successfully!")
            except Exception as e:
                print(e)
                speak("Sorry  I am not able to send this email")        
        elif 'translate' in query:
            speak("Say something in any language")
            query1 = takeCommand().lower()
            translator = Translator()
            translation = translator.translate(query1)
            speak(translation.text)
            print(translation.text)
            time.sleep(5)
        elif 'change voice' in query:
            if(i==0):
                engine.setProperty('voice', voices[1].id)
                i=1
                wishMe()
            else:
                engine.setProperty('voice', voices[0].id)
                i=0
                wishMe()    
        elif 'meaning' in query:
            speak("Say an word")
            query4 = takeCommand().lower()
            print(dictionary.meaning(query4))
            speak(dictionary.meaning(query4))
            time.sleep(3)
        elif 'wait' in query:
            time.sleep(15)    
            speak("I am back again")
        elif 'quit'  in query:
            speak("Thank you")
            quit()   

        else:
            speak("Sorry I am not able to understand your command")    
