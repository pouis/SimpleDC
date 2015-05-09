import unittest

import main


class DummyEvent(object):
    pass


class MapTest(unittest.TestCase):
  def test_empty(self):
      m = main.Map('foo', [
      ])
      assert m.is_empty

  def test_pop(self):
      m = main.Map('foo', [
          (DummyEvent, 2)
      ])
      assert not m.is_empty

      ev1 = m.pop_random_event()
      assert isinstance(ev1, DummyEvent)
      assert not m.is_empty

      ev2 = m.pop_random_event()
      assert isinstance(ev2, DummyEvent)
      assert m.is_empty


if __name__ == '__main__':
    unittest.main()
