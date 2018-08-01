'''
Module for computing to wound probability
'''

def compute_to_wound_probability(strength, toughness):
    '''
    Return the probability that a single hit will wound

    Parameters
    -----
    strength : int between 1 and 10 
        the strength of the attacking model/weapon
    toughness : int between 1 and 10 
        the toughness of the defending model
    Returns
    -------
    probability : float 
        Proability that a single hit will wound 
    '''
    if strength == toughness:
        return 0.5 
    elif strength > toughness:
        if strength >= toughness*2:
            return 5.0/6.0
        else:
            return 4.0/6.0
    else:
        if strength <= toughness/2.0:
            return 1.0/6.0
        else:
            return 2.0/6.0
