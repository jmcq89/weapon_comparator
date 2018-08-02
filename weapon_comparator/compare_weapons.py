'''
Module for doing weapon comparisons
'''
from weapons.melee_weapons import MeleeWeapon
from weapons.base_weapon_class import get_expected_damage
from weapons.ranged_weapons import RangedWeapon, RANGED_WEAPON_TYPE_TO_ATTACKS_MAP, AutoHitWeapon
from compute_unsaved_wound_probability import (compute_expected_unsaved_wound_toughness_armor_array,
                                               compute_expected_damage_toughness_armor_array)

def adjust_to_hit_params(attacks, auto_hit, distance_penalty, penalties, tactics, buffs):
    # to update when tactics, penalties and buffs are implemented 
    return attacks, auto_hit, distance_penalty

def get_best_weapon_and_rank_string(sorted_values, sorted_keys):
    best_weapon = sorted_keys[0]
    rank_string = best_weapon
    for index in range(1, len(sorted_values)):
        if sorted_values[index] == sorted_values[0]:
            best_weapon += ('=' + sorted_keys[index])
        if sorted_values[index] == sorted_values[index-1]:
            rank_string += ('=' + sorted_keys[index])
        else:
            rank_string += (', ' + sorted_keys[index])
    return best_weapon, rank_string

def rank_arrays(array_dict):
    weapons = array_dict.keys()
    first_keys = array_dict[weapons[0]].keys()
    second_keys = array_dict[weapons[0]][first_keys[0]].keys()
    best_weapons = {}
    ranks = {}
    for first_key in first_keys:
        best_weapons[first_key] = {}
        ranks[first_key] = {}
        for second_key in second_keys:
            values = [] 
            for weapon in weapons:
                values.append(array_dict[weapon][first_key][second_key])
            sort_indices = sorted(range(len(values)),key=values.__getitem__)
            sort_indices = sort_indices[::-1] # we want descending order 
            sorted_weapons = [weapons[index] for index in sort_indices]
            sorted_values = [values[index] for index in sort_indices]
            best_weapon, rank_string = get_best_weapon_and_rank_string(sorted_values, 
                                                                        sorted_weapons)
            best_weapons[first_key][second_key] = best_weapon
            ranks[first_key][second_key] = rank_string

    return best_weapons, ranks

def get_attacks_from_ranged_weapon_type(weapon_type, weapon_range, distance):
    full_range_attacks, half_range_attacks = RANGED_WEAPON_TYPE_TO_ATTACKS_MAP[weapon_type]
    if distance <= weapon_range/2.0 or distance is None:
        distance_penalty = False
        attacks = half_range_attacks
    elif distance > weapon_range:
        attacks = 0
        distance_penalty = True
    else:
        attacks = full_range_attacks
        distance_penalty = True 
    return attacks, distance_penalty


def get_attacks_from_weapon(weapon, base_attacks, distance):
    if isinstance(weapon, MeleeWeapon):
        if distance is not None and distance > 0:
            return 0, False, False 
        if base_attacks is None:
            base_attacks = 1
        if hasattr(weapon, 'bonus_attacks'):
            return base_attacks + weapon.bonus_attacks, False, False
        else:
            return base_attacks, False, False
    elif isinstance(weapon, RangedWeapon):
        if isinstance(weapon, AutoHitWeapon):
            auto_hit = True
        else:
            auto_hit = False
        attacks, distance_penalty = get_attacks_from_ranged_weapon_type(weapon.weapon_type,
                                                                        weapon.weapon_range,
                                                                        distance)
        return attacks, auto_hit, distance_penalty

