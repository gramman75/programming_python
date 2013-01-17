'''
Created on 2013. 1. 17.

@author: stmkmk
'''
from tkinter import *
from tkinter.messagebox import showinfo

class MyGui(Frame):
    def __init__(self,parent=None):
        Frame.__init__(self,parent)
        button = Button(self, text='press', command = self.reply)
        button.pack()
    def reply(self):
        showinfo(title='popup', message='Button Pressed')
        
class CustomGui(MyGui):
    def reply(self):
        showinfo(title='popup',message='Ouch!')
        
if __name__ == '__main__':
    '''
    window = MyGui()
    window.pack()
    window.mainloop()
    '''
    window = CustomGui()
    window.pack()
    window.mainloop()
        
        
        