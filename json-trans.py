"""
-*- coding: UTF-8 -*-
@author: yuanhai
@time: 2022/10/28 10:21
desc:

"""
import pandas
import json

# #json文件
# with open('./tmpt/data.json','r',encoding='GBK') as f:
#     print(f,type(f))
#     df=pandas.read_json(f)
# print(df)


#json对象
js=json.dumps([{'name':'源海','age':'22','sex':'man'},{'name':'jack','age':19,'sex':"female"}])
print(type(js))
df=pandas.read_json(js)
print(df)