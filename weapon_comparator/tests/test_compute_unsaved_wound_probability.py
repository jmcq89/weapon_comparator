import unittest
from compute_unsaved_wound_probability import (compute_unsaved_wound_probability,
                                               compute_unsaved_wound_toughness_armor_array,
                                               compute_expected_unsaved_wound_toughness_armor_array,
                                               ALL_TOUGHNESS,
                                               ALL_ARMORS)


class TestWarhammerMath(unittest.TestCase):

    def test_examples(self):
        assert compute_unsaved_wound_probability('3+', 6, 4, -1, '6+') == 4.0/9.0
        assert compute_unsaved_wound_probability('3+', 6, 5, -1, '7+') == 4.0/9.0
        assert compute_unsaved_wound_probability('4+', 4, 8, -4, '3+') == 1.0/12

    def test_arrays(self):
        def assert_array_keys_are_valid(array):
            assert set(array.keys()) == set(ALL_TOUGHNESS)
            for _,subdict in array.iteritems():
                assert set(subdict.keys()) == set(ALL_ARMORS)
        assert_array_keys_are_valid(compute_unsaved_wound_toughness_armor_array('4+', 3, -1))
        assert_array_keys_are_valid(compute_expected_unsaved_wound_toughness_armor_array(3, '4+', 
                                                                                         3, -1))


if __name__ == '__main__':
    unittest.main()