def compare_weapons_across_all_toughess_armor(weapons, skills, 
                                              base_attacks=None, distance=None, penalties=None, 
                                              tactics=None, buffs=None):
    '''
    Compare input weapons across all Toughness and Armor Save pairs. 

    Rank each weapon in for each pair according to:
        1. Expected number of wounds
        2. Expected damage 

    Parameters
    ----------
    weapons : [list]
        list of Weapon objects from weapon_comparator.weapons
    skills : [list]
        the weapon skill or baslistic skill for each weapon, 
        taken to be all equal if len(skills)==1
    base_attacks : [list]
        for melee weapons the base attacks. 
        taken to be all equal if len(skills)==1
        taken to be 1 if None. 
    distance (default None) : float
        the distance at which the weapons are attacking
        for example for shooting over half distance incurs -1 to hit
        None is taken to mean all weapons (melee and range) hit with no penalties
    penalties (default None) : list of lists
        list of penalties e.g. 'flesh_wound' for each weapon.
        taken to be all equal if len(penalties) == 1 
        so that multiple penalties for all is input as [[penalty1, penalty2]]
    tactics (default None) : list of lists 
        list of tactics e.g. 'Careful Aim' for each weapon.
        taken to be all equal if len(tactics) == 1 
        so that multiple tactics for all is input as [[tactic1, tactic2]]
    buffs (default None) : list of lists 
        list of buffs e.g. 'recon suite' for each weapon.
        taken to be all equal if len(buffs) == 1 
        so that multiple buffs for all is input as [[buff1, buff2]]

    Output
    -------
    results : (dict)
        keys : 
        best_weapon_wounds : dict[toughness][armor_save]
            for each T/AS pair the best weapon from the input weapons 
            by expected number of wounds
        best_weapon_damage : dict[toughness][armor_save]
            for each T/AS pair the best weapon from the input weapons 
            by expected damage
        full_ranks_wounds : dict[toughness][armor_save]
            for each T/AS pair the full ordered list of the input weapons 
            by expected number of wounds
        full_ranks_damage : dict[toughness][armor_save]
            for each T/AS pair the full ordered list of the input weapons 
            by expected damage 
        full_arrays_wounds : dict[weapon_name][tougness][armor_save]
            full expected number of wounds array for each weapon 
        full_arrays_damage : dict[weapon_name][tougness][armor_save]
            full expected damage array for each weapon 
    '''
    full_arrays_wounds = {}
    full_arrays_damage = {}
    if len(skills) == 1:
        skills = [skills[0]]*len(weapons)
    for (weapon, skill) in zip(weapons, skills):
        attacks, auto_hit, distance_penalty = get_attacks_from_weapon(weapon, base_attacks, 
                                                                      distance)
        attacks, auto_hit, distance_penalty = adjust_to_hit_params(attacks, auto_hit, 
                                                                   distance_penalty,
                                                                   penalties,
                                                                   tactics,
                                                                   buffs)
        # 1. compute full_arrays_wounds
        full_arrays_wounds[weapon.name] =\
        compute_expected_unsaved_wound_toughness_armor_array(attacks, skill, 
                                                             weapon.strength, 
                                                             weapon.armor_penetration,
                                                             auto_hit=auto_hit,
                                                             distance_penalty=distance_penalty,
                                                             weapon=weapon,
                                                             penalties=penalties,
                                                             tactics=tactics,
                                                             buffs=buffs)

        # 2. compute full_arrays_damage
        damage = get_expected_damage(weapon.damage)
        full_arrays_damage[weapon.name] =\
        compute_expected_damage_toughness_armor_array(attacks, damage, skill, 
                                                      weapon.strength, 
                                                      weapon.armor_penetration,
                                                      auto_hit=auto_hit,
                                                      distance_penalty=distance_penalty,
                                                      weapon=weapon,
                                                      penalties=penalties,
                                                      tactics=tactics,
                                                      buffs=buffs)

    # 3. rank full_arrays_wounds
    array_wound_best, array_wound_ranks = rank_arrays(full_arrays_wounds)
    # 4. rank full_arrays_damage
    array_damage_best, array_damage_ranks = rank_arrays(full_arrays_damage)
    # 5. Store Results
    results = {}
    results['full_arrays_wounds'] = full_arrays_wounds
    results['full_arrays_damage'] = full_arrays_damage
    results['array_wound_best'] = array_wound_best
    results['array_wound_ranks'] = array_wound_ranks
    results['array_damage_best'] = array_damage_best
    results['array_damage_ranks'] = array_damage_ranks
    return results



