import random


class MainChar:
    """common base class for all main characters"""
    def __init__(self, charnb, title, name, _hp, maxhp, _mp, maxmp, _str, _agi, _int, _exp, _gold, _age):
        self.is_alive = True
        self.at_home = True
        self.charnb = charnb
        self.title = title
        self.name = name
        self._hp = _hp
        self.maxhp = maxhp
        self._mp = _mp
        self.maxmp = maxmp
        self._str = _str
        self._agi = _agi
        self._int = _int
        self._exp = _exp
        self._gold = _gold
        self._age = _age

    def go_home(self):
        self.at_home = True
        self.restore_hp()
        self.handle_age()

    def restore_hp(self):
        self._hp = self.maxhp

    def handle_age(self, amount=1):
        self._age += amount
        if self._age >= 40:
            self._process_jyumyou()

    def damage(self, amount):
        self._hp -= amount
        if self._hp <= 0:
            self.is_alive = False

    def _process_jyumyou(self):
        print("over40")
        jyumyou = 60
        tenmei = random.randrange(self._age, jyumyou + 1, 1)
        print("tenmei")
        if tenmei == jyumyou:
            print("jyumyou")
            self.is_alive = False
            self._hp = 0

sukesan = MainChar(1, "", "sukesan", 100, 100, 100, 100, 100, 100, 100, 0, 0, 36)
