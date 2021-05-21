from test_nextgen_api_case import information
import requests
import pymongo
from multiprocessing import cpu_count
import hashlib
import random
import time
import json
from distutils.log import info


class math():
    def __init__(self):
        pass
    def login(self,username='admin',password='admin'):

        header={"sobeyhive-http-operate-site":"S1",
                      "sobeyhive-http-site":"S1",
                      "sobeyhive-http-system":"SobeyHive",
                      "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"
            }

        body={
            "operateSite": "S1",
            "loginName": username,
            "password": password,
            "language": "en_US",
            "site": "S1",
            "expiration": 60
            }

        response = requests.request("post",information.login_url,headers=header,data=body,verify=False)
        return(response.json())

# p=math()
# print(p.login()['token'])
# print(type(p.login()['token']))


        