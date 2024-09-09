"""
-*- coding: UTF-8 -*-
@author: yuanhai
@time: 2022/11/10 11:14
desc:

"""
import requests
from lxml import etree
from requests.packages import urllib3

url = 'https://www.qb5.tw/login.php'
headers = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
}
#创建session对象
session = requests.session()
#获取链接
pag_text = session.get(url=url,headers=headers).text
#实例化一个etree对象，方便后续对页面进行数据解析
tree = etree.HTML(pag_text)
print(tree)
#验证码提取地址
img_path = 'https://www.qb5.tw'+tree.xpath('//*[@id="main"]/div[1]/form/fieldset/p[3]/img/@src')[0]
# print(img_path)
#下载验证码，以二进制的方式保存
img_content = session.get(img_path,headers=headers,verify=False).content
with open('./img.png','wb') as f:
    f.write(img_content)
    print('图片下载成功!')
img_code = input('请输入验证码:')
#准备登录需要的参数，用户名，密码，验证码
data = {
    'username': 'test123',
    'password': 'admin@123',
    'checkcode': img_code,
    'usecookie': '315360000',
    'action': 'login',
    'submit': '立即登陆'
}
# 判断是否登录成功
response = session.post(url=url,data=data,headers=headers,verify=False)
response.encoding = 'gbk'      #编码防止乱码
response_text = response.text
if "登录成功"  in response_text:
    print("登陆成功")
# 请求个人信息页
ge = session.get(url='https://www.qb5.tw/userdetail.php',headers=headers,verify=False)
with open('xs.html','w',encoding='gbk') as f:
    f.write(ge.text)