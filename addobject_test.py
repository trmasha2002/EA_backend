import unittest

from models import object
import logging
import logging.config
class TestAddObject(unittest.TestCase):
    def test_upper(self):
        logging.config.fileConfig('config/logging.conf')
        logger = logging.getLogger("AddObject")
        logger.info("Program started")
        self.assertTrue(object.add_object("example", "example", "example", "1", "1"))
        logger.info("Done!")

if __name__ == '__main__':
    unittest.main()
