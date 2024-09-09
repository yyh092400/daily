# coding=gbk
import random

import requests #请求网站
import json #数据解析
import pandas as pd


headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
    "Connection": "close"
}

#https://wp.m.163.com/163/page/news/virus_report/index.html?nw=1&anw=1
url = 'https://c.m.163.com/ug/api/wuhan/app/data/list-total'

re = requests.get(url=url, headers=headers,timeout=10)  # 请求接口
# print(re.text)
re.encoding = re.apparent_encoding
status = re.status_code
data_json = json.loads(re.text)
# print(status)
# print(data_json)
data = data_json['data']['areaTree'][2]['children'][8]['children'][0]
# print(data)
data_over = data['today']['confirm']
print('成都今日新增确诊病例：',data_over)
re.close()