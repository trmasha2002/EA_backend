import unittest
import logging
import logging.config
from models import package
class TestAddPackage(unittest.TestCase):
  def test_upper(self):
      logging.config.fileConfig('config/logging.conf')
      logger = logging.getLogger("AddPackage")
      self.assertTrue(package.add_package("Test", None, None, "Package", "1"))
      logger.info("Done!")

if __name__ == '__main__':
    unittest.main()


