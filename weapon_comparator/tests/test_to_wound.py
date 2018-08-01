import unittest
from to_wound import compute_to_wound_probability

STRENGTH_3 = {
    2: 4.0/6.0,
    3: 3.0/6.0,
    4: 2.0/6.0,
    5: 2.0/6.0,
    6: 1.0/6.0,
    7: 1.0/6.0,
    8: 1.0/6.0,
    9: 1.0/6.0,
    10: 1.0/6.0
}

STRENGTH_4 = {
    2: 5.0/6.0,
    3: 4.0/6.0,
    4: 3.0/6.0,
    5: 2.0/6.0,
    6: 2.0/6.0,
    7: 2.0/6.0,
    8: 1.0/6.0,
    9: 1.0/6.0,
    10: 1.0/6.0
}

STRENGTH_5 = {
    2: 5.0/6.0,
    3: 4.0/6.0,
    4: 4.0/6.0,
    5: 3.0/6.0,
    6: 2.0/6.0,
    7: 2.0/6.0,
    8: 2.0/6.0,
    9: 2.0/6.0,
    10: 1.0/6.0
}

STRENGTH_6 = {
    2: 5.0/6.0,
    3: 5.0/6.0,
    4: 4.0/6.0,
    5: 4.0/6.0,
    6: 3.0/6.0,
    7: 2.0/6.0,
    8: 2.0/6.0,
    9: 2.0/6.0,
    10: 2.0/6.0
}

TEST_STRENGTHS = {
    3 : STRENGTH_3, 
    4 : STRENGTH_4, 
    5 : STRENGTH_5,
    6 : STRENGTH_6
}

class TestToHit(unittest.TestCase):

    def test_strengths(self):
        for strength, strength_probs in TEST_STRENGTHS.iteritems():
            for toughness, prob in strength_probs.iteritems():
                assert compute_to_wound_probability(strength, toughness) == prob

if __name__ == '__main__':
    unittest.main(verbosity=2)