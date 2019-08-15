import unittest
import logging
import logging.config
from models import diagramobjects

class TestAddDiagramsObject(unittest.TestCase):
    def test_upper(self):
        logging.config.fileConfig('config/logging.conf')
        logger = logging.getLogger("AddDiagramObjects")
        logger.info("Program started")
        self.assertTrue(diagramobjects.add_diagramobjects('100', '101'))
        logger.info("Done!")

if __name__ == '__main__':
    unittest.main()
