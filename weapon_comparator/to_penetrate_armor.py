'''
Module for computing to penetrate armor save probability 
'''

def compute_to_penetrate_armor_probability(armor_penetration, armor_save):
    '''
    Return the probability that a single wound will penetrate armor 

    Parameters
    -----
    armor_penetration : int, one of : 0, -1, -2, -3, -4 
        the armor penetration of the attacking weapon 
    armor_save : string, e.g. '4+'
        the armor save of the defending model
    Returns
    -------
    probability : float 
        Proability that a single wound will penetrate armor 
    '''
    armor = float(armor_save.strip('+'))
    return max(1.0/6.0, min((armor-armor_penetration-1)/6.0,1.0))