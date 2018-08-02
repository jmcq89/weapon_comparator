import unittest
from to_penetrate_armor import compute_to_penetrate_armor_probability

ARMOR_SAVES = {
    '2+' : 1.0/6.0,
    '3+' : 2.0/6.0,
    '4+' : 3.0/6.0,
    '5+' : 4.0/6.0,
    '6+' : 5.0/6.0,
    '7+' : 1.0 
}
TEST_AP = [0, -1, -2, -3, -4]

def compute_save_difference(current_save, penetration):
    save = int(current_save.strip('+'))
    next_save = save - penetration
    if next_save > 7:
        next_save = 7
    if next_save < 2:
        next_save = 2
    return str(next_save) + '+'

class TestWarhammerMath(unittest.TestCase):

    def test_no_armor_penetration(self):
        # no armor penetration 
        for armor_save, probability in ARMOR_SAVES.iteritems():
            assert compute_to_penetrate_armor_probability(0, armor_save) == probability

    def test_ap(self):
        def get_armor_save_from_dictionary(armor_penetration, armor_save):
            next_save = compute_save_difference(armor_save, armor_penetration)
            return ARMOR_SAVES[next_save]

        for armor_penetration in TEST_AP:
            for armor_save in ARMOR_SAVES:
                assert compute_to_penetrate_armor_probability(armor_penetration,\
                       armor_save) == get_armor_save_from_dictionary(armor_penetration, armor_save)

if __name__ == '__main__':
    unittest.main()