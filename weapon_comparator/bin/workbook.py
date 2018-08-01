from weapon_comparator.compute_unsaved_wound_probability import compute_unsaved_wound_toughness_armor_array


def main():
    skill = '4+'
    strength = 4
    armor_penetration = 0 
    array = compute_unsaved_wound_toughness_armor_array(skill, strength, armor_penetration)
    for toughness in array:
        print 'Toughness: {toughness}'.format(toughness=toughness)
        print 'to wound probabilities (for one attack) by armor save:'
        print array[toughness]
        print ''

if __name__ == '__main__':
    main()