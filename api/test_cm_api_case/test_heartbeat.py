'''
Created on May 12, 2021

@author: Administrator
'''
import unittest

import requests
from test_cm_api_case import method, information
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)   #禁用安全警告
import json

class Test(unittest.TestCase):


    def setUp(self):
        self.p=method.math()


    def tearDown(self):
        pass


    def test_heatbeat(self):  
        usercode=self.p.login()['ext']['usercode']
        usertoken=self.p.login()['ext']['usertoken']
        logininfoid=self.p.login()['ext']['logininfoid']

        header={"Content-Type": "application/x-www-form-urlencoded",
                "sobeyhive-http-system": "WEBCM",
                "sobeyhive-http-token": usertoken,
                "sobeyhive-http-tool": "WEBCM",
                "sobeyhive-http-usercode": usercode}
        
        url=information.domain+'/CM/CMAPI/CMApi/api/basic/account/heatbeat?loginInfoID='+str(logininfoid)+'&systemtype='
        body="loginInfoID="+str(logininfoid)+"&systemtype="
        body=json.dumps(body,ensure_ascii=False,indent=4)

        response = requests.request("get",url,headers=header,data=body,verify=False)
        self.assertCountEqual('login status update data is success。', response.json()['msg'], response.json())
        time=response.elapsed.total_seconds()
        self.assertLessEqual(time,information.time,"heatbeat响应时间为%s"%time)

   

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()