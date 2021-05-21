'''
Created on Nov 17, 2020

@author: Administrator
'''
import requests
from test_cm_api_case import information
import pymongo
from multiprocessing import cpu_count
import hashlib
import random
import time
import json


class math():
    def __init__(self):
        pass
    def login(self,username='monster',password='monster'):
        login_url=information.ip+"/CMApi/api/basic/account/login"
        login_header={
            "Content-Type": "application/json;charset=UTF-8",
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'     
            }
        password=hashlib.md5(password.encode(encoding='UTF-8')).hexdigest()
        login_data='{"LOGINSUBSYSTEM":"CM","LOGINIP":"10.0.100.99","LOGINNAME":"'+username+'","LOGINPWD":"'+password+'"}'
        response = requests.request("post",login_url,headers=login_header,data=login_data,verify=False)
#         usercode=response.json()['ext']['usercode']
#         usertoken=response.json()['ext']['usertoken']
#         logininfoid=response.json()['ext']['logininfoid']
        return(response.json())

    def get_time(self):
        now=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
        return(now)
    
    
    def connect_mongo(self):
        mongo_client = pymongo.MongoClient(information.host, information.port)
        db = mongo_client.admin
        # 认证
        db.authenticate(information.user_name, information.user_pwd)
        # 需要用的的表需要在认证后用client单独去关联
        hive=mongo_client.hivedb #hivedb
        all_coll = hive.list_collection_names()#获取hive下的所有集合
#         print(all_coll)
        return(hive)
    
    def cpu_count(self):
        return(cpu_count())

    def MD5(self,string):
        encoder=hashlib.md5(string.encode(encoding='UTF-8')).hexdigest()  #md5加密
        return(encoder)
    
    def get_folder_guid(self,char='abcdefghijklmnopqrstuvwxyz0123456789'):
        guid=random.sample(char,32)
        guid="".join(guid)
        return(guid)
    
    def get_clip_guid(self,char='abcdefabcdef01234567890123456789'):
        char='abcdefabcdef01234567890123456789'
        guid=random.sample(char,32)
        guid="".join(guid)
        return(guid)
    
    def path_tranf_url(self,path=information.path):
        path=path.replace('/',"%2F")
        path=path.replace(' ',"%20")
        return(path)
    
    def getfoldercollectionname(self,path=information.path):     #获取目标文件下的素材的基础信息 只包含name和type
        usercode=self.login()['ext']['usercode']
        usertoken=self.login()['ext']['usertoken']
        url=information.domain+'/CM/CMAPI/CMApi/api/entity/folder/getfoldercollectionname?path='+self.path_tranf_url(path)

        header={"Content-Type": "application/x-www-form-urlencoded",
                     "sobeyhive-http-system": "WEBCM",
                     "sobeyhive-http-token": usertoken,
                     "sobeyhive-http-tool": "WEBCM",
                     "sobeyhive-http-usercode": usercode}

        body='path='+self.path_tranf_url(path)
        response = requests.request("get",url,headers=header,data=body,verify=False)
        return(response.json())
    
    def getobjectinfo(self,clip_contentid=information.clip_contentid):    #获取单个素材信息 用来获取trim和save pic的body信息
        usercode=self.login()['ext']['usercode']
        usertoken=self.login()['ext']['usertoken']
        header={"Content-Type": "application/x-www-form-urlencoded",
                     "sobeyhive-http-system": "WEBCM",
                     "sobeyhive-http-token": usertoken,
                     "sobeyhive-http-tool": "WEBCM",
                     "sobeyhive-http-usercode": usercode}
        
        url=information.domain+'/CM/CMAPI/CMApi/api/v3/entity/object/getobjectinfo?queryvideostandard=true&contentid='+clip_contentid+'&pathtype=http&objecttype=32&siteCode='
        body='queryvideostandard=true&contentid='+clip_contentid+'&pathtype=unc&objecttype=32&siteCode='
        response = requests.request("get",url,headers=header,data=body,verify=False)
        return(response.json())
    
    
    
    def getchildobjects(self,path=information.path):  #目标文件夹必须要和contentid一致       获取目标文件夹下的所有素材信息包括folder和cp  不递归
        usercode=self.login()['ext']['usercode']
        usertoken=self.login()['ext']['usertoken']
        url=information.domain+'/CM/CMAPI/CMApi/api/v2/entity/object/getchildobjects?siteCode=&pathtype=http&path='+self.path_tranf_url(path)+'&subtype=0&querysoftlink=true&queryvideostandard=true&foldercontentid='+information.folder_contentid+'&page=1&size=500'
        
        header={"Content-Type": "application/x-www-form-urlencoded",
                     "sobeyhive-http-system": "WEBCM",
                     "sobeyhive-http-token": usertoken,
                     "sobeyhive-http-tool": "WEBCM",
                     "sobeyhive-http-usercode": usercode}
        
        body='siteCode=&pathtype=http&path='+self.path_tranf_url(path)+'&subtype=0&querysoftlink=true&queryvideostandard=true&foldercontentid='+information.folder_contentid+'&page=1&size=500'
        response = requests.request("get",url,headers=header,data=body,verify=False)
        return(response.json())

    def fulltextsearchnew(self,path=information.folder_path):         #用来获取目标文件夹下的所有素材（可以递归用）
        usercode=self.login()['ext']['usercode']
        usertoken=self.login()['ext']['usertoken']
        header={"Content-Type": "application/x-www-form-urlencoded",
                     "sobeyhive-http-system": "WEBCM",
                     "sobeyhive-http-token": usertoken,
                     "sobeyhive-http-tool": "WEBCM",
                     "sobeyhive-http-usercode": usercode}
        
        url=information.domain+'/CM/CMAPI/CMApi/api/v3/entity/search/fulltextsearchnew?queryvideostandard=true&pathtype=http'
        body={"kvs":[{"key":"tree_path_","value":path}],"usercode":usercode,"condition":{"include":"*","exacts":"","anys":"","notstr":""},"page":1,"size":500}
        body=json.dumps(body,ensure_ascii=False,indent=4)
        response = requests.request("post",url,headers=header,data=body,verify=False)
        return(response.json())


        
        
        

