'''
Base class for all weapons
'''

class Weapon(object):
    def __init__(self, strength, armor_penetration, damage):
        self.strength = strength
        self.armor_penetration = armor_penetration
        self.damage = damage