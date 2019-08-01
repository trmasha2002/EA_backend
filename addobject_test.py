import unittest

from models import object

class TestAddObject(unittest.TestCase):
    def test_upper(self):
        self.assertTrue(object.add_object("example", "example", "example", "1", "1"))


if __name__ == '__main__':
    unittest.main()
