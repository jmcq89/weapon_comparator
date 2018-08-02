'''
Module to store melee weapons
'''
from weapons.base_weapon_class import Weapon

class MeleeWeapon(Weapon):
    ''' base weapon class for ranged weapons'''
    def __init__(self, name, strength, armor_penetration, damage):
        super(MeleeWeapon, self).__init__(name, strength, armor_penetration, damage)

class BonusAttackMeleeWeapon(MeleeWeapon):
    ''' Weapons which give bonus attack(s)'''
    def __init__(self, name, strength, armor_penetration, damage, bonus_attacks):
        super(BonusAttackMeleeWeapon, self).__init__(name, strength, armor_penetration, damage)
        self.bonus_attacks = bonus_attacks

class UnwieldyWeapon(MeleeWeapon):
    ''' Weapons which give penalty to hit'''
    def __init__(self, name, strength, armor_penetration, damage, to_hit_penalty):
        super(UnwieldyWeapon, self).__init__(name, strength, armor_penetration, damage)
        self.to_hit_penalty = to_hit_penalty

class DefensiveWeapon(MeleeWeapon):
    ''' Weapons which grant invulnerable saves '''
    def __init__(self, name, strength, armor_penetration, damage, invulnerable_save):
        super(DefensiveWeapon, self).__init__(name, strength, armor_penetration, damage)
        self.invulnerable_save = invulnerable_save