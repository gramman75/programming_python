'''
Created on 2013. 1. 17.

@author: stmkmk
'''

from tkinter import *
from tkinter.messagebox import showinfo, showerror
import shelve

fieldnames =('name','age','pay','job')
db = shelve.open('people-class')
entries ={}

def makeWidjets():
    mainwin = Tk()
    mainwin.title('People Shelve')
    form = Frame(mainwin)
    
    for (ix, label) in enumerate(('key',)+ fieldnames):
        lab = Label(form, text=label)
        ent = Entry(form)
        lab.grid(row=ix, column=0)
        ent.grid(row=ix, column=1)
        entries[label] = ent
    form.pack()
    Button(mainwin, text='Fetch', command=fetchRecord).pack(side=LEFT)
    Button(mainwin, text='Update', command=updateRecord).pack(side=LEFT)
    Button(mainwin, text='Quit', command=mainwin.quit).pack(side=RIGHT)
    return mainwin

def fetchRecord():
    key = entries['key'].get()
    if not key:
        showerror(title='Error', message='Input Key Value')
    try:
        record = db[key]
    except:
        showerror(title='Error', message='Can not find %s key' %key)
    else:
        for field in fieldnames:
            #entries[field] = getattr(record, field)
            entries[field].delete(0, END)
            entries[field].insert(0, repr(getattr(record, field)))
            
def updateRecord():
    key = entries['key'].get()
    if not key:
        showerror(title='Error', message='Input Key Value')
    else:
        try:
            record = db[key]
        except:
            from person_start import Person
            record = Person(name="?", age="?")
        
        
        for field in fieldnames:
            setattr(record, field, eval(entries[field].get()))
        db[key] = record

window = makeWidjets()
window.mainloop()
db.close()
    
    