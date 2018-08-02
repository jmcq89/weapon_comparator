import unittest
from weapons.base_weapon_class import WEAPON_DAMAGE_HASH
from weapons.ranged_weapons import RANGED_WEAPON_TYPE_TO_ATTACKS_MAP

class TestImport(unittest.TestCase):
    def setup_method(self, test_method):
        self.all_weapons = []
        self.melee_weapons = []
        self.ranged_weapons = []
        try:
            from weapons import grey_knights
            self.all_weapons.extend(grey_knights.gk_melee_weapons_list)
            self.melee_weapons.extend(grey_knights.gk_melee_weapons_list)
            self.all_weapons.extend(grey_knights.gk_ranged_weapons_list)
            self.ranged_weapons.extend(grey_knights.gk_ranged_weapons_list)
        except:
            pass

    def test_import_grey_knights_weapons(self):
        from weapons import grey_knights
        assert True

    def test_names_are_unique(self):
        weapon_names = []
        for weapon in self.all_weapons:
            weapon_names.append(weapon.name)
        unique_names = list(set(weapon_names))
        assert len(unique_names) == len(weapon_names)

    def test_all_ranged_weapon_types_in_hash(self):
        for ranged_weapon in self.ranged_weapons:
            assert ranged_weapon.weapon_type in RANGED_WEAPON_TYPE_TO_ATTACKS_MAP

    def test_all_damage_types_in_hash(self):
        for weapon in self.all_weapons:
            assert weapon.damage in WEAPON_DAMAGE_HASH

if __name__ == '__main__':
    unittest.main()