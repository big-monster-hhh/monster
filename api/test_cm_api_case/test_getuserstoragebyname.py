'''
Created on May 13, 2021

@author: Administrator
'''
import unittest
import requests
from test_cm_api_case import method, information
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)   #禁用安全警告


class Test(unittest.TestCase):


    def setUp(self):
        self.p=method.math()


    def tearDown(self):
        pass


    def test_getuserstoragebyname(self):
        usercode=self.p.login()['ext']['usercode']
        usertoken=self.p.login()['ext']['usertoken']
        header={"Content-Type": "application/x-www-form-urlencoded",
                "sobeyhive-http-system": "WEBCM",
                "sobeyhive-http-token": usertoken,
                "sobeyhive-http-tool": "WEBCM",
                "sobeyhive-http-usercode": usercode}
        url=information.domain+'/CM/CMAPI/CMApi/api/basic/account/getuserstoragebyname?loginName='+information.username
        body='{loginName:'+information.username+'}'
        response = requests.request("get",url,headers=header,data=body,verify=False)
        result=list(response.json()['ext'].keys())
        expect=['storagesize', 'storageusage', 'storagewarningpct', 'storagecritical']
        self.assertCountEqual(result, expect, response.json())
        time=response.elapsed.total_seconds()
        self.assertLessEqual(time,information.time,"getuserstoragebyname响应时间为%s"%time)




if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()