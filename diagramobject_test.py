import unittest
import logging
import logging.config
from models import diagramobjects

class TestAddDiagramsObject(unittest.TestCase):
    def test_upper(self):
        logging.config.fileConfig('config/logging.conf')
        logger = logging.getLogger("DiagramObjects")
        logger.info("Program started")
        self.assertTrue(diagramobjects.add_diagramobjects('100', '101'))
        logger.info("Done!")

class TestUpdateDiagramObjects(unittest.TestCase):
    def test_upper(self):
        logging.config.fileConfig('config/logging.conf')
        logger = logging.getLogger("DiagramObjects")
        logger.info("Program started")
        self.assertTrue(diagramobjects.update_by_id('110', '111', '2'))
        logger.info("Done!")

class TestDeleteDiagramObjects(unittest.TestCase):
    def test_upper(self):
        logging.config.fileConfig('config/logging.conf')
        logger = logging.getLogger("DiagramObjects")
        logger.info("Program started")
        self.assertTrue(diagramobjects.delete_by_instance_id('32'))
        logger.info("Done!")

if __name__ == '__main__':
    unittest.main()
