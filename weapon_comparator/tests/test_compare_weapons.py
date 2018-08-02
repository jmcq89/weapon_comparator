import unittest
from compare_weapons import compare_weapons_across_all_toughess_armor,rank_arrays
from weapons.grey_knights import StormBolter
from compute_unsaved_wound_probability import ALL_TOUGHNESS, ALL_ARMORS


class TestCompareWeapons(unittest.TestCase):

    def setup_method(self, test_method):
        weapon_one_array = {
            2 : {
                '3+':0.1,
                '4+':0.2
            },
            3 : {
                '3+':0.03,
                '4+':0.4
            }
        }
        weapon_two_array = {
            2 : {
                '3+':0.01,
                '4+':0.1
            },
            3 : {
                '3+':0.3,
                '4+':0.01
            }
        }
        weapon_three_array = {
            2 : {
                '3+':0.2,
                '4+':0.1
            },
            3 : {
                '3+':0.00,
                '4+':0.4
            }
        }
        self.arrays = {'weapon_1':weapon_one_array,
                       'weapon_2':weapon_two_array,
                       'weapon_3':weapon_three_array}
        self.best_weapons = {
            2 : {
                '3+':'weapon_3',
                '4+':'weapon_1'
            },
            3 : {
                '3+':'weapon_2',
                '4+':'weapon_3=weapon_1'
            }
        }
        self.ranks = {
            2 : {
                '3+':'weapon_3, weapon_1, weapon_2',
                '4+':'weapon_1, weapon_2=weapon_3'
            },
            3 : {
                '3+':'weapon_2, weapon_1, weapon_3',
                '4+':'weapon_3=weapon_1, weapon_2'
            }
        }

    def test_best_weapons_array(self):
        best_weapons, ranks = rank_arrays(self.arrays)
        assert best_weapons == self.best_weapons

    def test_ranks_array(self):
        best_weapons, ranks = rank_arrays(self.arrays)
        assert ranks == self.ranks

    def test_array_sizes(self):
        weapons = [StormBolter]

        def assert_array_keys_are_valid(base_array, weapons):
            assert set(base_array.keys()) == set([weapon.name for weapon in weapons])
            for _,array in base_array.iteritems():
                assert set(array.keys()) == set(ALL_TOUGHNESS)
                for _,subdict in array.iteritems():
                    assert set(subdict.keys()) == set(ALL_ARMORS)
                    
        results = compare_weapons_across_all_toughess_armor(weapons, ['4+'])
        assert_array_keys_are_valid(results['full_arrays_wounds'], weapons)
        assert_array_keys_are_valid(results['full_arrays_damage'], weapons)

if __name__ == '__main__':
    unittest.main()