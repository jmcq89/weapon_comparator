'''
Storing all Grey Knights Weapons
'''
from melee_weapons import MeleeWeapon, DefensiveWeapon, UnwieldyWeapon, BonusAttackMeleeWeapon
from ranged_weapons import RangedWeapon, AutoHitWeapon, MortalWoundWeapon

# Grey Knight Melee Weapons 
DaemonHammer = UnwieldyWeapon(strength=8, armor_penetration=-3, damage=3, to_hit_penalty=-1)
Falchions = BonusAttackMeleeWeapon(strength=5, armor_penetration=-2, damage='D3', bonus_attacks=1)
ForceHalberd = MeleeWeapon(strength=5, armor_penetration=-2, damage='D3')
ForceSword = MeleeWeapon(strength=4, armor_penetration=-3, damage='D3')
WardingStave = DefensiveWeapon(strength=6, armor_penetration=-1, damage='D3', invulnerable_save='5+')

# Grey Knights Ranged Weapons
FragGrenade = RangedWeapon(weapon_range=6, weapon_type='Grenade D6',
                           strength=3, armor_penetration=0, damage=1)
Incinerator = AutoHitWeapon(weapon_range=6, weapon_type='Assault D6',
                            strength=6,armor_penetration=-1,damage=1)
KrakGrenade = RangedWeapon(weapon_range=6, weapon_type='Grenade 1',
                           strength=6, armor_penetration=-1, damage='D3')
Psilencer = RangedWeapon(weapon_range=24, weapon_type='Heavy 6',
                         strength=4, armor_penetration=0, damage='D3')
Psycannon = RangedWeapon(weapon_range=24, weapon_type='Heavy 4',
                         strength=7, armor_penetration=-1, damage=1)
PsykOutGrenade = MortalWoundWeapon(weapon_range=6, weapon_type='Grenade D3',
                                   strength=2, armor_penetration=0, damage=1)
StormBolter = RangedWeapon(weapon_range=24, weapon_type='Rapid Fire 2',
                           strength=4, armor_penetration=0, damage=1)
