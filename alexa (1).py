import os
#used to access system details and process utilities.
import psutil

#convert audio into text for further processing.
import speech_recognition as sr

# text-to-speech conversion
import pyttsx3
import datetime

#Play a YouTube video.and Perform a Google Search.
import pywhatkit

import subprocess
# provides the ability to simulate mouse cursor moves and clicks as well as keyboard button presses.
import pyautogui
import screen_brightness_control
import AppOpener
import pyaudio

#allows displaying Web-based documents to users.
import webbrowser


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')     #gets the current value of engine property
#0]=male voice and
# [1]=female voice in set Property.
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        print("Good Morning!")
        talk("good morning! ")

    elif hour >= 12 and hour < 18:
        print("Good Afternoon!")
        talk("Good Afternoon!")


    else:
        print("Good Evening!")
        talk("Good Evening!")

    talk("I am alexa... Please tell me how may I help you")
    print("I am alexa... Please tell me how may I help you")


def take_command():
    try:
        with sr.Microphone() as source:
            hour = int(datetime.datetime.now().hour)
            print("\nlistening.....")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass
    return command


def run_alexa():
    command = take_command()
    print(command)

    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)

    elif 'open youtube' in command :
        webbrowser.open("youtube.com")

    elif "open google" in command :
        webbrowser.open("google.com")

    elif "open wikipedia" in command:
        webbrowser.open("wikipedia.com")


    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('current time is ' + time)

    elif "open notepad" in command :
        pyttsx3.speak("opening notepad")
        print("OPENING NOTEPAD")
        os.system("notepad")

    elif 'open calculator ' in command :
        subprocess.Popen("C:\Windows\System32\calc.exe")

    elif 'open any desk' in command:
        pyttsx3.speak("opening any desk")
        print("opening any desk")
        subprocess.Popen("C:\\Program Files (x86)\\AnyDesk\\AnyDesk.exe")


    elif "shut down " in command:
        os.system("shutdown /s /t 1")

    elif "restart " in command:
        os.system("shutdown /r /t 1")

    elif "c drive" in command:
        os.startfile("C:")

    elif "d drive" in command:
        os.startfile("D:")

    elif "e drive" in command:
        os.startfile("E:")

    elif "screenshot" in command :
        ss = pyautogui.screenshot()
        ss.save(r'D:\screenshot\screenhot_1.png')

    elif "battery " in command :
        battery= psutil.sensors_battery()

        print("Battery percentage : ", battery.percent)
        talk("Battery percentage : ")
        talk(battery.percent)
        print("power plugged in  :", battery.power_plugged )
        talk('power plugged in  : ')
        talk(battery.power_plugged)

    elif " increase volume" in command :
        pyautogui.press('volumeup')

    elif " decrease volume" in command :
        pyautogui.press('volumedown')

        ''''elif " set brightness to 25" in command :
        current_brightness = screen_brightness_control .get_brightness()
        print(current_brightness)
        talk(current_brightness )
        primary_brightness = screen_brightness_control.get_brightness(display=0)
        print(primary_brightness)
        print(screen_brightness_control.set_brightness(25) )
        print(screen_brightness_control.get_brightness())'''


    elif " set brightness to 50" in command :
        current_brightness = screen_brightness_control .get_brightness()
        print(current_brightness)
        talk(current_brightness )
        primary_brightness = screen_brightness_control.get_brightness(display=0)
        print(primary_brightness)
        print(screen_brightness_control.set_brightness(50) )
        print(screen_brightness_control.get_brightness() )
        talk(screen_brightness_control.get_brightness())


    elif " set brightness to 75" in command :
        current_brightness = screen_brightness_control .get_brightness()
        print(current_brightness)
        primary_brightness = screen_brightness_control.get_brightness(display=0)
        print(primary_brightness)
        talk(current_brightness )
        print(screen_brightness_control.set_brightness(75,display= 0) )
        print(screen_brightness_control.get_brightness() )


    elif " set brightness to 100" in command :
        current_brightness = screen_brightness_control .get_brightness()
        print(current_brightness)
        talk(current_brightness )
        primary_brightness = screen_brightness_control.get_brightness(display=0)
        print(primary_brightness)
        print(screen_brightness_control.set_brightness(100) )
        print(screen_brightness_control.get_brightness())



            
       # ---------------------------------------------------------------------------------

    elif 'open cmd'  in command:
        subprocess.Popen("C:\\Windows\\System32\\cmd.exe")

    elif 'open xmapp'  in command:
        #subprocess.Popen("C:\\xampp\\xampp_start.exe")
        os.startfile("C:\\xampp\\xampp_start.exe")

    elif "open camera" in command :
        os.system("start microsoft .windows. camera :")

    elif "open word" in command:
        pyttsx3.speak("opening word")
        print("OPENING WORD")
        os.system("winword")

        '''elif "open vlcplayer" in command:
        pyttsx3.speak("opening word")
        print("OPENING WORD")
        os.system("VLC")'''



    elif "open excel" in command :
        pyttsx3.speak("opening excel")
        print("OPENING EXCEL")
        os.system("excel")

    elif "open powerpoint" in command :
        pyttsx3.speak("opening power point")
        print("OPENING POWER POINT")
        os.system("powerpnt")



    elif "open paint" in command:
        pyttsx3.speak("opening paint")
        print("OPENING PAINT")
        os.system("paint")

        '''elif 'open xmapp':
                subprocess.Popen("C:\\xampp\\xampp_start.exe")'''

        '''elif 'open notepad':
        subprocess.Popen("C:\\Windows\\System32\\notepad.exe")'''

        '''elif " open camera" in command :
                pyttsx3.speak("opening camera")
                print("OPENING CAMERA")
                subprocess.Popen("camera.exe")'''



    else:
        talk('please say the command again..')


wishme()
while True:
    run_alexa()