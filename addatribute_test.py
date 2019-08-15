import unittest
import logging
import logging.config
from models import attribute
class TestAddAttribute(unittest.TestCase):
    def test_upper(self):
        logging.config.fileConfig('config/logging.conf')
        logger = logging.getLogger("AddAttribute")
        logger.info("Program started")
        self.assertTrue(attribute.add_attribute("first_attibute", "1"))
        logger.info("Done!")

if __name__ == '__main__':
    unittest.main()
