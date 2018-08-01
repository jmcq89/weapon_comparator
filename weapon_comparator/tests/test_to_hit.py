import unittest
from to_hit import compute_to_hit_probability

KT_TO_HIT_DICTIONARY = {
    '0+' : 5.0/6.0,
    '1+' : 5.0/6.0,
    '2+' : 5.0/6.0,
    '3+' : 4.0/6.0,
    '4+' : 3.0/6.0,
    '5+' : 2.0/6.0,
    '6+' : 1.0/6.0,
    '7+' : 1.0/6.0,
    '8+' : 1.0/6.0,
    '9+' : 1.0/6.0,
    '10+' : 1.0/6.0
}

class TestToHit(unittest.TestCase):

    def test_kill_team_to_hits(self):
        for skill, prob in KT_TO_HIT_DICTIONARY.iteritems():
            assert compute_to_hit_probability(skill) == prob

if __name__ == '__main__':
    unittest.main()