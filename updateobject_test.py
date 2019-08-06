import unittest

from models import object

class TestUpdateObject(unittest.TestCase):
    def test_upper(self):
        self.assertTrue(object.update_object("NewPackage", "executable", "1"))


if __name__ == '__main__':
    unittest.main()
