'''
Created on May 12, 2021

@author: Administrator
'''
import unittest
from selenium.webdriver import Chrome
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.action_chains import ActionChains
import time
from test_ui_case import information




class Test(unittest.TestCase):


    def setUp(self):
        self.dr=Chrome()
        self.dr.get(information.login_url)
        self.Actions = ActionChains(self.dr)
        self.dr.maximize_window()

    def tearDown(self):
        self.dr.quit()

#     @unittest.skip('')
    def test_Normal_account(self):
        time.sleep(2)
        self.dr.find_element_by_xpath(information.username).send_keys(information.normal_account)
        self.dr.find_element_by_xpath(information.pwd).send_keys(information.normal_pwd)
        self.dr.find_element_by_xpath(information.login_buton).click()
        time_start=time.time()
        WebDriverWait(self.dr, 50, 0.5).until(EC.presence_of_element_located((By.XPATH,information.user)))
        network=self.dr.find_element_by_xpath(information.network).text
        quicklinks=self.dr.find_element_by_xpath(information.quciklinks).text
        search_template=self.dr.find_element_by_xpath(information.search_template).text
        user=self.dr.find_element_by_xpath(information.user).text
        time_end=time.time()
        costtime=float(time_end-time_start)
        self.assertGreater(information.login_time,costtime,'登录超时，性能不达标')
        self.assertEqual(network, 'Network', 'Network节点没有刷新出来')
        self.assertEqual(quicklinks, 'Quick Links', 'Quick Links节点没有刷新出来')
        self.assertEqual(search_template, 'Search Template', 'search_template节点没有刷新出来')
        self.assertEqual(user, information.normal_account, 'search_template节点没有刷新出来')
        time.sleep(3)
        self.Actions.move_to_element(self.dr.find_element_by_xpath(information.logout_option)).click().perform()
        WebDriverWait(self.dr, 5, 0.5).until(EC.presence_of_element_located((By.XPATH, information.logout)))
        self.Actions.move_to_element(self.dr.find_element_by_xpath(information.logout)).click().perform()
        time.sleep(2)
        log=self.dr.find_element_by_xpath(information.login_buton).text
        self.assertEqual(log,'Login','登出失败')
        

#     @unittest.skip('')    
    def test_error_user_account(self):
        time.sleep(2)
        self.dr.find_element_by_xpath(information.username).send_keys(information.error_user_account)
        self.dr.find_element_by_xpath(information.pwd).send_keys(information.error_user_pwd)
        self.dr.find_element_by_xpath(information.login_buton).click()
        time.sleep(2)
        WebDriverWait(self.dr, 50, 0.5).until(EC.presence_of_element_located((By.XPATH,information.msg)))
        msg=self.dr.find_element_by_xpath(information.msg).text
        self.assertEqual(msg,'Invalid Username or Password, please try again!',msg)
        
#     @unittest.skip('')    
    def test_error_userpwd_account(self):
        time.sleep(2)
        self.dr.find_element_by_xpath(information.username).send_keys(information.error_userpwd_account)
        self.dr.find_element_by_xpath(information.pwd).send_keys(information.error_userpwd_pwd)
        self.dr.find_element_by_xpath(information.login_buton).click()
        time.sleep(2)
        WebDriverWait(self.dr, 50, 0.5).until(EC.presence_of_element_located((By.XPATH,information.msg)))
        msg=self.dr.find_element_by_xpath(information.msg).text
        self.assertEqual(msg,'Invalid Username or Password, please try again!',msg)

#     @unittest.skip('')
    def test_AD_account(self):
        time.sleep(2)
        self.dr.find_element_by_xpath(information.username).send_keys(information.aduser_account)
        self.dr.find_element_by_xpath(information.pwd).send_keys(information.aduser_pwd)
        self.dr.find_element_by_xpath(information.login_buton).click()
        time_start=time.time()
        WebDriverWait(self.dr, 50, 0.5).until(EC.presence_of_element_located((By.XPATH,information.user)))
        network=self.dr.find_element_by_xpath(information.network).text
        quicklinks=self.dr.find_element_by_xpath(information.quciklinks).text
        search_template=self.dr.find_element_by_xpath(information.search_template).text
        user=self.dr.find_element_by_xpath(information.user).text
        time_end=time.time()
        costtime=float(time_end-time_start)
        self.assertGreater(information.login_time,costtime,'登录超时，性能不达标')
        self.assertEqual(network, 'Network', 'Network节点没有刷新出来')
        self.assertEqual(quicklinks, 'Quick Links', 'Quick Links节点没有刷新出来')
        self.assertEqual(search_template, 'Search Template', 'search_template节点没有刷新出来')
        self.assertEqual(user, information.name, 'search_template节点没有刷新出来')

        
#     @unittest.skip('')
    def test_error_pwd_account(self):
        time.sleep(2)
        self.dr.find_element_by_xpath(information.username).send_keys(information.error_pwd_account)
        self.dr.find_element_by_xpath(information.pwd).send_keys(information.error_pwd_pwd)
        self.dr.find_element_by_xpath(information.login_buton).click()
        time.sleep(2)
        WebDriverWait(self.dr, 50, 0.5).until(EC.presence_of_element_located((By.XPATH,information.msg)))
        msg=self.dr.find_element_by_xpath(information.msg).text
        self.assertEqual(msg, 'Invalid password, you have 2 attempts before your account is locked.', msg)
        time.sleep(2)
        self.dr.find_element_by_xpath(information.username).clear()
        self.dr.find_element_by_xpath(information.pwd).clear()
        self.dr.find_element_by_xpath(information.username).send_keys(information.error_pwd_account)
        self.dr.find_element_by_xpath(information.pwd).send_keys(information.error_pwd_pwd)
        self.dr.find_element_by_xpath(information.login_buton).click()
        WebDriverWait(self.dr, 50, 0.5).until(EC.presence_of_element_located((By.XPATH,information.msg)))
        time.sleep(2)
        msg1=self.dr.find_element_by_xpath(information.msg).text
        self.assertEqual(msg1, 'Invalid password, you have only 1 attempt before your account is locked.', msg1)
        time.sleep(2)
        self.dr.find_element_by_xpath(information.username).clear()
        self.dr.find_element_by_xpath(information.pwd).clear()
        self.dr.find_element_by_xpath(information.username).send_keys(information.error_pwd_account)
        self.dr.find_element_by_xpath(information.pwd).send_keys(information.error_pwd_pwd)
        self.dr.find_element_by_xpath(information.login_buton).click()
        WebDriverWait(self.dr, 50, 0.5).until(EC.presence_of_element_located((By.XPATH,information.msg)))
        time.sleep(2)
        msg2=self.dr.find_element_by_xpath(information.msg).text
        self.assertEqual(msg2, 'Your account has been locked out due to too many invalid login attempts.', msg2)

 



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()