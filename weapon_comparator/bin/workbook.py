from weapon_comparator.compute_unsaved_wound_probability import compute_unsaved_wound_toughness_armor_array


def main():
    skill = '4+'
    strength = 4
    armor_penetration = 0 
    array = compute_unsaved_wound_toughness_armor_array(skill, strength, armor_penetration)
    

if __name__ == '__main__':
    main()