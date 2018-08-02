import unittest
from compare_weapons import compare_weapons_across_all_strength_toughness
from weapons.grey_knights import StormBolter
from compute_unsaved_wound_probability import ALL_TOUGHNESS, ALL_ARMORS

class TestCompareWeapons(unittest.TestCase):
    def test_array_sizes(self):
        weapons = [StormBolter]
        def assert_array_keys_are_valid(base_array, weapons):
            assert set(base_array.keys()) == set([weapon.name for weapon in weapons])
            for _,array in base_array.iteritems():
                assert set(array.keys()) == set(ALL_TOUGHNESS)
                for _,subdict in array.iteritems():
                    assert set(subdict.keys()) == set(ALL_ARMORS)
        results = compare_weapons_across_all_strength_toughness(weapons, ['4+'])
        assert_array_keys_are_valid(results['full_arrays_wounds'], weapons)

if __name__ == '__main__':
    unittest.main()