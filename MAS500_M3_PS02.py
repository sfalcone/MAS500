# Showing a "test-driven" style

from MAS500_M3_PS01 import fetch_candidate_data
import unittest, datetime

# source: https://github.com/mitmedialab/MediaCloud-API-Client/blob/master/mediacloud/test/apitest.py
class MediaCloudTest(unittest.TestCase):

    #see a passing test... positivity...
    def test_test(self):
        pass

    #check that data is received
    def test_data_fetch(self):
        self.response = fetch_candidate_data('trump')
        assert self.response >= 0


# if this file is run directly, run the tests
if __name__ == "__main__":
    unittest.main()









