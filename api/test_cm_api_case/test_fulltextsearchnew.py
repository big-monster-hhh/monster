'''
Created on May 13, 2021

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


    def test_fulltextsearchnew(self):         #用来获取目标文件夹下的所有素材（可以递归用）
        usercode=self.p.login()['ext']['usercode']
        usertoken=self.p.login()['ext']['usertoken']
        header={"Content-Type": "application/x-www-form-urlencoded",
                     "sobeyhive-http-system": "WEBCM",
                     "sobeyhive-http-token": usertoken,
                     "sobeyhive-http-tool": "WEBCM",
                     "sobeyhive-http-usercode": usercode}
        
        totalPage=self.p.fulltextsearchnew()['totalPage']
        totalCount=self.p.fulltextsearchnew()['totalCount']
        url=information.domain+'/CM/CMAPI/CMApi/api/v3/entity/search/fulltextsearchnew?queryvideostandard=true&pathtype=http'
        if totalPage==0:
            print('目标文件夹下没有素材') 
        else:
            i=0
            while i<totalPage:
                body={"kvs":[{"key":"tree_path_","value":information.folder_path}],"usercode":usercode,"condition":{"include":"*","exacts":"","anys":"","notstr":""},"page":i+1,"size":500}
                body=json.dumps(body,ensure_ascii=False,indent=4)
                response = requests.request("post",url,headers=header,data=body,verify=False)
                self.assertEqual(response.json()['totalCount'], totalCount, response.json())
                i+=1
            


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()