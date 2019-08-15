import unittest
import logging
import logging.config
from models import object

class TestUpdateObject(unittest.TestCase):
    def test_upper(self):
        logging.config.fileConfig('config/logging.conf')
        logger = logging.getLogger("UpdateObject")
        logger.info("Program started")
        self.assertTrue(object.update_object("NewPackage", "executable", "1"))
        logger.info("Done!")

if __name__ == '__main__':
    unittest.main()
