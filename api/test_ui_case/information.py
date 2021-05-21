'''
Created on May 12, 2021

@author: Administrator
'''
#登录使用的账号
normal_account='CMSG1'    #普通账号
normal_pwd='123'     #普通账号密码
error_user_account='cmsgggg2'      #错误账号用户
error_user_pwd='123'       #错误账号用户密码
error_pwd_account='CMSG3'      #错误密码用户
error_pwd_pwd='12345'       #错误密码用户密码
error_userpwd_account='monsterr'      #错误账号密码用户
error_userpwd_pwd='monsterr'       #错误账号密码用户密码
aduser_account='srf.com\yehui'      #错误账号密码用户
aduser_pwd='Sobey123'       #错误账号密码用户密码
norights_account='monster1'      #没有权限账号密码用户
norights_pwd='monster1'       #没有权限账号用户密码
name='yehui'   #AD账户昵称  用来断言


#url
login_url='https://srf.test.com/CMWeb/login.aspx'

#element xpath
username='//*[@id="userName"]'
pwd='//*[@id="pwd"]'
login_buton='//*[@id="login-button"]'
msg='//*[@id="msgtext"]'   #报错信息


#CM主页元素
quciklinks='//*[@id="folder_box"]/div[1]/div/div[1]/div[1]/span[3]'
network='//*[@id="folder_box"]/div[1]/div/div[2]/div[1]/span[3]'
search_template='//*[@id="folder_box"]/div[1]/div/div[3]/div[1]/span[3]'
logout_option='//*[@id="stage_wrapper"]/div[1]/div[2]/div/span[2]'
logout='//*[@id="stage_wrapper"]/div[1]/div[2]/div/span[2]/div/ul/li'
user='//*[@class="username_show"]' #昵称

#登录时延
login_time=10