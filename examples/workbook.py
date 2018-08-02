from weapon_comparator.compare_weapons import compare_weapons_across_all_toughess_armor
from weapon_comparator.weapons.grey_knights import Psilencer, Psycannon, Incinerator
from weapon_comparator.compute_unsaved_wound_probability import ALL_TOUGHNESS, ALL_ARMORS

def print_sorted_armor_string(dictionary):
    sorted_keys = sorted(dictionary)
    components = []
    for key in sorted_keys:
        component = key + ': ' + dictionary[key]
        components.append(component)
    return ', '.join(components)

def main():
    skill = '4+'
    weapons = [Psycannon, Psilencer]
    results = compare_weapons_across_all_toughess_armor(weapons, [skill])

    print '\n'
    print 'comparing: {weapons}'.format(weapons=', '.join([weapon.name for weapon in weapons]))
    print '\n'
    print 'Best Weapon by wounds:'
    for toughness in range(2,6):
        print 'Toughness: {toughness}'.format(toughness=toughness)
        del results['array_wound_best'][toughness]['2+']
        print print_sorted_armor_string(results['array_wound_best'][toughness])
    print '\n'
    print '------------\n'
    print 'Best Weapon by Damage:'
    for toughness in range(2,6):
        print 'Toughness: {toughness}'.format(toughness=toughness)
        del results['array_damage_best'][toughness]['2+']
        print print_sorted_armor_string(results['array_damage_best'][toughness])
    print '\n'

if __name__ == '__main__':
    main()