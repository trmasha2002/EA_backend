import unittest
import logging
import logging.config
from models import package
class TestAddPackage(unittest.TestCase):
  def test_upper(self):
      logging.config.fileConfig('config/logging.conf')
      logger = logging.getLogger("Package")
      logger.info("Program started")
      self.assertTrue(package.add_package("Test", None, None, "Package", "1"))
      logger.info("Done!")

class TestUpdatePackage(unittest.TestCase):
    def test_upper(self):
        logging.config.fileConfig('config/logging.conf')
        logger = logging.getLogger("Package")
        logger.info("Program started")
        self.assertTrue(package.update_package("NewPackage", None, "executable", "2"))
        logger.info("Done!")

class DeletePackage(unittest.TestCase):
    def test_upper(self):
        logging.config.fileConfig('config/logging.conf')
        logger = logging.getLogger("Package")
        logger.info("Program started")
        self.assertTrue(package.delete_by_ea_guid("89452"))
        logger.info("Done!")
if __name__ == '__main__':
    unittest.main()


