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


    def test_trim(self):
        usercode=self.p.login()['ext']['usercode']
        usertoken=self.p.login()['ext']['usertoken']
        header={"Content-Type": "application/x-www-form-urlencoded",
                     "sobeyhive-http-system": "WEBCM",
                     "sobeyhive-http-token": usertoken,
                     "sobeyhive-http-tool": "WEBCM",
                     "sobeyhive-http-usercode": usercode}
        

        url='https://srf.test.com/CM/CMAPI/CMApi/api/entity/clip/savenewclip?trimin='+str(information.nanoSecIn)+ '&trimout='+str(information.nanoSecOut)
        body={"isLive":'false',"trimin":information.trimin,"trimout":information.trimout,"nanoSecIn":information.nanoSecIn,"nanoSecOut":information.nanoSecOut,"object":self.p.getobjectinfo()['ext'], 'version': 1, 'type': 'biz_sobey_video'}
        body['object']['entity']['isseparation']='true'
        body['object']['entity']['storagequota']=0
        body['object']['entity']['id']=''
        body['object']['entity']['iconframe']='0'
        body['object']['entity']['iconframe']=0
        del body['object']['entity']['iconfilename']
        del body['object']['entity']['mosid']
        body=json.dumps(body,ensure_ascii=False,indent=4)
        response = requests.request("post",url,headers=header,data=body,verify=False)
        self.assertCountEqual(response.json()['code'],'0', response.json())
        time=response.elapsed.total_seconds()
        self.assertLessEqual(time,information.time ,time)

        

    def test_mark_trim(self):
        usercode=self.p.login()['ext']['usercode']
        usertoken=self.p.login()['ext']['usertoken']
        header={"Content-Type": "application/x-www-form-urlencoded",
                     "sobeyhive-http-system": "WEBCM",
                     "sobeyhive-http-token": usertoken,
                     "sobeyhive-http-tool": "WEBCM",
                     "sobeyhive-http-usercode": usercode}
        
        url='https://srf.test.com/CM/CMAPI/CMApi/api/entity/clip/savenewclip'
        body={"isLive":'false',"object":self.p.getobjectinfo()['ext'], 'version': 1, 'type': 'biz_sobey_video'}
        body['object']['entity']['isseparation']='true'
        body['object']['entity']['storagequota']=0
        body['object']['entity']['id']=''
        del body['object']['entity']['iconfilename']
        del body['object']['entity']['mosid']
        del body['object']['streammedia']
        body=json.dumps(body,ensure_ascii=False,indent=4)
        response = requests.request("post",url,headers=header,data=body,verify=False)
        self.assertCountEqual(response.json()['code'],'0', response.json())
        time=response.elapsed.total_seconds()
        self.assertLessEqual(time,information.time ,time)



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()