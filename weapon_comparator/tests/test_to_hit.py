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

def compute_distance_penalty(current_to_hit, penalty):
    save = int(current_to_hit.strip('+'))
    next_to_hit = save + penalty
    if next_to_hit > 10:
        next_to_hit = 10
    if next_to_hit < 0:
        next_to_hit = 10
    return str(next_to_hit) + '+'


class TestToHit(unittest.TestCase):

    def test_kill_team_to_hits(self):
        for skill, prob in KT_TO_HIT_DICTIONARY.iteritems():
            assert compute_to_hit_probability(skill) == prob

    def test_auto_hit(self):
        assert compute_to_hit_probability('0+', auto_hit=True) == 1.0 

    def test_distance_penalty(self):
        for skill, prob in KT_TO_HIT_DICTIONARY.iteritems():
            penalized_skill = compute_distance_penalty(skill, 1)
            assert compute_to_hit_probability(skill, 
                                              distance_penalty=True) ==\
                                               KT_TO_HIT_DICTIONARY[penalized_skill]


if __name__ == '__main__':
    unittest.main()