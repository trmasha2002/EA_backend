import unittest
import logging
import logging.config
from models import diagram


class TestAddDiagram(unittest.TestCase):
  def test_upper(self):
      logging.config.fileConfig('config/logging.conf')
      logger = logging.getLogger("Diagram")
      logger.info("Program started")
      self.assertTrue(diagram.add_diagram("twelve", '6', 'package', 'pac'))
      logger.info("Done!")

class TestUpdateDiagram(unittest.TestCase):
    def test_upper(self):
        logging.config.fileConfig('config/logging.conf')
        logger = logging.getLogger("Diagram")
        logger.info("Program started")
        self.assertTrue(
            diagram.update_by_ea_guid("name", "stereotype", "app-link", "{10774b8a-2e77-431f-9deb-c2ad65e24d5c}"))
        logger.info("Done!")


class TestDeleteDiagram(unittest.TestCase):
    def test_upper(self):
        logging.config.fileConfig('config/logging.conf')
        logger = logging.getLogger("Diagram")
        logger.info("Program started")
        self.assertTrue(diagram.delete_by_ea_guid("99499"))
        logger.info("Done!")


if __name__ == '__main__':
    unittest.main()
