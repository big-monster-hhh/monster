'''
Created on May 11, 2021
备注：
ad账号与普通登录接口不一致
没有权限的账户可以使用接口直接登录，后期通过UI实现
@author: Administrator  
'''
import unittest
from test_cm_api_case import method

class Test(unittest.TestCase):


    def setUp(self):
        self.p=method.math()
        self.normal_account='cmsg1'    #普通账号
        self.normal_pwd='123'     #普通账号密码
        self.error_user_account='cmsghhh1'      #错误账号用户
        self.error_user_pwd='123'       #错误账号用户密码
        self.error_pwd_account='cmsg2'      #错误密码用户
        self.error_pwd_pwd='12345'       #错误密码用户密码
        self.error_userpwd_account='cmsghhh1'      #错误账号密码用户
        self.error_userpwd_pwd='cmsghhh1'       #错误账号密码用户密码
 

    def tearDown(self):
        pass
        

    def test_a_normal_account_login(self):
        code=self.p.login(self.normal_account,self.normal_pwd)['code']
        msg=self.p.login(self.normal_account,self.normal_pwd)['msg']
        self.assertEqual(code, '0', '返回值code异常：%s'%code)
        self.assertEqual(msg, 'login status update data is success。', '返回值msg异常：%s'%msg)
        

    def test_b_error_user_account_login(self):
        code=self.p.login(self.error_user_account,self.normal_pwd)['code']
        self.assertEqual(code, '104',code)


    def test_c_error_pwd_account_login(self):    #登录失败次数达到限制账号被锁 
        errorMessage=self.p.login(self.error_pwd_account,self.error_pwd_pwd)['errorMessage']
        self.assertEqual(errorMessage, {'failedCount': 1, 'maxFailedCount': 3},errorMessage)
        errorMessage1=self.p.login(self.error_pwd_account,self.error_pwd_pwd)['errorMessage']
        self.assertEqual(errorMessage1, {'failedCount': 2, 'maxFailedCount': 3},errorMessage)
        errorMessage2=self.p.login(self.error_pwd_account,self.error_pwd_pwd)['errorMessage']
        self.assertEqual(list(errorMessage2.keys()), ['failedCount', 'lockTime', 'maxFailedCount'],errorMessage2)
        

    def test_d_error_userpwd_account_login(self):
        code=self.p.login(self.error_userpwd_account,self.error_userpwd_pwd)['code']
        self.assertEqual(code, '104',code)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()