'''
Created on May 13, 2021
该case前提 测试账户只用准备1个检索模板（通过查询已有检索模板的过滤条件作为新模板的条件）
@author: Administrator
'''
# -*- coding: utf8 -*-
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

    #获取my template
    def test_a_querybyusercode(self):         
        usercode=self.p.login()['ext']['usercode']
        usertoken=self.p.login()['ext']['usertoken']
        header={"Content-Type": "application/x-www-form-urlencoded",
                     "sobeyhive-http-system": "WEBCM",
                     "sobeyhive-http-token": usertoken,
                     "sobeyhive-http-tool": "WEBCM",
                     "sobeyhive-http-usercode": usercode}
        
        url=information.domain+'/CM/CMAPI/CMApi/api/general/data/querybyusercode?type=0'
        body=[usercode]
        body=json.dumps(body,ensure_ascii=False,indent=4)
        response = requests.request("post",url,headers=header,data=body,verify=False)
        self.assertEqual(response.json()['code'], '0', response.json())
        return(response.json())

        
    #添加检索模板
#     @unittest.skip('')
    def test_b_data_add(self):
        usercode=self.p.login()['ext']['usercode']
        usertoken=self.p.login()['ext']['usertoken']
        header={"Content-Type": "application/x-www-form-urlencoded",
                "sobeyhive-http-system": "WEBCM",
                "sobeyhive-http-token": usertoken,
                "sobeyhive-http-tool": "WEBCM",
                "sobeyhive-http-usercode": usercode,
                'Content-Type': 'application/json'}
        url=information.domain+'/CM/CMAPI/CMApi/api/general/data/add'
        body=[{'type':0,'name':information.my_tmp_name,'data':Test.test_a_querybyusercode(self)['ext'][0]['data'],"usercodes":["e358de165ec2443e82cc0374a52c1961"]}]
        body=json.dumps(body)
        response = requests.request("post",url,headers=header,data=body,verify=False)
        self.assertEqual(response.json()['code'], '0', response.json())
        return(response.json())
  
        
    #共享检索模板添加（1）
    def test_c_data_add(self):
        usercode=self.p.login()['ext']['usercode']
        usertoken=self.p.login()['ext']['usertoken']
        header={"Content-Type": "application/x-www-form-urlencoded",
                "sobeyhive-http-system": "WEBCM",
                "sobeyhive-http-token": usertoken,
                "sobeyhive-http-tool": "WEBCM",
                "sobeyhive-http-usercode": usercode,
                'Content-Type': 'application/json'}
        url=information.domain+'/CM/CMAPI/CMApi/api/general/data/add'
        body=[{'type':0,'name':information.share_tmp_name,'data':Test.test_a_querybyusercode(self)['ext'][0]['data'],"usercodes":["e358de165ec2443e82cc0374a52c1961"]}]
        body=json.dumps(body)
        response = requests.request("post",url,headers=header,data=body,verify=False)
        self.assertEqual(response.json()['code'], '0', response.json())
        return(response.json())
    
    #共享检索模板添加（2）
    def test_d_template_add(self):
    
        usercode=self.p.login()['ext']['usercode']
        usertoken=self.p.login()['ext']['usertoken']
        header={"Content-Type": "application/x-www-form-urlencoded",
                "sobeyhive-http-system": "WEBCM",
                "sobeyhive-http-token": usertoken,
                "sobeyhive-http-tool": "WEBCM",
                "sobeyhive-http-usercode": usercode,
                'Content-Type': 'application/json'}
        url=information.domain+'/CM/CMAPI/CMApi/api/share/template/add'
        body=[{"templateid":Test.test_a_querybyusercode(self)['ext'][2]['templateid'],"fromuser":usercode,"touser":information.touser,"type":0}]
        body=json.dumps(body)
        response = requests.request("post",url,headers=header,data=body,verify=False)
        self.assertEqual(response.json()['code'], '0', response.json())
        return(response.json())
    
    def test_e_queryshareed(self):
        usercode=self.p.login()['ext']['usercode']
        usertoken=self.p.login()['ext']['usertoken']
        header={"Content-Type": "application/x-www-form-urlencoded",
                "sobeyhive-http-system": "WEBCM",
                "sobeyhive-http-token": usertoken,
                "sobeyhive-http-tool": "WEBCM",
                "sobeyhive-http-usercode": usercode,
                'Content-Type': 'application/json'}
        url=information.domain+'/CM/CMAPI/CMApi/api/share/template/queryshareed'
        body=[usercode]
        body=json.dumps(body)
        response = requests.request("post",url,headers=header,data=body,verify=False)
        self.assertEqual(response.json()['code'], '0', response.json())
        return(response.json())
        
    #删除my template
    def test_f_deletebyid(self):
        usercode=self.p.login()['ext']['usercode']
        usertoken=self.p.login()['ext']['usertoken']
        header={"Content-Type": "application/x-www-form-urlencoded",
                "sobeyhive-http-system": "WEBCM",
                "sobeyhive-http-token": usertoken,
                "sobeyhive-http-tool": "WEBCM",
                "sobeyhive-http-usercode": usercode}
        url=information.domain+'/CM/CMAPI/CMApi/api/general/data/deletebyid'
        body=[Test.test_a_querybyusercode(self)['ext'][1]['id']]
        body=json.dumps(body)
        response = requests.request("delete",url,headers=header,data=body,verify=False)
        self.assertEqual(response.json()['code'], '0', response.json())
        
        
    #删除shared template
    def test_g_deletebyid(self):
        usercode=self.p.login()['ext']['usercode']
        usertoken=self.p.login()['ext']['usertoken']
        header={"Content-Type": "application/x-www-form-urlencoded",
                "sobeyhive-http-system": "WEBCM",
                "sobeyhive-http-token": usertoken,
                "sobeyhive-http-tool": "WEBCM",
                "sobeyhive-http-usercode": usercode}
        url=information.domain+'/CM/CMAPI/CMApi/api/general/data/deletebyid'
        body=[Test.test_e_queryshareed(self)['ext'][0]['id']]
        body=json.dumps(body)
        response = requests.request("delete",url,headers=header,data=body,verify=False)
        self.assertEqual(response.json()['code'], '0', response.json())
    #修改检索模板
    def test_h_update(self):
        usercode=self.p.login()['ext']['usercode']
        usertoken=self.p.login()['ext']['usertoken']
        header={"Content-Type": "application/x-www-form-urlencoded",
                "sobeyhive-http-system": "WEBCM",
                "sobeyhive-http-token": usertoken,
                "sobeyhive-http-tool": "WEBCM",
                "sobeyhive-http-usercode": usercode,
                'Content-Type': 'application/json'}
        url=information.domain+'/CM/CMAPI/CMApi/api/general/data/update'
        body={'type':0,'id':Test.test_a_querybyusercode(self)['ext'][0]['id'],'templateid':Test.test_a_querybyusercode(self)['ext'][0]['templateid'],'name':information.update_name,'data':Test.test_a_querybyusercode(self)['ext'][0]['data'],"usercodes":["e358de165ec2443e82cc0374a52c1961"]}
        body=json.dumps(body)
        response = requests.request("patch",url,headers=header,data=body,verify=False)
        self.assertEqual(response.json()['code'], '0', response.json())
       


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()