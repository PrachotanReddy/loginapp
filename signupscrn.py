import config
from tkinter import *
import mysql.connector
import tkinter.messagebox
from PIL import Image,ImageTk
from tkinter import filedialog
from loginscrn import *
import config

def signup():
    global suscrn
    suscrn=Toplevel(config.home)
    suscrn.geometry("500x500")
    suscrn.configure(bg="#E100FF")
    suscrn.title("Sign Up")
    Label(suscrn,text="Let's Get To Know!",bd=20, font=('arial', 15, 'bold'), relief="groove", fg="white",bg="#7F00FF",width=200).pack()
    Label(suscrn,text="",bg="#E100FF",height="3").pack()
    global usrentry
    global nameentry
    global pwdentry
    usrentry = StringVar()
    nameentry = StringVar()
    pwdentry = StringVar()
    Label(suscrn, text="Name :", fg="black", font=('arial', 12, 'bold')).pack()
    Entry(suscrn, textvariable=nameentry).pack()
    Label(suscrn, text="",bg="#E100FF").pack()
    Label(suscrn, text="UserName :", fg="black", font=('arial', 12, 'bold')).pack()
    Entry(suscrn, textvariable=usrentry).pack()
    Label(suscrn, text="",bg="#E100FF").pack()
    Label(suscrn, text="Password :", fg="black", font=('arial', 12, 'bold')).pack()
    Entry(suscrn, textvariable=pwdentry, show="*").pack()
    Label(suscrn, text="",bg="#E100FF").pack()
    Button(suscrn, text="Join", bg="blue", fg='white', relief="groove", font=('arial', 12, 'bold'),command=user_add).pack()

def user_add():
    usrentry1=usrentry.get()
    nameentry1=nameentry.get()
    pwdentry1=pwdentry.get()
    sql = "insert into user(name,usr,pwd) VALUES(%s,%s,%s)"
    try:
        config.cursordb.execute(sql,[(nameentry1),(usrentry1),(pwdentry1)])
        flag=0
        config.connectiondb.commit()
    except:
        config.connectiondb.rollback()
        tkinter.messagebox.showerror("Error","Error Signing Up :-( \n Kindly check all your fields and try again.")
    if flag==0:
        print("user added successfully")
        wayOut = tkinter.messagebox.askyesno("Sign Up System", "Yayy! Welcome to the family!\n Login now?")
        if wayOut > 0:
            suscrn.destroy()
            return
        else:
            suscrn.destroy()
            config.home.destroy()
            return