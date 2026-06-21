import pyttsx3
import speech_recognition as sr
from googletrans import Translator
import datetime
import os
import cv2
import random
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import smtplib 
import sys

def speak(audio):
    engine=pyttsx3.init('sapi5')
    voices=engine.getProperty('voices')
#print (voices[0].id) 0=male voice , 1= female voice
    engine.setProperty('voices',voices[0].id)
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def takecom():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("LISTNING...")
        r.pause_threshold=2
        audio=r.listen(source,timeout=1,phrase_time_limit=5)

    try:
        print("RECOGNISING...")
        query=r.recognize_google(audio,language='en-in')
        translator=Translator()
        english=translator.translate(query , src='hi' , dest='en').text
      #  print(f"you said : {engine}")
        speak(english)
        
    except Exception as e:
        speak("say that again please...")
        return "none"
    return english

def wish():
    hour = int(datetime.datetime.now().hour)

    if hour >=0 and hour <=12:
        speak("GOOD MORNING SIR DOMINO AT YOUR SERVICE...")
    elif hour>12 and hour<=15:
        speak("GOOD EVENING SIR  DOMINO AT YOUR SERVICE...")
    elif hour>15 and hour<=20:
        speak("GOOD EVENING SIR DOMINO AT YOUR SERVICE...")
    else:
        speak("GOOD NIGHT SIR DOMINO AT YOUR SERVICE...")
    speak("what can i help you ?")

def email(to , con):
    server=smtplib.SMTP("smtp.gmail.com" , 587)
    server.ehlo()
    server.starttls()
    server.login("tvaishnavi513@gmail.com" , "psop purc hhkr gsmt")
    server.sendmail("tvaishnavi513@gmail.com" , to , con)
    server.close()


if __name__=="__main__":
    wish()
    while True:

        query=takecom().lower()

        if "open notepad" in query:
            npath="C:\\windows\\system32\\notepad.exe"
            os.startfile(npath)
        elif "open command prompt" in query:
            os.system("start cmd")

        elif "open camera" in query:
            cap=cv2.VideoCapture(0)
            while True:
                ret,img = cap.read()
                cv2.imshow('webcam',img)
                k=cv2.waitKey(50)
                if k==30:
                    break;
            cap.release()
            cv2.destroyAllWindows()

        elif "ip address" in query:
            ip=get('https://api.ipify.org').text
            speak(f"your ip address is : {ip}")
        
        elif "wikipedia" in query :
            speak("searching wikipedia")
            wikipedia.set_lang("en")
            summary = wikipedia.summary(query, sentences=3)
            speak("according to wikipedia")
            speak(summary)
            print(summary)

            search_results = wikipedia.search(query)
            print("\nSearch Results:")
            for result in search_results:
                speak(result)
                print(result)

            try:
                page = wikipedia.page(query)
                print("\nFull Page Content:")
                print(page.content[:500]) # Print first 500 characters for brevity
            except wikipedia.exceptions.PageError:
                print("\nPage not found.")
            except wikipedia.exceptions.DisambiguationError as e:
                print(f"\nDisambiguation page. Options: {e.options}")

# Access other properties of a page object
            try:
                page = wikipedia.page(query)
                print(f"\nPage Title: {page.title}")
                print(f"Page URL: {page.fullurl}")
                print(f"Page Categories: {page.categories}")
                print(f"Page Images (first 5): {page.images[:5]}")
            except wikipedia.exceptions.PageError:
                print("\nPage not found.")

        elif "open youtube" in query:
            ypath="https://www.youtube.com/?authuser=0"
            os.startfile(ypath)

        elif "open instagram" in query:
            ipath="C:\\Users\\acer\\OneDrive\\Desktop\\Instagram.lnk"
            os.startfile(ipath)
        
        elif "open telegram" in query:
            tpath="C:\\Users\\acer\\OneDrive\\Desktop\\Telegram.lnk"
            os.startfile(tpath)
        
        elif "open whatsapp" in query:
            wpath="C:\\Users\\acer\\OneDrive\\Desktop\\WhatsApp.lnk"
            os.startfile(wpath)
        
        elif "open chrome" in query:
            wpath="C:\\Users\\Public\\Desktop\\Google Chrome.lnk"
            os.startfile(wpath)

        elif "open playlist" in query:
            wpath="https://www.youtube.com//watch?v=XyO0vnidCGY&list=PL-T70U7BaA6lnZ6x54niLAzS723IDg_-8"
            webbrowser.open(wpath)
        
        elif "open google" in query:
            speak("what i must search on google?")
            cm=takecom().lower()
            webbrowser.open(f"{cm}")

        elif "play song on youtube" in query:
            def songg():
                fav=["hymn of the weekend","into the stars","something just like this","calm down","surmedani","faded","senorita"]
                speak("would you like to listen : ")
                r=random.choice(fav)
                speak(r)
                speak("are you ok with the song suggested? or you would choose accoring to your wish?")
                dec=takecom().lower()
                if "no" in dec:
                    songg()
                elif "yes" in dec:
                    kit.playonyt(r)
                else:
                    speak("ok sir , what you would like to listen?")
                    song=takecom().lower()
                    kit.playonyt(f"{song}")
            songg()  
            
                

        elif "send message" in query:
            speak("through which app?")
            app=takecom().lower()
            if "whatsapp" in app:
                speak("to whom you want to send the message")
                mess=takecom().lower()
                speak("say your message")
                say=takecom().lower()
                kit.sendwhatmsg("+918840544701" , say ,3,15, wait_time= 5)

            elif "email" in app:
                try:
                    speak("say your mssg")
                    con=takecom().lower()
                    to="signor849@gmail.com"
                    email(to,con)
                    speak("send successfully")
                except Exception as e:
                    print (e)
                    speak ("sorry")

        elif "no thanks" in query:
            speak("domino falling")
            sys.exit()
        
        speak("sir , do you want to give another command?")
                


