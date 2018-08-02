from weapon_comparator.compare_weapons import compare_weapons_across_all_toughess_armor
from weapon_comparator.weapons.grey_knights import (Psilencer, Psycannon, Incinerator, StormBolter,
                                                    ForceHalberd, ForceSword, WardingStave, 
                                                    Falchions, DaemonHammer)

def print_sorted_armor_string(dictionary):
    sorted_keys = sorted(dictionary)
    components = []
    for key in sorted_keys:
        component = key + ': ' + dictionary[key]
        components.append(component)
    return ', '.join(components)

def main():
    skill = '4+'
    weapons = [ForceHalberd, ForceSword, WardingStave, Falchions, DaemonHammer]
    #weapons = [Psycannon, Psilencer, StormBolter]
    results = compare_weapons_across_all_toughess_armor(weapons, [skill])

    wounds = False
    if wounds:
        array = 'array_wound_ranks'
    else:
        array = 'array_damage_ranks'

    print '\n'
    print 'comparing: {weapons}'.format(weapons=', '.join([weapon.name for weapon in weapons]))
    print '\n'
    if wounds:
        print 'All Ranks by Expected Number of Wounds:'
    else:
        print 'All Ranks by Expected Number of Damage:'
    for toughness in range(2,6):
        print 'Toughness: {T}    \n'.format(T=toughness)
        for armorsave in ['3+', '4+', '5+', '6+', '7+']:
                print "* " + armorsave + "  " + results[array][toughness][armorsave] + "    "

if __name__ == '__main__':
    main()