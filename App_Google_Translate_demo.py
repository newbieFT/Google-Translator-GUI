from tkinter import *
from PIL import Image, ImageTk
from googletrans import Translator
from win10toast import ToastNotifier
import pyttsx3
import time
from apscheduler.schedulers.blocking import BlockingScheduler
import speech_recognition as sr
import textwrap

# Set the interface
root = Tk()
root.title("Google Galaxy")
root.geometry("500x630")
root.iconbitmap("logo.ico")

# Set background for app
input_file = Image.open("background.png")
bgr = ImageTk.PhotoImage(input_file)
img = Label(root, image=bgr)
img.place(x=0, y=0)

main_title = Label(root, text="Translator", fg="#FFFFFF", bg="#011226", bd=0)
main_title.config(font=("Transformers Movie", 30))
main_title.pack(pady=10)

# Box text
box_1 = Text(root, width=40, height=10, font=("ROBOTO", 10), borderwidth=5)
box_1.pack(pady=10)
box_2 = Text(root, width=40, height=10, font=("ROBOTO", 10), borderwidth=5)
box_2.pack(pady=80)

# Buttons
button_frame = Frame(root).pack(side=BOTTOM)
x = 'Viet'
y = 'Eng'


def clear():
    box_1.delete(1.0, END)
    box_2.delete(1.0, END)


clear_button = Button(button_frame, text="Clear text", font=("Arial", 10, "bold"), fg="#FFFFFF", bg="#011226",
                      borderwidth=7, command=clear)
clear_button.place(x=110, y=280)

a = 'vi'
b = 'en'
def swap():
    global a, b
    box1 = box_1.get(1.0, END)
    box2 = box_2.get(1.0, END)
    # swap
    tmp = box1
    box1 = box2
    box2 = tmp
    clear()
    box_1.insert(END, box1)
    box_2.insert(END, box2)
    tmp_1 = a
    a = b
    b = tmp_1


swap_button = Button(button_frame, text="Swapping", font=("Arial", 10, "bold"), fg="#FFFFFF", bg="#011226",
                     borderwidth=7, command=swap)
swap_button.place(x=210, y=280)
vi_text = Label(root, text=x, fg="#FFFFFF", bg="#18A05E", bd=0)
vi_text.config(font=("Transformers Movie", 20))
vi_text.place(x=40, y=90)
eng_text = Label(root, text=y, fg="#FFFFFF", bg="#18A05E", bd=0)
eng_text.config(font=("Transformers Movie", 20))
eng_text.place(x=40, y=355)


def translate():
    global a
    value = box_1.get(1.0, END)
    wrapper = textwrap.TextWrapper(width=45)
    input_words = wrapper.fill(text=value)
    print(input_words)
    t = Translator()
    if a == 'vi':
        new_words = t.translate(input_words, src='vi', dest='en')
    elif a == 'en':
        new_words = t.translate(input_words, src='en', dest='vi')
    tmp = new_words.text
    box_2.insert(END, tmp)
    if box_1.get(1.0, END) == 0:
        box_2.delete(1.0, END)


trans_button = Button(button_frame, text="Translate", font=("Arial", 10, "bold"), fg="#FFFFFF", bg="#011226",
                      borderwidth=7, command=translate)
trans_button.place(x=310, y=280)

# Record voice
icon_micro = ImageTk.PhotoImage(Image.open("microphone.png"))
icon_speak = ImageTk.PhotoImage(Image.open("speaker.png"))


# English
def speak_en():
    eng_speaker = pyttsx3.init()
    voices = eng_speaker.getProperty('voices')
    eng_speaker.setProperty('voice', voices[2].id)
    eng_speaker.setProperty('rate', 137)
    speak_word = box_2.get(1.0, END)
    eng_speaker.say(speak_word)
    eng_speaker.runAndWait()
speak_en_button = Button(button_frame, image=icon_speak, font=("Arial", 10, "bold"), fg="#FFFFFF", bg="#3C3F41",
                         borderwidth=5, command=speak_en)
speak_en_button.place(x=410, y=480)


def micro():
    c = sr.Recognizer()
    with sr.Microphone() as source:
        c.pause_threshold = 1.5
        audio = c.listen(source)
        if a == 'vi':
            speech = c.recognize_google(audio, language='vi')
            speech.lower()
            box_1.insert(END, speech)
        elif a == 'en':
            speech = c.recognize_google(audio, language='en')
            speech.lower()
            box_1.insert(END, speech)


# Vietnamese
def speak_vi():
    vi_speaker = pyttsx3.init()
    voices = vi_speaker.getProperty('voices')
    vi_speaker.setProperty('voice', voices[0].id)
    vi_speaker.setProperty('rate', 137)
    speak_word = box_1.get(1.0, END)
    vi_speaker.say(speak_word)
    vi_speaker.runAndWait()
speak_vi_button = Button(button_frame, image=icon_speak, font=("Arial", 10, "bold"), fg="#FFFFFF", bg="#3C3F41",
                         borderwidth=5, command=speak_vi)
speak_vi_button.place(x=410, y=225)
micro_button = Button(button_frame, image=icon_micro, font=("Arial", 10, "bold"), fg="#FFFFFF", bg="#3C3F41",
                      borderwidth=5, command=micro)
micro_button.place(x=455, y=225)


# Remind each day to learn
def remind():
    schel = BlockingScheduler()
    while True:
        t = ToastNotifier()
        note = "Spend 5 minutes to learn! \nDo it now"
        t.show_toast("Google Galaxy", note, icon_path="logo.ico", duration=20)
        schel.scheduled_job('cron', day_of_week='mon-sun', hour=8)
        schel.start()


root.mainloop()
remind()
