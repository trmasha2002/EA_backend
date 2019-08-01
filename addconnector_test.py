import unittest

from models import connector

class TestAddConnector(unittest.TestCase):
  def test_upper(self):
      self.assertTrue(connector.add_connector("example", "app-link", "12", "13"))


if __name__ == '__main__':
    unittest.main()

