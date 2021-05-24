from tkinter import *
import mysql.connector
import tkinter.messagebox
from PIL import Image,ImageTk
from tkinter import filedialog
from loginscrn import *
from signupscrn import *
import config

def login():
    global usrverify
    global pwdverify
    usrverify=StringVar()
    pwdverify=StringVar()
    config.logscrn=Toplevel(config.home)
    config.logscrn.geometry("500x500")
    config.logscrn.configure(bg="#E100FF")
    config.logscrn.title("Log In")
    Label(config.logscrn,text="Log In Now!",bd=20, font=('arial', 15, 'bold'), relief="groove", fg="white",bg="#7F00FF",width=200).pack()
    Label(config.logscrn,text="",bg="#E100FF",height="3").pack()
    Label(config.logscrn, text="UserName :", fg="black", font=('arial', 12, 'bold')).pack()
    Entry(config.logscrn, textvariable=usrverify).pack()
    Label(config.logscrn, text="",bg="#E100FF").pack()
    Label(config.logscrn, text="Password :", fg="black", font=('arial', 12, 'bold')).pack()
    Entry(config.logscrn, textvariable=pwdverify, show="*").pack()
    Label(config.logscrn, text="",bg="#E100FF").pack()
    Button(config.logscrn, text="Join", bg="blue", fg='white', relief="groove", font=('arial', 12, 'bold'),command=user_verify).pack()

def user_verify():
    usrverify1=usrverify.get()
    pwdverify1=pwdverify.get()
    sql="select * from user where usr=%s and pwd=%s"
    config.cursordb.execute(sql,[(usrverify1),(pwdverify1)])
    results = config.cursordb.fetchall()
    if results:
        for i in results:
            logged()
            break
    else:
        failed()

def logged():
    usrverify1=usrverify.get()
    pwdverify1=pwdverify.get()
    config.logged_message = Toplevel(config.logscrn)
    config.logged_message.title("Welcome")
    config.logged_message.geometry("500x500")
    Label(config.logged_message, text="Login Successfully!... Welcome {} ".format(usrverify.get()), fg="green", font="bold").pack()
    Label(config.logged_message, text="").pack()
    sql="select name from user where usr=%s and pwd=%s"
    config.cursordb.execute(sql,[(usrverify1),(pwdverify1)])
    result = config.cursordb.fetchall()
    Label(config.logged_message,text="Name:",fg="black",font="bold").pack()
    Label(config.logged_message,text=result,fg="#E100FF",font="bold").pack()
    global canvas
    canvas = Canvas(config.logged_message, width = 100, height = 100)
    canvas.pack()
    config.image_label= None
    config.update=None
    Button(config.logged_message, text="Choose Pic", bg="blue", fg='white', relief="groove", font=('arial', 12, 'bold'), command=open_file).pack()
    Button(config.logged_message, text="Logout", bg="blue", fg='white', relief="groove", font=('arial', 12, 'bold'), command=logged_destroy).pack()

def open_file():
    global my_image
    global filename
    if config.image_label:
        config.image_label.destroy()
    if config.update:
        config.update.destroy()
    filename = filedialog.askopenfilename(initialdir="/home/prachotan", title="Select An Image", filetypes=(("jpeg files", "*.jpg"), ("gif files", "*.gif*"), ("png files", "*.png")))
    config.image_label = Label(config.logged_message, text=filename)
    config.image_label.pack()
    my_image = PhotoImage(file=filename)
    canvas.create_image(50, 50, image=my_image)
    config.update=Button(config.logged_message, text="Update Pic", bg="blue", fg='white', relief="groove", font=('arial', 12, 'bold'), command=update_dp)
    config.update.pack()

def update_dp():
    usrverify1=usrverify.get()
    sql="update user set dp=%s where usr=%s"
    config.cursordb.execute(sql,[(filename),(usrverify1)])
    config.connectiondb.commit()
    config.update.destroy()

def failed():
    global failed_message
    failed_message = Toplevel(config.logscrn)
    failed_message.title("Invalid Message")
    failed_message.geometry("500x100")
    Label(failed_message, text="Invalid Username or Password", fg="red", font="bold").pack()
    Label(failed_message, text="").pack()
    Button(failed_message,text="Ok", bg="blue", fg='white', relief="groove", font=('arial', 12, 'bold'), command=failed_destroy).pack()

def logged_destroy():
    config.logged_message.destroy()
    config.logscrn.destroy()

def failed_destroy():
    failed_message.destroy()