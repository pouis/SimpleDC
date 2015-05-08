#!/usr/bin/env python
from tkinter import *
from tkinter import ttk
from events import *
from mainchar import *
import random

LARGE_FONT = ("Verdana", 12)

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

# -----INITIAL SETUP VARIABLES-----
at_home = True
is_alive = True
# ---------------------------------


class Generator(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}

        for F in (MainPage, ShopPage, PageTwo):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(MainPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class MainPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.s = ttk.Scrollbar(self)
        self.t = Text(self, height=12, width=50)
        self.t2 = Text(self, height=12, width=10)
        self.s.grid(row=1, column=2, sticky='ns')
        self.t.grid(row=1, column=1, columnspan=1)
        self.t2.grid(row=1, column=3, columnspan=1)
        self.s.config(command=self.t.yview)
        self.t.config(yscrollcommand=self.s.set)
        self.t.config(state=DISABLED)
        self.t2.config(state=DISABLED)

        self.label = ttk.Label(self, text="Start Page", font=LARGE_FONT)
        self.label.grid(row=0, column=1, sticky=W)

        self.btn_shop = ttk.Button(self, text="購入する", command=lambda: controller.show_frame(ShopPage))
        self.btn_shop.grid(row=3, column=3)

        self.btn_quit = ttk.Button(self, text='Quit', command=self.quit)
        self.btn_quit.grid(row=4, column=3)
        self.btn_explore = ttk.Button(self, text='探索する', command=self.explore)
        self.btn_explore.grid(row=2, column=1)
        self.btn_home = ttk.Button(self, text='帰宅する', command=self.home)
        self.btn_home.grid(row=2, column=3)
        menu_list1_var = StringVar()
        menu_list1_var.set('地下１階')
        available_dg = ['地下１階', '地下２階', '地下３階']
        menu_list1 = OptionMenu(self, menu_list1_var, *available_dg)
        menu_list1.grid(row=3, column=1)
        menu_list1_var.get()

        display_status(self)

    def display_text(self, itext):
        self.t.config(state=NORMAL)
        self.t.insert(END, "%s\n" % itext)
        self.t.see(END)
        self.t.config(state=DISABLED)

    def explore(self):
        global at_home
        if len(map1)==0:
            text="ダンジョンを制覇した！"
            self.display_text(text)
            return
        if at_home:
            text = '\n家に負けず劣らず薄暗いダンジョンにもぐった。'
            self.display_text(text)
            at_home = False
        
        event_nb = random.randrange(0, len(map1), 1)  # random select of event from map list
        # event = event_list[event_nb]                 # search in event_list corresponding event(Class)
        event = map1.pop(event_nb)                    # pick up the event from map list
        text = event.event_text
        self.display_text(text)
        test_parameter = event.event_test
        if test_parameter == "_str":
            main_char_test = random.randrange(0, sukesan._str+1, 1)
        elif test_parameter == "_agi":
            main_char_test = random.randrange(0, sukesan._agi+1, 1)
        elif test_parameter == "_int":
            main_char_test = random.randrange(0, sukesan._int+1, 1)
        elif test_parameter == "_hp":
            main_char_test = random.randrange(0, sukesan._hp+1, 1)
        else:
            main_char_test = 0
        self.hurdle_check(event.event_hurdle, main_char_test, event)
        display_status(self)

    def hurdle_check(self, event_hurdle, main_char_test, event):
        if event_hurdle > main_char_test:  # case fail
            text = event.msg_event_fail
            incidence_effect = random.randrange(event.incidence_min, event.incidence_max+1, 1)
            sukesan._hp -= incidence_effect
        else:
            text = event.msg_event_succeed  # case succeed
            exp_effect = random.randrange(event.exp_min, event.exp_max+1, 1)
            sukesan._exp += exp_effect
            gold_effect = random.randrange(event.gold_min, event.gold_max+1, 1)
            sukesan._gold += gold_effect
        self.display_text(text)

    def check_status(self):
        global is_alive
        if sukesan._hp <= 0:
            text = '免れることのない死が訪れた。ピンピンころり。やったね！'
            is_alive = False
            self.btn_explore.grid_forget()
            # self.btn_home.grid_forget()
            self.display_text(text)

    def home(self):
        global at_home
        global is_alive
        if not at_home:
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
        self.display_text(text)
        display_status(self)


class ShopPage(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        label = ttk.Label(self, text="何を購入されます？", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        btn_main = ttk.Button(self, text="戻る", command=lambda: controller.show_frame(MainPage))
        btn_main.pack()

        # button2 = ttk.Button(self, text="Page Two", command=lambda: controller.show_frame(PageTwo))
        # button2.pack()


class PageTwo(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        label = ttk.Label(self, text="Page Two!!!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        btn_main = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(MainPage))
        btn_main.pack()

        button2 = ttk.Button(self, text="Page One", command=lambda: controller.show_frame(ShopPage))
        button2.pack()


def display_status(self):
    _hp = sukesan._hp
    _exp = sukesan._exp
    _gold = sukesan._gold
    _age = sukesan._age
    self.check_status()

    self.t2.config(state=NORMAL)
    self.t2.delete(1.0, END)
    self.t2.insert(END, "L    %s\n" % _hp)
    self.t2.insert(END, "E    %s\n" % _exp)
    self.t2.insert(END, "G    %s\n" % _gold)
    self.t2.insert(END, "A    %s\n" % _age)
    self.t2.see(END)
    self.t2.config(state=DISABLED)




sukesan = MainChar(1, "", "sukesan", 50, 50, 80, 80, 80, 80, 80, 0, 0, 36)


app = Generator()
app.mainloop()
