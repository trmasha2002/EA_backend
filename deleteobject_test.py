import unittest
import logging
import logging.config
from models import object

class TestDeleteObject(unittest.TestCase):
    def test_upper(self):
        logging.config.fileConfig('config/logging.conf')
        #logger = logging.getLogger("UpdateObject")
        #logger.info("Program started")
        self.assertTrue(object.delete_by_ea_guid('{a17b50e1-a05e-4fdc-9bd3-9d1661e5b39b}'))
        #logger.info("Done!")

if __name__ == '__main__':
    unittest.main()
