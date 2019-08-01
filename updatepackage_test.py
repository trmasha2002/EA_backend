import unittest

from models import package

class TestUpdatePackage(unittest.TestCase):
  def test_upper(self):
      self.assertTrue(package.update_package("NewPackage", None, "executable", "2"))


if __name__ == '__main__':
    unittest.main()

