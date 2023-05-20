
from tkinter import *
import tkinter.messagebox
from VideoFinder import *
root = Tk()
import urllib.request
import urllib.parse
import re
import urllib
from VideoDownloader import *
import time
import tkinter as tk
import os
import cv2
from VideoPlayer import *


textBox = Entry(root, width=50)
textBox.pack()

class NewWindow(tk.Toplevel):
    def __init__(self, parent):
        tk.Toplevel.__init__(self, parent)
        self.title("Play Window")
        self.geometry("200x200")
        self.label = tk.Label(self, text="Videos Found!")
        self.label.pack()
        self.playButton = Button(self, text="Play", command=self.clickPlayButton)
        self.playButton.pack()

    
    def clickPlayButton(self):
        Player()


class Window(Frame): #defines window hahahahh
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.pack(fill=BOTH, expand=1)
        exitButton = Button(self, text="Exit", command=self.clickExitButton)
        
        exitButton.place(x=0, y=0)
        clearButton = Button(self, text="Clear", command=self.clickClearButton)
        
        clearButton.place(x=0, y=20)
        helloButton = Button(self, text="What would you like to learn?", command=self.clickHelloButton)
        helloButton.place(x=42, y=57)
    
    def clickExitButton(self):
        exit()
    
    def clickHelloButton(self): 
        search_query = textBox.get()
        Finder(search_query)
        Downloader()
        new_window = NewWindow(self)
        new_window.mainloop()
        #time.sleep(0.7)
        
        if hasMp4File():
            new_window.playButton.place(x=90, y=90)
        else:
            tkinter.messagebox.showinfo("No MP4 Files", "No MP4 files found in the video files folder.")
        

    def clickClearButton(self):
        return Clear()
         
def hasMp4File():
    folder_path = r"C:\Users\iamsa\Desktop\Code\AVERIS\VideoFiles"  
    files = os.listdir(folder_path)
    for file in files:
        if file.endswith(".mp4"):
            return True
    return False
        
app = Window(root)
root.wm_title("AVERIS") #names the window
root.geometry("320x200")
root.mainloop()
