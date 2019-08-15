import unittest
import logging
import logging.config
from models import connector

class TestAddConnector(unittest.TestCase):
  def test_upper(self):
      logging.config.fileConfig('config/logging.conf')
      logger = logging.getLogger("AddConnector")
      logger.info("Program started")
      self.assertTrue(connector.add_connector("example", "app-link", "12", "13"))
      logger.info("Done")

if __name__ == '__main__':
    unittest.main()

