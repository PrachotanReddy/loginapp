from tkinter import *
import mysql.connector
import tkinter.messagebox
from PIL import Image,ImageTk
from tkinter import filedialog
from loginscrn import *
from signupscrn import *
import config

def dash():
    dashscrn=Toplevel(config.logged_message)
    