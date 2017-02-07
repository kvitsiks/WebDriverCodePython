import unittest

def test_squirrel_play(temp, is_summer):
    if temp >= 60 and (temp <= 90 or (is_summer and temp <= 100)):
        return True
    else:
        return False

class MyTestCase(unittest.TestCase):
    def test_basic(self):
        self.assertTrue(test_squirrel_play(70, True))

    def test_that_left_border_is_included(self):
        self.assertTrue(test_squirrel_play(60, True))

    def test_right_border_summer(self):
        self.assertTrue(test_squirrel_play(100, True))
        self.assertFalse(test_squirrel_play(100, False))

    def test_right_border_other(self):
        self.assertTrue(test_squirrel_play(90, True))
        self.assertTrue(test_squirrel_play(90, False))

    def test_low_temperature(self):
        self.assertFalse(test_squirrel_play(50, True))
        self.assertFalse(test_squirrel_play(50, False))

    def test_high_temperature(self):
        self.assertFalse(test_squirrel_play(101, True))
        self.assertFalse(test_squirrel_play(101, False))

if __name__ == '__main__':
    unittest.main()
