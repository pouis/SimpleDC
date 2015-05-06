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
T2.config(state=DISABLED)
# ---------------------

# -----MAP SETUP-----

mapdict = {
    '地下１階': 'map1',
    '地下２階': 'map2',
    '地下３階': 'map3',
}

map1 = []
for i in range(0, 10):
    map1.append(Explore())
for i in range(0, 5):
    map1.append(Encounter())
for i in range(0, 3):
    map1.append(Pit())
for i in range(0, 2):
    map1.append(HiddenDoor())
for i in range(0, 1):
    map1.append(Treasure())

map2 = []
for i in range(0, 2):
    map2.append(Explore())
for i in range(0, 2):
    map2.append(Encounter())
for i in range(0, 2):
    map2.append(Pit())
for i in range(0, 2):
    map2.append(HiddenDoor())
for i in range(0, 2):
    map2.append(Treasure())

map3 = []
for i in range(0, 2):
    map3.append(Explore())
for i in range(0, 2):
    map3.append(Encounter())
for i in range(0, 2):
    map3.append(Pit())
for i in range(0, 2):
    map3.append(HiddenDoor())
for i in range(0, 2):
    map3.append(Treasure())

# ------------------

# -----SETUP EVENT LIST-----
#eventlist = [
#    Explore(),      # 0
#    Encounter(),    # 1
#    Pit(),          # 2
#    HiddenDoor(),   # 3
#]
# ---------------------------

# -----INITIAL SETUP VARIABLES-----
at_home = True
is_alive = True
# ---------------------------------

def checkstatus():
    global text
    global is_alive
    if sukesan._hp <= 0:
        text = '免れることのない死が訪れた。ピンピンころり。やったね！'
        is_alive = False
        btn_explore.grid_forget()
        btn_home.grid_forget()
        display_text()

def display_status():
    _hp = sukesan._hp
    _exp = sukesan._exp
    _gold = sukesan._gold
    _age = sukesan._age
    checkstatus()

    T2.config(state=NORMAL)
    T2.delete(1.0, END)
    T2.insert(END, "L    %s\n" % _hp)
    T2.insert(END, "E    %s\n" % _exp)
    T2.insert(END, "G    %s\n" % _gold)
    T2.insert(END, "A    %s\n" % _age)
    T2.see(END)
    T2.config(state=DISABLED)


def display_text():            # here, you should not put (self) or it breaks
    T.config(state=NORMAL)
    T.insert(END, "%s\n" % text)
    T.see(END)
    T.config(state=DISABLED)


def explore():
    global at_home
    global text

# selectedmap = mapdict[menulist1var.get()]

    if len(map1)==0:
        text="ダンジョンを制覇した！"
        display_text()
        return

    if at_home:
        text = '\n家に負けず劣らず薄暗いダンジョンにもぐった。'
        display_text()
        at_home = False

    eventnb = random.randrange(0, len(map1), 1)  # random select of event
    # event = eventlist[eventnb]          # search in eventlist corresponding event(Class)
    event = map1.pop(eventnb)   # pick up the event from map list
    text = event.eventtext
    display_text()
    testparameter = event.eventtest
    if testparameter == "_str":
        mainchartest = random.randrange(0, sukesan._str+1, 1)
    elif testparameter == "_agi":
        mainchartest = random.randrange(0, sukesan._agi+1, 1)
    elif testparameter == "_int":
        mainchartest = random.randrange(0, sukesan._int+1, 1)
    elif testparameter == "_hp":
        mainchartest = random.randrange(0, sukesan._hp+1, 1)
    else:
        mainchartest = 0
    hurdlecheck(event.eventhurdle, mainchartest, event)
    display_status()


def hurdlecheck(eventhurdle, mainchartest, event):
    global text
    if eventhurdle > mainchartest:  # case fail
        text = event.msgeventfail
        incidenceeffect = random.randrange(event.incidencemin, event.incidencemax+1, 1)
        sukesan._hp -= incidenceeffect
    else:
        text = event.msgeventsucceed  # case succeed
        expeffect = random.randrange(event.expmin, event.expmax+1, 1)
        sukesan._exp += expeffect
        goldeffect = random.randrange(event.goldmin, event.goldmax+1, 1)
        sukesan._gold += goldeffect
    display_text()


def home():
    global at_home
    global is_alive
    if not at_home:
        global text
        text = 'おうちに帰った。'
        at_home = True
        sukesan._hp = sukesan.maxhp
        sukesan._age += 1
        if sukesan._age >= 40:
            print("over40")
            jyumyou = 60
            tenmei = random.randrange(sukesan._age, jyumyou+1, 1)
            print("tenmei")
            if tenmei == jyumyou:
                print("jyumyou")
                is_alive = False
                sukesan._hp= 0

    else:
        text = '狭くて暗くて嫌かもしれませんが、ここがあなたの家です。'
    display_text()
    display_status()

def shop():
    global shopwindow
    btn_explore.config(state=DISABLED)
    btn_home.config(state=DISABLED)
    btn_shop.config(state=DISABLED)
    shopwindow = Toplevel()
    label = Label(shopwindow, text="何を買うんだね？")
    label.pack(side="top", fill="both", padx=10, pady=10)
    shopmenu1var=StringVar()
    shopmenu1var.set('選んでね')
    availablequests = ['あれ','これ','それ']
    shopmenu1 = OptionMenu(shopwindow, shopmenu1var, *availablequests)
    shopmenu1.pack()
    shopwindow.protocol("WM_DELETE_WINDOW", on_closing)
    pass


def on_closing():
    btn_explore.config(state=NORMAL)
    btn_home.config(state=NORMAL)
    btn_shop.config(state=NORMAL)
    shopwindow.destroy()

btn_quit = Button(root, text='Quit', command=root.quit)
btn_quit.grid(row=4, column=3)
btn_explore = Button(root, text='探索する', command=explore)
btn_explore.grid(row=2, column=1)
btn_home = Button(root, text='帰宅する', command=home)
btn_home.grid(row=2, column=3)
btn_shop = Button(root, text='購入する', command=shop)
btn_shop.grid(row=3, column=3)
menulist1var=StringVar()
menulist1var.set('地下１階')
availabledg = ['地下１階','地下２階','地下３階']
menulist1 = OptionMenu(root, menulist1var, *availabledg)
menulist1.grid(row=3, column=1)
menulist1var.get()

sukesan = MainChar(1, "", "sukesan", 50, 50, 80, 80, 80, 80, 80, 0, 0, 36)
display_status()

# --------------TIMER------------
# ---I don't know how to use it properly yet---
# counter = 0
# def counter_label(label):
#  def count():
#    global counter
#    counter += 1
#    label.config(text=str(counter))
#    display_text()
#    label.after(1000, count)
#  count()
# label = Label(root, fg="green")
# counter_label(label)
# -------------------------------

mainloop()
