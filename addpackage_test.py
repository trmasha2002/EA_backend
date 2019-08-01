import unittest

from models import package

class TestAddPackage(unittest.TestCase):
  def test_upper(self):
      self.assertTrue(package.add_package("Test", None, None, "Package", "1"))


if __name__ == '__main__':
    unittest.main()

