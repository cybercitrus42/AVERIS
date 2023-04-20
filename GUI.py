
from tkinter import *
import tkinter.messagebox
root = Tk()

textBox = Entry(root, width=50)
textBox.pack()

class Window(Frame): #defines window hahahahh
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

        self.pack(fill=BOTH, expand=1)

        #exitButton = Button(self, text="Exit", command=self.clickExitButton)
        
        #exitButton.place(x=0, y=0)

        helloButton = Button(self, text="What would you like to learn?", command=self.clickHelloButton)

        helloButton.place(x=42, y=57)


    def clickExitButton(self):
        exit()

    def clickHelloButton(self): 
        #tkinter.messagebox.showinfo("winner")
        Search = Label(root, text = textBox.get())
        Search.pack()
        #tkinter.messagebox.showinfo("Fruit List!!", readFruitContents)
        #tkinter.messagebox.showinfo("Fruit List", random_line('fruitList.txt'))


app = Window(root)
root.wm_title("Tkinter window") #names the window
root.geometry("320x200")
root.mainloop()