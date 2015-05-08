
class Event:
    """common base class for all events"""
    def __init__(self, event_nb, subevent_nb, event_text, event_test, event_hurdle,
                 incidence, incidence_min, incidence_max, exp_min, exp_max,
                 gold_min, gold_max, msg_event_succeed, msg_event_fail):
        self.event_nb = event_nb
        self.subevent_nb = subevent_nb
        self.event_text = event_text
        self.event_test = event_test
        self.event_hurdle = event_hurdle
        self.incidence = incidence
        self.incidence_min = incidence_min
        self.incidence_max = incidence_max
        self.exp_min = exp_min
        self.exp_max = exp_max
        self.gold_min = gold_min
        self.gold_max = gold_max
        self.msg_event_succeed = msg_event_succeed
        self.msg_event_fail = msg_event_fail

    def display(self):
        print(self.event_nb)


class Explore(Event):
    def __init__(self):
        super().__init__(event_nb=0, subevent_nb=0, event_text="探索を続ける", event_test="_hp", event_hurdle=20,
                 incidence="_hp", incidence_min=3, incidence_max=7, exp_min=0, exp_max=0,
                 gold_min=0, gold_max=2, msg_event_succeed="まだまだいける", msg_event_fail="ちょっと疲れた")

# explore = Event(1, 0, "探索を続ける", "Stamina", 6, 20,
#                "Stamina", 6, 3, 7, 0, 0,
#                0, 2, "まだまだいける", "ちょっと疲れた")

# explore.display()
# print(explore.event_text)
# a = Explore()
# print(a.event_text)


class Encounter(Event):
    def __init__(self):
        super().__init__(event_nb=1, subevent_nb=0, event_text="ゾンビに襲われた！", event_test="_str", event_hurdle=50,
                 incidence="_hp", incidence_min=3, incidence_max=7, exp_min=1, exp_max=1,
                 gold_min=0, gold_max=3, msg_event_succeed="逃げた。", msg_event_fail="なんとか撃退した。")


class Pit(Event):
    def __init__(self):
        super().__init__(event_nb=2, subevent_nb=0, event_text="落とし穴だ！", event_test="_agi", event_hurdle=60,
                 incidence="_hp", incidence_min=3, incidence_max=7, exp_min=1, exp_max=2,
                 gold_min=0, gold_max=4, msg_event_succeed="切り抜けた。", msg_event_fail="落ちた・・・")


class HiddenDoor(Event):
    def __init__(self):
        super().__init__(event_nb=3, subevent_nb=0, event_text="気配を感じる！", event_test="_int", event_hurdle=60,
                 incidence="_hp", incidence_min=3, incidence_max=7, exp_min=1, exp_max=2,
                 gold_min=0, gold_max=4, msg_event_succeed="隠し扉を発見！", msg_event_fail="何もなかった・・・")


class Treasure(Event):
    def __init__(self):
        super().__init__(event_nb=4, subevent_nb=0, event_text="宝箱を発見！", event_test="_agi", event_hurdle=60,
                 incidence="_hp", incidence_min=3, incidence_max=7, exp_min=1, exp_max=2,
                 gold_min=0, gold_max=4, msg_event_succeed="色々手に入れた！", msg_event_fail="開かなかった・・・")
