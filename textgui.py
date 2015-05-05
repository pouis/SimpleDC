#!/usr/bin/env python

from tkinter import *
from events import *
from mainchar import *
import random

# -----SCREEN SETUP-----
root = Tk()
S = Scrollbar(root)
T = Text(root, height=12, width=50)
T2 = Text(root, height=12, width=10)
S.grid(column=2, row=0, sticky='ns')
T.grid(column=1, row=0, columnspan=1)
T2.grid(column=3, row=0, columnspan=1)
S.config(command=T.yview)
T.config(yscrollcommand=S.set)
T.config(state=DISABLED)
# ---------------------

# -----SETUP EVENT LIST-----
eventlist = [
    Explore(),      # 0
    Encounter(),    # 1
    Pit(),          # 2
    HiddenDoor(),   # 3
]
# ---------------------------


def show_entry_fields(self):    # need to put (self) otherwise e.bind('<Return>', show_entry_fields) doesn't work
    userinput = e.get()
    T.config(state=NORMAL)      # allow display area to be edited
    T.insert(END, ">%s\n" % userinput)  # insert text from the input field
    T.see(END)
    T.config(state=DISABLED)    # lock display are from editing so that user can't type in directly
    e.delete(0, END)            # clear the input field
    evaluate(userinput)


def display_quote():            # here, you should not put (self) or it breaks
    T.config(state=NORMAL)
    T.insert(END, "%s\n" % quote)
    T.see(END)
    T.config(state=DISABLED)


def evaluate(userinput):
    global quote
    if userinput == "bonjour":
        quote = "nice to meet you"
        display_quote()
    elif userinput == "":
        eventnb = random.randrange(0, 4, 1)  # random select of event
        event = eventlist[eventnb]          # search in eventlist corresponding event(Class)
        quote = event.eventtext
        display_quote()
        mainchartest = event.eventtest
        a=sukesan._agi
        print(mainchartest)
        print(a)
        #hurdlecheck(event.eventhurdle,b)


def hurdlecheck(eventhurdle, b):
    pass

Label(root, text=">").grid(row=1, column=0, sticky=W+E)
e = Entry(root)
e.grid(row=1, column=1, sticky=W+E)
e.bind('<Return>', show_entry_fields)
Button(root, text='Quit', command=root.quit).grid(row=2, column=1)


quote = "test display"
display_quote()
explore = Explore()
explore.display()
print(explore.eventtext)
sukesan = MainChar(1, "", "sukesan", 100, 100, 100, 100, 100, 100, 100)

#--------------TIMER------------
#---I don't know how to use it properly yet---
#counter = 0
#def counter_label(label):
#  def count():
#    global counter
#    counter += 1
#    label.config(text=str(counter))
#    display_quote()
#    label.after(1000, count)
#  count()
#label = Label(root, fg="green")
#counter_label(label)
#-------------------------------

mainloop()