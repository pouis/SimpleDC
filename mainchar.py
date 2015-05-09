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


sukesan = MainChar(1, "", "sukesan", 100, 100, 100, 100, 100, 100, 100, 0, 0, 36)
