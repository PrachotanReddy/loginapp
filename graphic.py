from tkinter import *
import mysql.connector

def submit():
    usr1=usr_storge.get()
    pwd1=pwd_storge.get()
    print("User added:   "+usr1+"\tWith Password: "+pwd1)
    usr.delete(0,END)
    pwd.delete(0,END)
screen = Tk()
screen.configure(bg="#C6426E")
screen.title("First GUI")
screen.geometry("500x500")

wtext=Label(text="Login",fg="#642B73",bg="#C6426E",activebackground="#ff5e62",anchor="nw",font=('calibre',20, 'bold'))
wtext.pack()

usr_label=Label(text="Username",fg="#ec38bc",bg="#C6426E",font=('calibre',10, 'bold'))
usr_storge=StringVar()
usr=Entry(textvariable=usr_storge,relief=RAISED)
usr_label.pack()
usr.pack()
pwd_label=Label(text="Password",fg="#ec38bc",bg="#C6426E",font=('calibre',10, 'bold'))
pwd_storge=StringVar()
pwd=Entry(textvariable=pwd_storge,relief=RAISED,show="$")
pwd_label.pack()
pwd.pack()
btn=Button(text="Hit Me",fg="#fdbb2d",bg="#1a2a6c",command=submit)
btn.pack()


screen.mainloop()