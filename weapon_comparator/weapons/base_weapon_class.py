'''
Base class for all weapons
'''

class Weapon(object):
    def __init__(self, name, strength, armor_penetration, damage):
        self.name = name
        self.strength = strength
        self.armor_penetration = armor_penetration
        self.damage = damage