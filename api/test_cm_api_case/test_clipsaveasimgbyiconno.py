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



    def test_savebmp(self):
        usercode=self.p.login()['ext']['usercode']
        usertoken=self.p.login()['ext']['usertoken']

        header={"Content-Type": "application/x-www-form-urlencoded",
                     "sobeyhive-http-system": "WEBCM",
                     "sobeyhive-http-token": usertoken,
                     "sobeyhive-http-tool": "WEBCM",
                     "sobeyhive-http-usercode": usercode}
        
        newdata={"type":"biz_sobey_picture","version":1,"object":self.p.getobjectinfo()['ext']}
        newdata['object']['entity']['isseparation']='true'
        newdata['object']['entity']['storagequota']=0
        newdata['object']['entity']['guid']=self.p.get_clip_guid() 
        newdata['object']['entity']['subtype']=32
        newdata['object']['entity']['creator']=newdata['object']['entity']['modifier']
        del newdata['object']['entity']['mosid']
        newdata['object']['entity']['item']['trimout']=40000000
        newdata['object']['entity']['item']['length']=863999600000
        del newdata['object']['entity']['item']['streamflag']
        newdata['object']['entity']['status']=0
        body=json.dumps(newdata,ensure_ascii=False,indent=4)
        storage=self.p.getobjectinfo()['ext']['entity']['item']['clipfile'][0]['filename']
        filename=storage.replace('\\','%5C')
        url=information.domain+'/CM/CMAPI/CMApi/api/entity/clip/clipsaveasimgbyiconno?filename='+filename+'&iconno='+str(information.iconno)+'&extendname=bmp&fileformatid=568625'
        
        response = requests.request("post",url,headers=header,data=body,verify=False)
        self.assertCountEqual(response.json()['code'],'0', response.json())
        time=response.elapsed.total_seconds()
        self.assertLessEqual(time,information.time ,time)

        
    def test_savejpg(self):
        usercode=self.p.login()['ext']['usercode']
        usertoken=self.p.login()['ext']['usertoken']

        header={"Content-Type": "application/x-www-form-urlencoded",
                     "sobeyhive-http-system": "WEBCM",
                     "sobeyhive-http-token": usertoken,
                     "sobeyhive-http-tool": "WEBCM",
                     "sobeyhive-http-usercode": usercode}
        
        newdata={"type":"biz_sobey_picture","version":1,"object":self.p.getobjectinfo()['ext']}
        newdata['object']['entity']['isseparation']='true'
        newdata['object']['entity']['storagequota']=0
        newdata['object']['entity']['guid']=self.p.get_clip_guid() 
        newdata['object']['entity']['subtype']=32
        newdata['object']['entity']['creator']=newdata['object']['entity']['modifier']
        del newdata['object']['entity']['mosid']
        newdata['object']['entity']['item']['trimout']=40000000
        newdata['object']['entity']['item']['length']=863999600000
        del newdata['object']['entity']['item']['streamflag']
        newdata['object']['entity']['status']=0
        body=json.dumps(newdata,ensure_ascii=False,indent=4)
        storage=self.p.getobjectinfo()['ext']['entity']['item']['clipfile'][0]['filename']
        filename=storage.replace('\\','%5C')
        url=information.domain+'/CM/CMAPI/CMApi/api/entity/clip/clipsaveasimgbyiconno?filename='+filename+'&iconno='+str(information.iconno)+'&extendname=jpg&fileformatid=568625'
        
        response = requests.request("post",url,headers=header,data=body,verify=False)
        self.assertCountEqual(response.json()['code'],'0', response.json())
        time=response.elapsed.total_seconds()
        self.assertLessEqual(time,information.time ,time)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()