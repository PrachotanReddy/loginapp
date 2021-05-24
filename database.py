from tkinter import *
import mysql.connector
import tkinter.messagebox
from PIL import Image,ImageTk
from tkinter import filedialog
from loginscrn import *
from signupscrn import *
import config

def main_display():
    config.home=Tk()
    config.home.configure(bg="#E100FF")
    config.home.title("First GUI")
    config.home.geometry("500x500")
    Label(config.home,text="Welcome to Zathura!",bd=20, font=('arial', 20, 'bold'), relief="groove", fg="white",bg="#7F00FF",width=300).pack()
    Label(config.home,text="",bg="#E100FF",height="3").pack()
    Button(config.home,text="LOG IN",font=('arial', 15, 'bold'),relief="groove", fg="white",bg="#7F00FF",height="1",width="20", bd=8,command=login).pack()
    Label(config.home,text="",bg="#E100FF",height="3").pack()
    Button(config.home,text="SIGN UP",font=('arial', 15, 'bold'),relief="groove", fg="white",bg="#7F00FF",height="1",width="20", bd=8,command=signup).pack()
    Label(config.home,text="",bg="#E100FF",height="3").pack()
    Button(config.home,text="QUIT",font=('arial', 15, 'bold'),relief="groove", fg="white",bg="#7F00FF",height="1",width="20", bd=8,command=exit).pack()

def exit():
    wayOut = tkinter.messagebox.askyesno("Login System", "Sorry to See you Go :-(\nExit now?")
    if wayOut > 0:
        config.home.destroy()
        return
main_display()
config.home.mainloop()