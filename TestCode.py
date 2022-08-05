from tkinter import *
from PIL import Image, ImageTk
from googletrans import Translator

#Set the interface
root = Tk()
root.title("Translator Galaxy")
root.geometry("500x630")
root.iconbitmap("logo.ico")

#Set the back ground
input_img = Image.open("background.png")
bgr = ImageTk.PhotoImage(input_img)
bg = Label(root, image=bgr)
bg.place(x=0, y=0)

main_title = Label(root, text="Translator", fg="#FFFFFF", bg="#010E21", bd=0)
main_title.config(font=("Transformers Movie", 30))
main_title.pack(pady=20)

#Box text:
box_1 = Text(root, width=40, height=10, font=("ROBOTO", 10), borderwidth=5)
box_1.pack(pady=10)
box_2 = Text(root, width=40, height=10, font=("ROBOTO", 10), borderwidth=5)
box_2.pack(pady=80)


root.mainloop()