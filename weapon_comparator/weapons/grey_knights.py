'''
Storing all Grey Knights Weapons
'''
from melee_weapons import MeleeWeapon, DefensiveWeapon, UnwieldyWeapon, BonusAttackMeleeWeapon
from ranged_weapons import RangedWeapon, AutoHitWeapon, MortalWoundWeapon

# Grey Knight Melee Weapons 
DaemonHammer = UnwieldyWeapon(name='grey_knights_daemon_hammer',
                              strength=8, armor_penetration=-3, damage=3, to_hit_penalty=-1)
Falchions = BonusAttackMeleeWeapon(name='grey_knights_falchions',
                                   strength=4, armor_penetration=-2, damage='D3', bonus_attacks=1)
ForceHalberd = MeleeWeapon(name='grey_knights_force_halberd',
                          strength=5, armor_penetration=-2, damage='D3')
ForceSword = MeleeWeapon(name='grey_knights_force_sword',
                         strength=4, armor_penetration=-3, damage='D3')
WardingStave = DefensiveWeapon(name='grey_knights_warding_stave',
                               strength=6, armor_penetration=-1, damage='D3', 
                               invulnerable_save='5+')

gk_melee_weapons_list = [DaemonHammer, Falchions, ForceHalberd, ForceSword, WardingStave]

# Grey Knights Ranged Weapons
FragGrenade = RangedWeapon(name='grey_knights_frag_grenade',
                           weapon_range=6, weapon_type='Grenade D6',
                           strength=3, armor_penetration=0, damage=1)
Incinerator = AutoHitWeapon(name='grey_knights_incinerator',
                            weapon_range=6, weapon_type='Assault D6',
                            strength=6,armor_penetration=-1,damage=1)
KrakGrenade = RangedWeapon(name='grey_knights_krak_grenade',
                           weapon_range=6, weapon_type='Grenade 1',
                           strength=6, armor_penetration=-1, damage='D3')
Psilencer = RangedWeapon(name='grey_knights_psilencer',
                         weapon_range=24, weapon_type='Heavy 6',
                         strength=4, armor_penetration=0, damage='D3')
Psycannon = RangedWeapon(name='grey_knights_psycannon',
                         weapon_range=24, weapon_type='Heavy 4',
                         strength=7, armor_penetration=-1, damage=1)
PsykOutGrenade = MortalWoundWeapon(name='grey_knights_psyk_out_grenade',
                                   weapon_range=6, weapon_type='Grenade D3',
                                   strength=2, armor_penetration=0, damage=1)
StormBolter = RangedWeapon(name='grey_knights_storm_bolter',
                           weapon_range=24, weapon_type='Rapid Fire 2',
                           strength=4, armor_penetration=0, damage=1)

gk_ranged_weapons_list = [FragGrenade, Incinerator, KrakGrenade, Psilencer, Psycannon, 
                          PsykOutGrenade, StormBolter]
