'''
Module for doing weapon comparisons
'''
from compute_unsaved_wound_probability import compute_expected_unsaved_wound_toughness_armor_array

def compare_weapons_across_all_strength_toughness(weapons, skills, 
                                                  base_attacks=None, range=None, penalties=None, 
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
    range (default None) : float
        the range at which the weapons are attacking
        for example for shooting over half range incurs -1 to hit
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
    # 1. compute full_arrays_wounds
    full_arrays_wounds = {}
    for (weapon, skill) in zip(weapons, skills):
        # get the number of attacks
        attacks = 1 # temporary 
        full_arrays_wounds[weapon.name] =\
        compute_expected_unsaved_wound_toughness_armor_array(attacks, skill, 
                                                             weapon.strength, 
                                                             weapon.armor_penetration)

    # 2. compute full_arrays_damage
    # 3. rank full_arrays_wounds
    # 4. rank full_arrays_damage
    results = {}
    results['full_arrays_wounds'] = full_arrays_wounds
    return results



