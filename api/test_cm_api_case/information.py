'''
Created on Nov 16, 2020

@author: Administrator
'''
import hashlib
#登录基础信息
username='monster'  # 登录账号
pwd='monster'        #登录密码
password=hashlib.md5(pwd.encode(encoding='UTF-8')).hexdigest()  #md5加密后的密码
ip='http://10.0.100.125:9023'
domain='https://srf.test.com'
address="srf.test.com"
terminal='10.0.100.99' #使用终端
clip_contentid='0fa29c886e434993ad374bf04ea769fd' #用于获取关键帧   
time=20.00   #接口响应时延  断言用的
path="global_sobey_defaultclass/MaterialList/Public Material/CMS 185P1/yh/KKK"  #新建文件夹的路径
folder_contentid='e418c0aa827ce5f5efc8d697962ca3f5' #用于后面的检索和获取素材元数据 与上面新建文件夹路径必须对应
folder_path="global_sobey_defaultclass/MaterialList/Public Material/CMS 185P1/Stability/target2"  #用于后面的检索
delete_path='global_sobey_defaultclass/MaterialList/Public Material/CMS 185P1/Stability/target2'  #用于后面的删除

move_path='global_sobey_defaultclass/MaterialList/Public Material/CMS 185P1/yh/KKK/move/target'    #用于后面move后的目标文件夹位置
move_folder_path='global_sobey_defaultclass/MaterialList/Public Material/CMS 185P1/yh/KKK/move' #被移动文件夹所在路径
move_folder='global_sobey_defaultclass/MaterialList/Public Material/CMS 185P1/yh/KKK/move/original' #被移动的文件夹
move_folder_contentid='9a80ebe3b2270d0ff84c0488d6188bfd'  #被移动的文件夹contentid

recover_path='global_sobey_defaultclass/MaterialList/Public Material/CMS 185P1/yh/KKK/move'    #用于后面move后的目标文件夹位置
recover_folder_path='global_sobey_defaultclass/MaterialList/Public Material/CMS 185P1/yh/KKK/move/target'  #被移动文件夹所在路径 
recover_folder="global_sobey_defaultclass/MaterialList/Public Material/CMS 185P1/yh/KKK/move/target/original" #被移动的文件夹    #1111111111111111111




#用来获取用户信息 给method用的
login_url=ip+"/CMApi/api/basic/account/login"
login_header={
            "Content-Type": "application/json;charset=UTF-8",
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'     
            }
login_data='{"LOGINSUBSYSTEM":"CM","LOGINIP":"10.0.100.99","LOGINNAME":"'+username+'","LOGINPWD":"'+password+'"}'


#savepic
iconno=20  #第几帧的图片另存

#trim in out 点 百纳秒对对应起止的帧数  下面是25帧的素材  丢帧的素材需要重新计算（除不尽）
nanoSecIn=26800000
nanoSecOut=40000000
trimin=67
trimout=100

#mongodb 基础信息
host='10.0.100.13'
port=27017
user_name='sobeyhive'
user_pwd='$0bEyHive*2o1Six'


#检索模板：
my_tmp_name='tmp2'
share_tmp_name='tmp3'
update_name='tmpppp'
touser='Daaaadb'  #共享检索结果给目标用户组








      
