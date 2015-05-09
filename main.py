#!/usr/bin/env python
from tkinter import *
from tkinter import ttk
from events import *
from mainchar import *
import random

LARGE_FONT = ("Verdana", 12)

# -----MAP SETUP-----

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

mapdict = {
    '地下１階': map1,
    '地下２階': map2,
    '地下３階': map3,
}

current_map = map1
# ------------------


# -----MAIN CHARACTER SETUP-----
char1 = MainChar(1, "", "スケ郎", 25, 25, 70, 70, 70, 70, 70, 0, 0, 36)
char2 = MainChar(2, "", "スケ次", 50, 50, 80, 80, 80, 80, 80, 0, 0, 36)
char3 = MainChar(3, "", "すけさん", 100, 100, 90, 90, 90, 90, 90, 0, 0, 36)

chardict = {
    'スケ郎': char1,
    'スケ次': char2,
    'すけさん': char3,
}
sukesan = char1
# ------------------------------


# ----- Window Management System -----
# I don't fully understand how it works, but it works
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
# ----------------------------------


# -----Start of Main Page Window and Executions -----
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
        self.btn_home = ttk.Button(self, text='帰宅する', command=self._handle_home)
        self.btn_home.grid(row=2, column=3)
        menu_list1_var = StringVar()
        menu_list1_var.set('地下１階')
        available_dg = ['地下１階', '地下２階', '地下３階']
        # available_dg = mapdict.keys() # Why if I replace above line with this, it does not work?
        print(available_dg)
        self.menu_list1 = ttk.OptionMenu(self, menu_list1_var, None, *available_dg, command=self.select_map)
        self.menu_list1.grid(row=3, column=1)
        menu_list2_var = StringVar()
        menu_list2_var.set('スケ郎')
        available_char = ['スケ郎', 'スケ次', 'すけさん']
        menu_list2_var.set(available_char[0])
        self.menu_list2 = ttk.OptionMenu(self, menu_list2_var, None, *available_char, command=self.select_char)
        self.menu_list2.grid(row=4, column=1)

        self.display_status()
        self._event = None

    def select_map(self, map_name):
        global current_map
        current_map = mapdict[map_name]
        print(current_map)

    def select_char(self, char_name):
        global sukesan
        sukesan = chardict[char_name]
        self.display_status()
        print(sukesan)

    def display_text(self, itext):
        self.t.config(state=NORMAL)
        self.t.insert(END, "%s\n" % itext)
        self.t.see(END)
        self.t.config(state=DISABLED)

    def explore(self):
        if not sukesan.is_alive:
            return

        if len(current_map) == 0:
            text = "このダンジョンは制覇した！"
            self.display_text(text)
            self.btn_home.config(state=NORMAL)
            return

        self.btn_explore.config(state=DISABLED)
        self.btn_shop.config(state=DISABLED)
        self.menu_list1.config(state=DISABLED)

        if sukesan.at_home:
            text = '\n家に負けず劣らず薄暗いダンジョンにもぐった。'
            self.display_text(text)
            sukesan.at_home = False
        if self._event is None:
            self._next_event()
        else:
            self._process_event(self._event.event_hurdle, main_char_test, self._event)
            self._event = None
            self.display_status()
            self.btn_home.config(state=NORMAL)

        # ----- Loop Execution with Timer -----
        self.timer_id = self.after(500, self.explore)    # this is the loop execution with timer
        # self.after_cancel(timer_id)
        # ------------------------------------

    def _next_event(self):
        global main_char_test
        event_nb = random.randrange(0, len(current_map), 1)  # random select of event from map list
        self._event = current_map.pop(event_nb)                    # pick up the event from map list
        main_char_max = getattr(sukesan, self._event.event_test) or 0
        main_char_test = random.randrange(1, main_char_max + 1, 1)
        text = "%s %s %s/%s" % (self._event.event_text, self._event.event_test, self._event.event_hurdle, main_char_max)
        self.display_text(text)
        self.btn_home.config(state=DISABLED)

    def _process_event(self, event_hurdle, main_char_test, event):
        if event_hurdle > main_char_test:  # case fail
            text = "%s %s" % (main_char_test, event.msg_event_fail)
            incidence_effect = random.randrange(event.incidence_min, event.incidence_max + 1, 1)
            sukesan.damage(incidence_effect)
            if not sukesan.is_alive:
                self._handle_death()
                return
        else:   # case succeed
            text = "%s %s" % (main_char_test, event.msg_event_succeed)
            exp_effect = random.randrange(event.exp_min, event.exp_max + 1, 1)
            sukesan._exp += exp_effect
            gold_effect = random.randrange(event.gold_min, event.gold_max + 1, 1)
            sukesan._gold += gold_effect
        self.display_text(text)

    def _handle_death(self):
        text = '免れることのない死が訪れた。ピンピンころり。やったね！'
        self.btn_explore.grid_forget()
        self.btn_home.grid_forget()
        self.display_text(text)

    def _handle_home(self):
        self.after_cancel(self.timer_id)  # used to stop timer but also causes error when no timer on.
        if not sukesan.at_home:
            self._home()
        else:
            text = '狭くて暗くて嫌かもしれませんが、ここがあなたの家です。'
            self.display_text(text)
            self.display_status()

    def _home(self):
        text = 'おうちに帰った。'
        sukesan.go_home()
        self.btn_shop.config(state=NORMAL)
        self.menu_list1.config(state=NORMAL)
        self.btn_explore.config(state=NORMAL)
        self.display_text(text)
        self.display_status()

    def display_status(self):
        _hp = sukesan._hp
        _exp = sukesan._exp
        _gold = sukesan._gold
        _age = sukesan._age

        self.t2.config(state=NORMAL)
        self.t2.delete(1.0, END)
        self.t2.insert(END, "L    %s\n" % _hp)
        self.t2.insert(END, "E    %s\n" % _exp)
        self.t2.insert(END, "G    %s\n" % _gold)
        self.t2.insert(END, "A    %s\n" % _age)
        self.t2.see(END)
        self.t2.config(state=DISABLED)
# ----- END of Main Page Window -----


# ----- Start of Shop Page and Executions -----
class ShopPage(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        label = ttk.Label(self, text="何を購入されます？", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        btn_main = ttk.Button(self, text="戻る", command=lambda: controller.show_frame(MainPage))
        btn_main.pack()

        # button2 = ttk.Button(self, text="Page Two", command=lambda: controller.show_frame(PageTwo))
        # button2.pack()
# ----- END of Shop Page -----


class PageTwo(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        label = ttk.Label(self, text="Page Two!!!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        btn_main = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(MainPage))
        btn_main.pack()

        button2 = ttk.Button(self, text="Page One", command=lambda: controller.show_frame(ShopPage))
        button2.pack()


app = Generator()
app.mainloop()
