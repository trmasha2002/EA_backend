import unittest
import logging
import logging.config
from models import attribute


class TestAddAttribute(unittest.TestCase):
    def test_upper(self):
        logging.config.fileConfig('config/logging.conf')
        logger = logging.getLogger("Attribute")
        logger.info("Program started")
        self.assertTrue(attribute.add_attribute("first_attibute", "1"))
        logger.info("Done!")


class TestUpdateAttribute(unittest.TestCase):
    def test_upper(self):
        logging.config.fileConfig('config/logging.conf')
        logger = logging.getLogger("Attribute")
        logger.info("Program started")
        self.assertTrue(attribute.update_attribute("second", 1))
        logger.info("Done!")




class TestDeleteAttribute(unittest.TestCase):
    def test_upper(self):
        logging.config.fileConfig('config/logging.conf')
        logger = logging.getLogger("Attribute")
        logger.info("Program started")
        attribute.delete_by_ea_guid("22422")
        logger.info("Done!")


if __name__ == '__main__':
    unittest.main()

