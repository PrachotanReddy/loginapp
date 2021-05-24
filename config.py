from tkinter import *
import mysql.connector
import tkinter.messagebox
from PIL import Image,ImageTk
from tkinter import filedialog
from loginscrn import *
from signupscrn import *

global home
global logscrn
global logged_message
global image_label
global update
connectiondb = mysql.connector.connect(host="localhost",user="root",passwd="bunny669",database="logindb")
cursordb = connectiondb.cursor()