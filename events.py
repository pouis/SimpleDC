
class Event:
    """common base class for all events"""
    def __init__(self, eventnb, subeventnb, eventtext, eventtest, eventhurdle,
                 incidence, incidencemin, incidencemax, expmin, expmax,
                 goldmin, goldmax, msgeventsucceed, msgeventfail):
        self.eventnb = eventnb
        self.subeventnb = subeventnb
        self.eventtext = eventtext
        self.eventtest = eventtest
        self.eventhurdle = eventhurdle
        self.incidence = incidence
        self.incidencemin = incidencemin
        self.incidencemax = incidencemax
        self.expmin = expmin
        self.expmax = expmax
        self.goldmin = goldmin
        self.goldmax = goldmax
        self.msgeventsucceed = msgeventsucceed
        self.msgeventfail = msgeventfail

    def display(self):
        print(self.eventnb)


class Explore(Event):
    def __init__(self):
        super().__init__(eventnb=0, subeventnb=0, eventtext="探索を続ける", eventtest="_hp", eventhurdle=20,
                 incidence="_hp", incidencemin=3, incidencemax=7, expmin=0, expmax=0,
                 goldmin=0, goldmax=2, msgeventsucceed="まだまだいける", msgeventfail="ちょっと疲れた")

# explore = Event(1, 0, "探索を続ける", "Stamina", 6, 20,
#                "Stamina", 6, 3, 7, 0, 0,
#                0, 2, "まだまだいける", "ちょっと疲れた")

# explore.display()
# print(explore.eventtext)
# a = Explore()
# print(a.eventtext)


class Encounter(Event):
    def __init__(self):
        super().__init__(eventnb=1, subeventnb=0, eventtext="ゾンビに襲われた！", eventtest="_str", eventhurdle=50,
                 incidence="_hp", incidencemin=3, incidencemax=7, expmin=1, expmax=1,
                 goldmin=0, goldmax=3, msgeventsucceed="逃げた。", msgeventfail="なんとか撃退した。")


class Pit(Event):
    def __init__(self):
        super().__init__(eventnb=2, subeventnb=0, eventtext="落とし穴だ！", eventtest="_agi", eventhurdle=60,
                 incidence="_hp", incidencemin=3, incidencemax=7, expmin=1, expmax=2,
                 goldmin=0, goldmax=4, msgeventsucceed="切り抜けた。", msgeventfail="落ちた・・・")


class HiddenDoor(Event):
    def __init__(self):
        super().__init__(eventnb=3, subeventnb=0, eventtext="気配を感じる！", eventtest="_int", eventhurdle=60,
                 incidence="_hp", incidencemin=3, incidencemax=7, expmin=1, expmax=2,
                 goldmin=0, goldmax=4, msgeventsucceed="隠し扉を発見！", msgeventfail="何もなかった・・・")


class Treasure(Event):
    def __init__(self):
        super().__init__(eventnb=4, subeventnb=0, eventtext="宝箱を発見！", eventtest="_agi", eventhurdle=60,
                 incidence="_hp", incidencemin=3, incidencemax=7, expmin=1, expmax=2,
                 goldmin=0, goldmax=4, msgeventsucceed="色々手に入れた！", msgeventfail="開かなかった・・・")
