'''
Created on Apr 27, 2021

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
    


    def test_create_folder(self):
        
        usercode=self.p.login()['ext']['usercode']
        usertoken=self.p.login()['ext']['usertoken']
        url=information.domain+'/CM/CMAPI/CMApi/api/entity/object/saveobjectinfo'
        header={"Content-Type": "application/x-www-form-urlencoded",
                     "sobeyhive-http-system": "WEBCM",
                     "sobeyhive-http-token": usertoken,
                     "sobeyhive-http-tool": "WEBCM",
                     "sobeyhive-http-usercode": usercode}

        
        body='{"object":{"entity":{"guid":"'+self.p.get_folder_guid()+'","type":16,"folderpath":"'+information.path+'","modifier":"'+usercode+'","modifyterminal":"'+information.terminal+'","modifydate":"'+self.p.get_time()+'","name":"'+self.p.get_folder_guid()+'"}},"version":1,"type":"folder"}'
        response = requests.request("post",url,headers=header,data=body,verify=False)
        self.assertCountEqual(response.json()['code'],'0', response.json())
        time=response.elapsed.total_seconds()
        self.assertLessEqual(time, information.time ,"create_folder响应时间为%s"%time)
      
    def test_create_cp(self):
        usercode=self.p.login()['ext']['usercode']
        usertoken=self.p.login()['ext']['usertoken']
        url=information.domain+'/CM/CMAPI/CMApi/api/entity/object/saveobjectinfo'
        header={"Content-Type": "application/x-www-form-urlencoded",
                     "sobeyhive-http-system": "WEBCM",
                     "sobeyhive-http-token": usertoken,
                     "sobeyhive-http-tool": "WEBCM",
                     "sobeyhive-http-usercode": usercode}

        body='{"object":{"entity":{"guid":"'+self.p.get_folder_guid()+'","type":16,"subtype":2097152,"folderpath":"'+information.path+'","modifier":"'+usercode+'","modifyterminal":"'+information.terminal+'","modifydate":"'+self.p.get_time()+'","name":"'+self.p.get_folder_guid()+'"}},"version":1,"type":"collectionpool"}'
        response = requests.request("post",url,headers=header,data=body,verify=False)
        self.assertCountEqual(response.json()['code'],'0', response.json())
        time=response.elapsed.total_seconds()
        self.assertLessEqual(time, information.time ,"create_cp响应时间为%s"%time)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName1']
    unittest.main()