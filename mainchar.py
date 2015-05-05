class MainChar:
    """common base class for all main characters"""
    def __init__(self, charnb, title, name, _hp, maxhp, _mp, maxmp, _str, _agi, _int):
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


sukesan = MainChar(1, "", "sukesan", 100, 100, 100, 100, 100, 100, 100)
