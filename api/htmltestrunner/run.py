'''
Created on Dec 1, 2020

每次测试前确保cmsg2  和 csmg3 用户没有被锁，不然有些接口或者界面因为登录失败case导致账号被锁，后面的case失败

@author: Administrator

'''
import HTMLTestRunner
import unittest
from time import strftime


director = 'C:\\workspace\\api'
discover = unittest.defaultTestLoader.discover(director, pattern='test*.py')


filename= './' + strftime('%Y_%m_%d_%H_%M_%S') + 'report.html'
fp = open(filename,"wb")
HTMLTestRunner.HTMLTestRunner(stream=fp,description='描述',title='标题').run(discover)
fp.close
