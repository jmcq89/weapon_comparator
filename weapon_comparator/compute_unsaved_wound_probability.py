'''
Module to compute probability of an unsaved wound
'''

from to_hit import compute_to_hit_probability
from to_wound import compute_to_wound_probability
from to_penetrate_armor import compute_to_penetrate_armor_probability

ALL_TOUGHNESS = range(1,11)
ALL_ARMORS = ['2+', '3+', '4+', '5+', '6+', '7+']

def compute_unsaved_wound_probability(skill, strength, toughness, armor_penetration, armor_save):
    '''
    Return the probability that a single attack/shot will cause an unsaved wound

    Parameters
    -----
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

    Returns
    -------
    probability : float 
        Proability that a single attack/shot will cause an unsaved wound 
    '''
    probability_of_hitting = compute_to_hit_probability(skill)
    probability_of_wounding = compute_to_wound_probability(strength, toughness)
    probability_of_penetrating_armor = compute_to_penetrate_armor_probability(armor_penetration, 
                                                                              armor_save)
    return probability_of_hitting*probability_of_wounding*probability_of_penetrating_armor

def compute_unsaved_wound_toughness_armor_array(skill, strength, armor_penetration):
    '''
    Compute the probability of an unsaved wound for a single attack across all 
    toughness and armor save pairs
    Parameters
    -----
    skill : string
        balistic or weapon skill, in format e.g. '4+'
    strength : int between 1 and 10 
        the strength of the attacking model/weapon
    armor_penetration : int, one of : 0, -1, -2, -3, -4 
        the armor penetration of the attacking weapon 

    Returns
    -------
    probability : dict[toughness][armor] 
        Proability that a single attack/shot will cause an unsaved wound 
    '''
    unsaved_wound_array = {}
    for toughness in ALL_TOUGHNESS:
        unsaved_wound_array[toughness] = {}
        for armor_save in ALL_ARMORS:
            unsaved_wound_array[toughness][armor_save] = compute_unsaved_wound_probability(skill, 
                                         strength, toughness, armor_penetration, armor_save)
    return unsaved_wound_array
