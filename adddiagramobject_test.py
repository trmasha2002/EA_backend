import unittest

from models import diagramobjects

class TestAddDiagramsObject(unittest.TestCase):
    def test_upper(self):
        self.assertTrue(diagramobjects.add_diagramobjects('100', '101'))


if __name__ == '__main__':
    unittest.main()
