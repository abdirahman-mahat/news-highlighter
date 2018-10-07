mport unittest
from models import articles
Articles=articles.Articles

class ArticlesTest(unittest.TestCase):
    '''
    testcase class
    '''
    def setUp(self):
        '''
        testcase that runs after every test
        '''
        self.new_article= Articles ('bbc-news','bbc','Charlie Adams','NJ Couple Ordered to Hand Over GoFundMe Money to Homeless Vet After He Accused Them of Fraud','the big blue wind blew for everyone','www.espn.com','www.image.com',20-5-2018)
    def test_for_instance(self):
        self.assertTrue(isinstance(self.new_article,Articles))
if __name__=='__main__':
    unittest.main()