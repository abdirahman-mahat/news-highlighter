import unittest
# from app import app
from app.models import Source
class SourceTest(unittest.TestCase):
    '''
    test class to test the source class
    '''
    def setUp(self):
        '''
        setup method always runs after every test
        '''
        self.new_source = Source(12,'BBC','best source')
    def test_for_instance(self):
        self.assertTrue(isinstance(self.new_source,Source))

if __name__=='__main__':
    unittest.main()