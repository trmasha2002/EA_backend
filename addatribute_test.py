import unittest
from models import attribute
class TestAddAttribute(unittest.TestCase):
    def test_upper(self):
        self.assertTrue(attribute.add_attribute("first_attibute", "1"))


if __name__ == '__main__':
    unittest.main()
