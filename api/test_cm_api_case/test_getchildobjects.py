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


    def test_getchildobjects(self):
        usercode=self.p.login()['ext']['usercode']
        usertoken=self.p.login()['ext']['usertoken']
        url=information.domain+'/CM/CMAPI/CMApi/api/v2/entity/object/getchildobjects?siteCode=&pathtype=http&path='+self.p.path_tranf_url()+'&subtype=0&querysoftlink=true&queryvideostandard=true&foldercontentid='+information.folder_contentid+'&page=1&size=500'
        
        header={"Content-Type": "application/x-www-form-urlencoded",
                     "sobeyhive-http-system": "WEBCM",
                     "sobeyhive-http-token": usertoken,
                     "sobeyhive-http-tool": "WEBCM",
                     "sobeyhive-http-usercode": usercode}

        
        
        body='siteCode=&pathtype=http&path='+self.p.path_tranf_url()+'&subtype=0&querysoftlink=true&queryvideostandard=true&foldercontentid='+information.folder_contentid+'&page=1&size=500'
        response = requests.request("get",url,headers=header,data=body,verify=False)
        self.assertCountEqual(response.json()['code'],'0', response.json())
        time=response.elapsed.total_seconds()
        self.assertLessEqual(time,information.time ,time)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()