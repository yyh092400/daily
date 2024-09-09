"""
-*- coding: UTF-8 -*-
@author: yuanhai
@time: 2022/11/29 10:52
desc:

"""
import requests #请求网站
import re

from bs4 import BeautifulSoup

url = 'https://voice.baidu.com/act/newpneumonia/newpneumonia/?from=osari_aladin_banner&city=四川-成都'
header = '"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"'
html = requests.get(url,header).text
main_page = BeautifulSoup(html,"html.parser")
print(main_page)
#正则提取数据
obj = re.compile(r'<p class="ProvinceSummary_1-135-1_1RW2uk ProvinceSummary_1-135-1_3aIcdg ProvinceSummary_1-135-1_pBq9kt"(?P<newAdd>.*?)</p>',re.S)
result = obj.search(html)
# print(result.group())
