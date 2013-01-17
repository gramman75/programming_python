'''
Created on 2013. 1. 17.

@author: stmkmk
'''
from tkinter import *
from tkinter.messagebox import showinfo

def reply():
    showinfo(title="popup", message="Button Pressed")
    
window = Tk()
label = Label(window,text="test")
button =Button(window,text='Button', command=reply)
button.pack()
label.pack()
window.mainloop()