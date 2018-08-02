import unittest

class TestImport(unittest.TestCase):

    def test_import_grey_knights_weapons(self):
        from weapons import grey_knights
        assert True

if __name__ == '__main__':
    unittest.main()