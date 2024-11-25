import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import time

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice','voices[200s].id')


def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    speak("Hi, I'm Cell.....")
    time.sleep(1)
    speak("What can I do for you")
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("By the way,Good Morning")
        print("By the way,Good Morning")
    elif hour>=12 and hour<18:
        speak("By the way,Good Afternoon")
        print("By the way,Good Afternoon")
    else:
        speak("By the way,Good Evening")
        print("By the way,Good Evening")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio=r.listen(source)

        try:
            statement=r.recognize_google(audio,language='en-in')
            print(f"user said:{statement}\n")

        except Exception as e:
            speak("PLease repeat what you said")
            return "None"
        return statement

if __name__=='__main__':
    wishMe()


    while True:
        statement = takeCommand().lower()
        if statement==0:
            break
        if "goodbye" in statement or "ok bye" in statement or "stop" in statement:
            speak("Goodbye... I'm Shutting.. down")
            print("Goodbye... I'm Shutting.. down")
            break
        elif statement == "shutdown":
            speak("Goodbye... I'm Shutting.. down")
            print("Goodbye... I'm Shutting.. down")
            break
        elif statement=="Hi":
            speak("Hi I'm Cel")
            print("Hi I'm Cel")
            break

        if 'open youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com/")
            speak("youtube is now open")
            time.sleep(5)

        elif 'open google' in statement:
            webbrowser.open_new_tab("https://www.google.com/")
            speak("Google chrome is now open")
            time.sleep(5)

        elif 'open gmail' in statement:
            webbrowser.open_new_tab("https://mail.google.com/mail/u/0/")
            speak("Gmail is now open, please login your account")
            time.sleep(5)

        elif 'time' in statement:
            current_time = datetime.datetime.now()
            hour = current_time.hour
            minute = current_time.minute
            
            if hour == 0:
                hour_str = "midnight"
            elif hour == 12:
                hour_str = "noon"
            elif hour < 12:
                hour_str = f"{hour} AM"
            else:
                hour_str = f"{hour - 12} PM"
            if minute == 0:
                minute_str = " "
            elif minute < 10:
                minute_str = f"oh {minute}"
            else:
                minute_str = str(minute)
                
            spoken_time = f"It's {hour_str} and {minute_str} minutes"
            speak(spoken_time)
            time.sleep(1)
            speak ("Is there anything else you would like me to do")

        elif 'what can you do' in statement:
            speak("Basically since I'm just an AI created for fun, I'm just literally nothing but a piece of work")

        elif "who made you" in statement or "who created you" in statement:
            speak("The..guy..who..made..me..is..nothing..but..the..most..lodi..and..the..most..handsome..lodicakes..'REKCEL'")
            print("The guy who made me is nothing but the most lodi and the most handsome lodicakes 'REKCEL'")
        
        elif "Who are you?" in statement or "who the heck are you" in statement:
            speak("I'm Cell and I'm an AI who can be anything someday like chatGPT")
            print("I'm Cell and I'm an AI who can be anything someday like chatGPT")
        elif "open instagram" in statement:
            webbrowser.open_new_tab("https://www.instagram.com/")
            speak("Here is your instagram")
        
        elif "open stack overflow" in statement:
            webbrowser.open_new_tab("https://stackoverflow.com/")
            speak("Here is stackoverflow")



time.sleep(3)












