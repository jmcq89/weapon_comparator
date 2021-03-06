'''
Module to compute probability of an unsaved wound and expected number of unsaved wounds
'''

from to_hit import compute_to_hit_probability
from to_wound import compute_to_wound_probability
from to_penetrate_armor import compute_to_penetrate_armor_probability

ALL_TOUGHNESS = range(1,11)
ALL_ARMORS = ['2+', '3+', '4+', '5+', '6+', '7+']

def _compute_over_T_S_array(function, **kwargs):
    array = {}
    for toughness in ALL_TOUGHNESS:
        array[toughness] = {}
        for armor_save in ALL_ARMORS:
            array[toughness][armor_save] = function(toughness=toughness, armor_save=armor_save,
                                                    **kwargs)
    return array 

def compute_unsaved_wound_probability(skill, strength, toughness, armor_penetration, armor_save, 
                                      auto_hit=False, distance_penalty=False, weapon=None,
                                      penalties=None, tactics=None, buffs=None):
    '''
    Return the probability that a single attack/shot will cause an unsaved wound

    Parameters
    ----------
    skill : string
        balistic or weapon skill, in format e.g. '4+'
    strength : int between 1 and 10 
        the strength of the attacking model/weapon
    toughness : int between 1 and 10 
        the toughness of the defending model
    armor_penetration : int, one of : 0, -1, -2, -3, -4 
        the armor penetration of the attacking weapon 
    armor_save : string, e.g. '4+'
        the armor save of the defending model
    auto_hit : bool,
        if the attack automatically hits
    distance_penalty : bool,
        if there is a -1 to hit distance penalty in play 

    TO IMPLEMENT: 
    weapon : weapon_comparator.weapons.Weapon object
        if special properties exist for the weapon 
    penalties : list
        if there are any penalties in play list them here 
    tactics : list 
        if there are any tactics in play list them here
    buffs : list 
        if there are any buffs in play list them here 


    Returns
    -------
    probability : float 
        Proability that a single attack/shot will cause an unsaved wound 

    To Do:
        * Incorporate penalties
        * Incorporate tactics
        * Incorporate buffs 
    '''
    probability_of_hitting = compute_to_hit_probability(skill, auto_hit, distance_penalty)
    probability_of_wounding = compute_to_wound_probability(strength, toughness)
    probability_of_penetrating_armor = compute_to_penetrate_armor_probability(armor_penetration, 
                                                                              armor_save)
    return probability_of_hitting*probability_of_wounding*probability_of_penetrating_armor

def compute_unsaved_wound_toughness_armor_array(skill, strength, armor_penetration, 
                                                auto_hit=False, distance_penalty=False,
                                                weapon=None, penalties=None,
                                                tactics=None, buffs=None):
    '''
    Compute the probability of an unsaved wound for a single attack across all 
    toughness and armor save pairs

    Parameters
    ----------
    see compute_unsaved_wound_probability for parameters

    Returns
    -------
    probability : dict[toughness][armor] 
        Proability that a single attack/shot will cause an unsaved wound over all toughness
        and armor save pairs. 
    '''
    return _compute_over_T_S_array(compute_unsaved_wound_probability,
                                   skill=skill, 
                                   strength=strength, 
                                   armor_penetration=armor_penetration,
                                   auto_hit=auto_hit,
                                   distance_penalty=distance_penalty,
                                   weapon=weapon,
                                   penalties=penalties,
                                   tactics=tactics,
                                   buffs=buffs)

