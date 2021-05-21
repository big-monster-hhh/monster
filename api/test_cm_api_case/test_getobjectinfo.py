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


    def test_getobjectinfo(self):
        usercode=self.p.login()['ext']['usercode']
        usertoken=self.p.login()['ext']['usertoken']
        header={"Content-Type": "application/x-www-form-urlencoded",
                     "sobeyhive-http-system": "WEBCM",
                     "sobeyhive-http-token": usertoken,
                     "sobeyhive-http-tool": "WEBCM",
                     "sobeyhive-http-usercode": usercode}
        
        url=information.domain+'/CM/CMAPI/CMApi/api/v3/entity/object/getobjectinfo?queryvideostandard=true&contentid='+information.clip_contentid+'&pathtype=http&objecttype=32&siteCode='
        body='queryvideostandard=true&contentid='+information.clip_contentid+'&pathtype=unc&objecttype=32&siteCode='
        response = requests.request("get",url,headers=header,data=body,verify=False)
        self.assertCountEqual(response.json()['code'],'0', response.json())
        self.assertCountEqual(response.json()['msg'],'success', response.json())


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()