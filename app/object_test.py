import unittest

from app.models import object
import logging
import logging.config
class TestAddObject(unittest.TestCase):
    def test_upper(self):
        logging.config.fileConfig('config/logging.conf')
        logger = logging.getLogger("Object")
        logger.info("Program started")
        self.assertTrue(object.add_object("example", "example", "example", "1", "1"))
        logger.info("Done!")

class TestUpdateObject(unittest.TestCase):
    def test_upper(self):
        logging.config.fileConfig('config/logging.conf')
        logger = logging.getLogger("Object")
        logger.info("Program started")
        self.assertTrue(object.update_object("second", "executable", "3"))
        logger.info("Done!")

class TestDeleteObject(unittest.TestCase):
    def test_upper(self):
        logging.config.fileConfig('config/logging.conf')
        logger = logging.getLogger("Object")
        logger.info("Program started")
        self.assertTrue(object.delete_by_ea_guid("126"))
        logger.info("Done!")

if __name__ == '__main__':
    unittest.main()
