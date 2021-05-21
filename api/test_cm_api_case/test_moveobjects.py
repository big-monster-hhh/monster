'''
Created on May 14, 2021

备注：单独移动非normal素材 CM前段会判断  但是移动folder可以包含非normal素材
move素材和movecp move folder接口是一样的
测试前检查被移动folder和目标folder以及contentid对应

@author: Administrator
'''
import unittest
import requests
from test_cm_api_case import method, information
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)   #禁用安全警告
import json
import time


class Test(unittest.TestCase):


    def setUp(self):
        self.p=method.math()


    def tearDown(self):
        pass

    def test_a_assetcount(self):
        usercode=self.p.login()['ext']['usercode']
        usertoken=self.p.login()['ext']['usertoken']
        header={"Content-Type": "application/x-www-form-urlencoded",
                     "sobeyhive-http-system": "WEBCM",
                     "sobeyhive-http-token": usertoken,
                     "sobeyhive-http-tool": "WEBCM",
                     "sobeyhive-http-usercode": usercode}

        url=information.domain+'/CM/CMAPI/CMApi/api/entity/search/assetcount'
        body=[information.move_folder]
        body=json.dumps(body,ensure_ascii=False,indent=4)
        response = requests.request("post",url,headers=header,data=body,verify=False)
        self.assertEqual(response.json()['code'], '0', response.json())
        
    def test_b_foldersizelist(self):
        usercode=self.p.login()['ext']['usercode']
        usertoken=self.p.login()['ext']['usertoken']
        header={"Content-Type": "application/x-www-form-urlencoded",
                     "sobeyhive-http-system": "WEBCM",
                     "sobeyhive-http-token": usertoken,
                     "sobeyhive-http-tool": "WEBCM",
                     "sobeyhive-http-usercode": usercode}

        url=information.domain+'/CM/CMAPI/CMApi/api/entity/folder/foldersizelist'
        body=[information.move_folder_contentid]
        body=json.dumps(body,ensure_ascii=False,indent=4)
        response = requests.request("post",url,headers=header,data=body,verify=False)
        self.assertEqual(response.json()['code'], '0', response.json())
        return(response.json())
        

 
    def test_c_checkfoldersize(self):
        foldersize=Test.test_b_foldersizelist(self)['ext'][0]['size']
        usercode=self.p.login()['ext']['usercode']
        usertoken=self.p.login()['ext']['usertoken']
        header={"Content-Type": "application/x-www-form-urlencoded",
                     "sobeyhive-http-system": "WEBCM",
                     "sobeyhive-http-token": usertoken,
                     "sobeyhive-http-tool": "WEBCM",
                     "sobeyhive-http-usercode": usercode}
        url=information.domain+'/CM/CMAPI/CMApi/api/entity/folder/checkfoldersize?path='+self.p.path_tranf_url(information.move_path)+'&size='+str(foldersize)+'&sourcepath='+self.p.path_tranf_url(information.move_folder_path)
        body='path='+self.p.path_tranf_url(information.move_path)+'&size='+str(foldersize)+'&sourcepath='+self.p.path_tranf_url(information.move_folder_path)
        body=json.dumps(body,ensure_ascii=False,indent=4)
        response = requests.request("get",url,headers=header,data=body,verify=False)
        self.assertEqual(response.json()['code'], '0', response.json())


    def test_d_moveobjects(self):
        usercode=self.p.login()['ext']['usercode']
        usertoken=self.p.login()['ext']['usertoken']
        header={"Content-Type": "application/x-www-form-urlencoded",
                     "sobeyhive-http-system": "WEBCM",
                     "sobeyhive-http-token": usertoken,
                     "sobeyhive-http-tool": "WEBCM",
                     "sobeyhive-http-usercode": usercode}
        url=information.domain+'/CM/CMAPI/CMApi/api/entity/object/moveobjects?desfolderpath='+self.p.path_tranf_url(information.move_path)
        body=information.move_folder_contentid
        body=json.dumps(body,ensure_ascii=False,indent=4)
        response = requests.request("post",url,headers=header,data=body,verify=False)
        self.assertEqual(response.json()['code'], '0', response.json())
        return(response.json())

    
    def test_e_move_status(self):
        taskID=Test.test_d_moveobjects(self)['ext']['taskId']
        usercode=self.p.login()['ext']['usercode']
        usertoken=self.p.login()['ext']['usertoken']
        header={"Content-Type": "application/x-www-form-urlencoded",
                     "sobeyhive-http-system": "WEBCM",
                     "sobeyhive-http-token": usertoken,
                     "sobeyhive-http-tool": "WEBCM",
                     "sobeyhive-http-usercode": usercode}

        url=information.domain+'/CM/CMAPI/CMApi/api/entity/move/status?taskid='+taskID
        body="taskid="+taskID
        body=json.dumps(body,ensure_ascii=False,indent=4)
        response = requests.request("post",url,headers=header,data=body,verify=False)
        self.assertEqual(response.json()['code'], '0', response.json())
        return(response.json())

    
    def test_f_movepermission(self):
        status=Test.test_e_move_status(self)['ext']['result'][0]['status']
        while status=='doing':
            time.sleep(2)
            status=Test.test_e_move_status(self)['ext']['result'][0]['status']

        taskID=Test.test_d_moveobjects(self)['ext']['taskId']
        usercode=self.p.login()['ext']['usercode']
        usertoken=self.p.login()['ext']['usertoken']
        header={"Content-Type": "application/x-www-form-urlencoded",
                     "sobeyhive-http-system": "WEBCM",
                     "sobeyhive-http-token": usertoken,
                     "sobeyhive-http-tool": "WEBCM",
                     "sobeyhive-http-usercode": usercode}
        
        url=information.domain+'/CM/CMAPI/CMApi/api/entity/object/movepermission?taskid='+taskID
        body="taskid="+taskID
        body=json.dumps(body,ensure_ascii=False,indent=4)
        response = requests.request("get",url,headers=header,data=body,verify=False)
        self.assertEqual(response.json()['code'], '0', response.json())
        print('wait')
        time.sleep(10)
        print('wait')
 
    def test_g_assetcount(self):
        usercode=self.p.login()['ext']['usercode']
        usertoken=self.p.login()['ext']['usertoken']
        header={"Content-Type": "application/x-www-form-urlencoded",
                     "sobeyhive-http-system": "WEBCM",
                     "sobeyhive-http-token": usertoken,
                     "sobeyhive-http-tool": "WEBCM",
                     "sobeyhive-http-usercode": usercode}

        url=information.domain+'/CM/CMAPI/CMApi/api/entity/search/assetcount'
        body=[information.recover_folder]
        body=json.dumps(body,ensure_ascii=False,indent=4)
        response = requests.request("post",url,headers=header,data=body,verify=False)
        self.assertEqual(response.json()['code'], '0', response.json())

        
    def test_h_foldersizelist(self):
        usercode=self.p.login()['ext']['usercode']
        usertoken=self.p.login()['ext']['usertoken']
        header={"Content-Type": "application/x-www-form-urlencoded",
                     "sobeyhive-http-system": "WEBCM",
                     "sobeyhive-http-token": usertoken,
                     "sobeyhive-http-tool": "WEBCM",
                     "sobeyhive-http-usercode": usercode}

        url=information.domain+'/CM/CMAPI/CMApi/api/entity/folder/foldersizelist'
        body=[information.move_folder_contentid]
        body=json.dumps(body,ensure_ascii=False,indent=4)
        response = requests.request("post",url,headers=header,data=body,verify=False)
        self.assertEqual(response.json()['code'], '0', response.json())
        return(response.json())

 
    def test_i_checkfoldersize(self):
        try:
            foldersize=Test.test_h_foldersizelist(self)['ext'][0]['size']
        except:
            foldersize='2'
        usercode=self.p.login()['ext']['usercode']
        usertoken=self.p.login()['ext']['usertoken']
        header={"Content-Type": "application/x-www-form-urlencoded",
                     "sobeyhive-http-system": "WEBCM",
                     "sobeyhive-http-token": usertoken,
                     "sobeyhive-http-tool": "WEBCM",
                     "sobeyhive-http-usercode": usercode}
        url=information.domain+'/CM/CMAPI/CMApi/api/entity/folder/checkfoldersize?path='+self.p.path_tranf_url(information.recover_path)+'&size=2'+str(foldersize)+'&sourcepath='+self.p.path_tranf_url(information.recover_folder_path)
        body='path='+self.p.path_tranf_url(information.recover_path)+'&size='+str(foldersize)+'&sourcepath='+self.p.path_tranf_url(information.recover_folder_path)
        body=json.dumps(body,ensure_ascii=False,indent=4)
        response = requests.request("get",url,headers=header,data=body,verify=False)
        self.assertEqual(response.json()['code'], '0', response.json())


    def test_j_moveobjects(self):
        usercode=self.p.login()['ext']['usercode']
        usertoken=self.p.login()['ext']['usertoken']
        header={"Content-Type": "application/x-www-form-urlencoded",
                     "sobeyhive-http-system": "WEBCM",
                     "sobeyhive-http-token": usertoken,
                     "sobeyhive-http-tool": "WEBCM",
                     "sobeyhive-http-usercode": usercode}
        url=information.domain+'/CM/CMAPI/CMApi/api/entity/object/moveobjects?desfolderpath='+self.p.path_tranf_url(information.recover_path)
        body=information.move_folder_contentid
        body=json.dumps(body,ensure_ascii=False,indent=4)
        response = requests.request("post",url,headers=header,data=body,verify=False)
        self.assertEqual(response.json()['code'], '0', response.json())
        return(response.json())

    
    def test_k_move_status(self):
        taskID=Test.test_j_moveobjects(self)['ext']['taskId']
        usercode=self.p.login()['ext']['usercode']
        usertoken=self.p.login()['ext']['usertoken']
        header={"Content-Type": "application/x-www-form-urlencoded",
                     "sobeyhive-http-system": "WEBCM",
                     "sobeyhive-http-token": usertoken,
                     "sobeyhive-http-tool": "WEBCM",
                     "sobeyhive-http-usercode": usercode}

        url=information.domain+'/CM/CMAPI/CMApi/api/entity/move/status?taskid='+taskID
        body="taskid="+taskID
        body=json.dumps(body,ensure_ascii=False,indent=4)
        response = requests.request("post",url,headers=header,data=body,verify=False)
        self.assertEqual(response.json()['code'], '0', response.json())
        return(response.json())

    
    def test_l_movepermission(self):
        status=Test.test_k_move_status(self)['ext']['result'][0]['status']
        while status=='doing':
            time.sleep(2)
            status=Test.test_k_move_status(self)['ext']['result'][0]['status']

        taskID=Test.test_j_moveobjects(self)['ext']['taskId']
        usercode=self.p.login()['ext']['usercode']
        usertoken=self.p.login()['ext']['usertoken']
        header={"Content-Type": "application/x-www-form-urlencoded",
                     "sobeyhive-http-system": "WEBCM",
                     "sobeyhive-http-token": usertoken,
                     "sobeyhive-http-tool": "WEBCM",
                     "sobeyhive-http-usercode": usercode}
        
        url=information.domain+'/CM/CMAPI/CMApi/api/entity/object/movepermission?taskid='+taskID
        body="taskid="+taskID
        body=json.dumps(body,ensure_ascii=False,indent=4)
        response = requests.request("get",url,headers=header,data=body,verify=False)
        self.assertEqual(response.json()['code'], '0', response.json())



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()