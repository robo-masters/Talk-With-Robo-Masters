from tkinter import *
from tkinter import ttk
import playsound
import speech_recognition as sr
from gtts import gTTS


def listen_user():
    """Capture audio"""

    rec = sr.Recognizer()

    with sr.Microphone() as source:
        print('Robo Masters Lestening To You')
        audio = rec.listen(source)

        try:
            text = rec.recognize_google(audio)
            return text

        except:
            print("Sorry , I Can't Listen To You")
            return 0

def talk(text , file):
    tts = gTTS(text= text , lang = "en")
    filename = "%s.mp3"%file
    tts.save(filename)
    playsound.playsound(filename)

def conatct():
    text_returnd = listen_user()
    if text_returnd == "robo masters":
        talk("Hello Welcome You Can Ask Me" , "save")
    if text_returnd == "hello":
       talk("Hello What is your name", "save6")
       phrase = listen_user()
       name = phrase.split()[-1]
       talk("Nice Name %s"%name, "save7")
    if text_returnd == "how are you":
        talk("Fine Thank You For Ask", "save2")
    if text_returnd == "who are you":
        talk("I Am Robo Masters", "save3")
    if text_returnd == "name":
        talk("I Am Robo Masters", "save4")
    if text_returnd == "hi":
        talk("Hi I Am Robo Masters You Can Ask Me", "save5")
    if text_returnd == "about robo masters":
        talk("The Robo Masters Team are a team of students and teachers from Ali Bin Abi Talib School and they are the robot team and they aspire to win the Who are Robo Masters Team competition", "")
    #I Work To Add More 



root = Tk()
root.title("Robo Masters")
root.geometry("520x600")
root.resizable(False , False)

img = PhotoImage(file='2.png')
LabelPhoto = Label(root, image=img).place(x=0 , y = 0)


ttk.Button(root , text = "Start Talk With Robo Masters" , command = lambda:conatct()).grid(column = 0 , row = 0 ,padx = 175 , pady =500, ipadx = 1 , ipady = 10)

root.mainloop()