def compute_expected_number_of_unsaved_wounds(attacks, skill, strength, toughness, 
                                              armor_penetration, armor_save,
                                              auto_hit=False, distance_penalty=False,
                                              weapon=None, penalties=None, tactics=None,
                                              buffs=None):
    '''
    Return the expected number of unsaved wounds for given number of attacks/shots

    Parameters
    ----------
    attacks : int 
        number of attacks or shots from a weapon

    see compute_unsaved_wound_probability for remaining parameters 

    Returns
    -------
    probability : float 
        Expected number of unsaved wounds caused by the given number of attacks/shots
    '''
    return attacks*compute_unsaved_wound_probability(skill, strength, toughness, 
                                                     armor_penetration, armor_save,
                                                     auto_hit=auto_hit,
                                                     distance_penalty=distance_penalty,
                                                     weapon=weapon,
                                                     penalties=penalties,
                                                     tactics=tactics,
                                                     buffs=buffs)

def compute_expected_unsaved_wound_toughness_armor_array(attacks, skill, strength, 
                                                         armor_penetration,
                                                         auto_hit=False, distance_penalty=False,
                                                         weapon=None, penalties=None, tactics=None,
                                                         buffs=None):
    '''
    Compute the expected number of unsaved wounds for a given number of attacks across all 
    toughness and armor save pairs

    Parameters
    ----------
    attacks : int 
        number of attacks or shots from a weapon

    see compute_unsaved_wound_probability for remaining parameters 

    Returns
    -------
    expected_unsaved_wounds : dict[toughness][armor] 
        Expected number of unsaved wounds caused by the given number of attacks/shots
        over all toughness and armor save pairs. 
    '''
    return _compute_over_T_S_array(compute_expected_number_of_unsaved_wounds,
                                   attacks=attacks, 
                                   skill=skill, 
                                   strength=strength, 
                                   armor_penetration=armor_penetration,
                                   auto_hit=auto_hit,
                                   distance_penalty=distance_penalty,
                                   weapon=weapon,
                                   penalties=penalties,
                                   tactics=tactics,
                                   buffs=buffs)

def compute_expected_damage(attacks, damage, skill, strength, toughness, 
                            armor_penetration, armor_save,
                            auto_hit=False, distance_penalty=False,
                            weapon=None, penalties=None, tactics=None,
                            buffs=None):
    '''
    Return the expected number of unsaved wounds for given number of attacks/shots

    Parameters
    ----------
    attacks : int 
        number of attacks or shots from a weapon
    damage : float
        expected (i.e. average) damage for the attack. E.g. 1 for D=1, but 2 for D=D3

    see compute_unsaved_wound_probability for remaining parameters 

    Returns
    -------
    probability : float 
        Expected (unsaved) Damage caused by the given number of attacks/shots
    '''
    return attacks*damage*compute_unsaved_wound_probability(skill, strength, toughness, 
                                                            armor_penetration, armor_save,
                                                            auto_hit=auto_hit,
                                                            distance_penalty=distance_penalty,
                                                            weapon=weapon,
                                                            penalties=penalties,
                                                            tactics=tactics,
                                                            buffs=buffs)

def compute_expected_damage_toughness_armor_array(attacks, damage, skill, strength, 
                                                  armor_penetration,
                                                  auto_hit=False, distance_penalty=False,
                                                  weapon=None, penalties=None, tactics=None,
                                                  buffs=None):
    '''
    Compute the expected number of unsaved wounds for a given number of attacks across all 
    toughness and armor save pairs

    Parameters
    ----------
    attacks : int 
        number of attacks or shots from a weapon

    see compute_unsaved_wound_probability for remaining parameters 

    Returns
    -------
    expected_unsaved_wounds : dict[toughness][armor] 
        Expected (unsaved) Damage caused by the given number of attacks/shots
        over all toughness and armor save pairs. 
    '''
    return _compute_over_T_S_array(compute_expected_damage,
                                   attacks=attacks, 
                                   damage=damage,
                                   skill=skill, 
                                   strength=strength, 
                                   armor_penetration=armor_penetration,
                                   auto_hit=auto_hit,
                                   distance_penalty=distance_penalty,
                                   weapon=weapon,
                                   penalties=penalties,
                                   tactics=tactics,
                                   buffs=buffs)

