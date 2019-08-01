import unittest

from models import diagram

class TestAddDiagram(unittest.TestCase):
  def test_upper(self):
      self.assertTrue(diagram.add_diagram("twelve", '6', 'package', 'pac'))


if __name__ == '__main__':
    unittest.main()

