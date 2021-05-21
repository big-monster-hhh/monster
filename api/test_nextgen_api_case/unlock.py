'''
Created on May 18, 2021

@author: Administrator
'''
import unittest
from test_nextgen_api_case import method,information
import requests


class Test(unittest.TestCase):


    def setUp(self):
        self.p=method.math()


    def tearDown(self):
        pass


    def test_unlock1(self):
        usercode=self.p.login(information.lock_user1,information.lock_passwd1)['userCode']
        unlock_url=information.domain+'/nebula-api/users/'+usercode+'/unlock'
        header={
            "sobeyhive-http-operate-site":"S1",
            "sobeyhive-http-site":"S1",
            "sobeyhive-http-system":"SOLAR",
            "sobeyhive-http-token":self.p.login()['token'],
            "sobeyhive-http-user":information.username,
            "Token-Expiration":"60"}
        
        response = requests.request("get",unlock_url,headers=header,data='',verify=False)
        keys=list(response.json().keys())
        self.assertEqual(keys, ['userCode'],response.json())
        
      
    def test_unlock2(self):
        usercode=self.p.login(information.lock_user2,information.lock_passwd2)['userCode']
        unlock_url=information.domain+'/nebula-api/users/'+usercode+'/unlock'
        header={
            "sobeyhive-http-operate-site":"S1",
            "sobeyhive-http-site":"S1",
            "sobeyhive-http-system":"SOLAR",
            "sobeyhive-http-token":self.p.login()['token'],
            "sobeyhive-http-user":information.username,
            "Token-Expiration":"60"}
        
        response = requests.request("get",unlock_url,headers=header,data='',verify=False)
        keys=list(response.json().keys())
        self.assertEqual(keys, ['userCode'],response.json())
        
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_login']
    unittest.main()