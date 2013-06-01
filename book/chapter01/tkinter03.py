'''
Created on 2013. 1. 17.

@author: stmkmk
'''
from tkinter import *
from tkinter.messagebox import showinfo

def reply(name):
    showinfo(title='Reply', message='Hello %s!' %name)

mainwin = Tk()
mainwin.title('Call Me Name')
mainwin.iconbitmap('events.ico')
Label(mainwin, text="Enter Your Name:").pack(side=TOP)
ent = Entry(mainwin)
ent.pack(side=TOP)
Button(mainwin, text="Submit", command=(lambda:reply(ent.get()))).pack(side=LEFT)
mainwin.mainloop()
