import unittest
from warhammer_math import round_up


class TestWarhammerMath(unittest.TestCase):

    def test_round_up(self):
        assert str(round_up(9, 2)) == '5'
        assert str(round_up(5, 2)) == '3'
        assert str(round_up(3, 2)) == '2'
        assert str(round_up(10, 3)) == '4'

if __name__ == '__main__':
    unittest.main()