'''
Base class for all weapons
'''

WEAPON_DAMAGE_HASH = {
    1 : 1,
    2 : 2,
    3 : 3,
    4 : 4,
    5 : 5,
    6 : 6,
    'D3' : 2,
    'D6' : 3.5
}

def get_expected_damage(damage_string):
    return WEAPON_DAMAGE_HASH[damage_string]
    
class Weapon(object):
    def __init__(self, name, strength, armor_penetration, damage):
        self.name = name
        self.strength = strength
        self.armor_penetration = armor_penetration
        self.damage = damage