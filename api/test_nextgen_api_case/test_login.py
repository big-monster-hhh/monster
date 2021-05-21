'''
Created on May 18, 2021

@author: Administrator
'''
import unittest
from test_nextgen_api_case import method

class Test(unittest.TestCase):


    def setUp(self):
        self.p=method.math()


    def tearDown(self):
        pass


    def test_login(self):
        keys=list(self.p.login().keys())
        self.assertEqual(keys, ['token', 'tokenExpiration', 'refreshToken', 'refreshExpiration', 'loginName', 'nickName', 'expiration', 'timestamp', 'userType', 'siteType', 'userCode', 'id', 'permissions', 'roleType'], 'login error')

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_login']
    unittest.main()