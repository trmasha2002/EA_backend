import unittest
import logging
import logging.config
from models import connector

class TestAddConnector(unittest.TestCase):
  def test_upper(self):
      logging.config.fileConfig('config/logging.conf')
      logger = logging.getLogger("Connector")
      logger.info("Program started")
      self.assertTrue(connector.add_connector("example", "app-link", "12", "13"))
      logger.info("Done!")

class TestUpdateConnector(unittest.TestCase):
    def test_upper(self):
        logging.config.fileConfig('config/logging.conf')
        logger = logging.getLogger("Connector")
        logger.info("Program started")
        self.assertTrue(connector.update_by_ea_guid("{5f68b72c-d02f-4ef0-8040-89ea827f0e20}", "second", "app", "13", "14"))
        logger.info("Done!")

class TestDeleteConnector(unittest.TestCase):
    def test_upper(self):
        logging.config.fileConfig("config/logging.conf")
        logger = logging.getLogger("Connector")
        logger.info("Program started")
        self.assertTrue(connector.delete_by_ea_guid("{782640db-1230-4c7f-adf2-b3edc3d318e8}"))
        logger.info("Done!")
if __name__ == '__main__':
    unittest.main()

