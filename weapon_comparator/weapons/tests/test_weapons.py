import unittest

class TestImport(unittest.TestCase):

    def test_import_grey_knights_weapons(self):
        from weapons import grey_knights
        assert True

    def test_names_are_unique(self):
        all_weapons = []
        try:
            from weapons import grey_knights
            all_weapons.extend(grey_knights.gk_melee_weapons_list)
            all_weapons.extend(grey_knights.gk_ranged_weapons_list)
        except:
            pass
        weapon_names = []
        for weapon in all_weapons:
            weapon_names.append(weapon.name)
        unique_names = list(set(weapon_names))
        assert len(unique_names) == len(weapon_names)

if __name__ == '__main__':
    unittest.main()