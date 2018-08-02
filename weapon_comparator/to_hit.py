'''
Module for computing to hit probability
'''

def compute_to_hit_probability(skill, auto_hit=False, distance_penalty=False):
    '''
    Return the probability that a single attack/shot will hit

    Parameters
    -----
    skill : string
        balistic or weapon skill, in format e.g. '4+'

    Returns
    -------
    probability : float 
        Proability that a single attack/shot will hit
    '''
    if auto_hit:
        return 1.0
    numeric_skill = float(skill.strip('+'))
    if distance_penalty:
        numeric_skill += 1
    probability = (7.0-numeric_skill)/6.0 
    probability = min(probability, 5.0/6.0) # 1s always miss
    probability = max(probability, 1.0/6.0) # 6s always hit 
    return probability