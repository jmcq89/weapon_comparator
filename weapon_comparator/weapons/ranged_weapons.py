'''
Module to store ranged weapons
'''
from base_weapon_class import Weapon

RANGED_WEAPON_TYPE_TO_ATTACKS_MAP = {
    'Rapid Fire 1' : (1, 2), 
    'Rapid Fire 2' : (2, 4),
    'Assault D6'   : (3.5, 3.5),
    'Heavy 6'      : (6, 6),
    'Heavy 4'      : (4, 4),
    'Grenade D6'   : (3.5, 3.5),
    'Grenade D3'   : (2, 2),
    'Grenade 1'    : (1, 1)
}

class RangedWeapon(Weapon):
    ''' base weapon class for ranged weapons'''
    def __init__(self, name, weapon_range, weapon_type, strength, armor_penetration, damage):
        super(RangedWeapon, self).__init__(name, strength, armor_penetration, damage)
        self.weapon_range = weapon_range
        self.weapon_type = weapon_type

class AutoHitWeapon(RangedWeapon):
    ''' Weapons which auto hit'''
    def __init__(self, name, weapon_range, weapon_type, strength, armor_penetration, damage):
        super(AutoHitWeapon, self).__init__(name, weapon_range, weapon_type, strength, 
                                             armor_penetration, damage)
        self.auto_hit = True

class MortalWoundWeapon(RangedWeapon):
    ''' Weapons which cause mortal wound(s) under certain conditions
    Additional Parameters
    ---------------------
    roll_condition (default 6+) : 
        what roll is required to trigger mortal round 
    num_mortal_wounds (default 1) : 
        how many mortal wounds are caused
    target_condition (default None) : 
        If the target must be of a particular type e.g, ['Psyker', 'Daemon']
    replaces_wound (default True) : 
        If the moral wound occurs instead of the original wound

    '''
    def __init__(self, name, weapon_range, weapon_type, strength, armor_penetration, damage,
                 roll_condition='6+', num_mortal_wounds=1,target_condition=None, 
                 replaces_wound=True):
        super(MortalWoundWeapon, self).__init__(name, weapon_range, weapon_type, strength, 
                                                armor_penetration, damage)
        self.roll_condition = roll_condition
        self.num_mortal_wounds = num_mortal_wounds
        self.target_condition = target_condition 
        self.replaces_wound = replaces_wound