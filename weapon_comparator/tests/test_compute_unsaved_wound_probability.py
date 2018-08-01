import unittest
from compute_unsaved_wound_probability import (compute_unsaved_wound_probability,
                                               compute_unsaved_wound_toughness_armor_array)


class TestWarhammerMath(unittest.TestCase):

    def test_examples(self):
        assert compute_unsaved_wound_probability('3+', 6, 4, -1, '6+') == 4.0/9.0
        assert compute_unsaved_wound_probability('3+', 6, 5, -1, '7+') == 4.0/9.0
        assert compute_unsaved_wound_probability('4+', 4, 8, -4, '3+') == 1.0/12

if __name__ == '__main__':
    unittest.main()