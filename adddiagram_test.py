import unittest
import logging
import logging.config
from models import diagram

class TestAddDiagram(unittest.TestCase):
  def test_upper(self):
      logging.config.fileConfig('config/logging.conf')
      logger = logging.getLogger("AddDiagram")
      logger.info("Program started")
      self.assertTrue(diagram.add_diagram("twelve", '6', 'package', 'pac'))
      logger.info("Done")

if __name__ == '__main__':
    unittest.main()

