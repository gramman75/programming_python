'''
Created on 2013. 1. 17.

@author: stmkmk
'''
from tkinter02 import MyGui
from tkinter import *
from tkinter.messagebox import showinfo

mainwin = Tk()
label = Label(mainwin,text='label')
mygui = MyGui(mainwin)
label.pack(side=LEFT)
mygui.pack(side=RIGHT)
mainwin.mainloop()

