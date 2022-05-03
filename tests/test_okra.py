import unittest
import sys

import okra

class TestUtils(unittest.TestCase):
    
    def test_help(self):
        sys.argv.append('--help')
        okra.load_config(sys.argv[1:])
        
    def test_short_schema_1(self):
        okra.load_config(
            schema_path='./tests/schemas/short_schema.yaml',
            config_path='./tests/configs/short_config_1.yaml'
            )
        
if __name__ == '__main__':
    unittest.main()
