import unittest
import logging
import logging.config
from models import package

class TestUpdatePackage(unittest.TestCase):
  def test_upper(self):
      logging.config.fileConfig('config/logging.conf')
      logger = logging.getLogger("UpdatePackage")
      logger.info("Program started")
      self.assertTrue(package.update_package("NewPackage", None, "executable", "2"))
      logger.info("Done!")

if __name__ == '__main__':
    unittest.main()

