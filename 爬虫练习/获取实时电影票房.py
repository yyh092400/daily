"""
-*- coding: UTF-8 -*-
@author: yuanhai
@time: 2022/10/31 13:43
desc:

"""
#requests  pip install requests
#BeautifulSoup-->pip install BeautifulSoup4



import requests
from bs4 import BeautifulSoup

#1.请求电影票房网站
header = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"}
text = requests.get("https://piaofang.maoyan.com/dashboard",headers="").text

page_text = text.encode('utf-8')
#2.使用beautifulsoup进行解析
main_page = BeautifulSoup(page_text,"html.parser")    #解析器

#把整个数据页给爬取下来，table页
table = main_page.find("table",{"class":"dashboard-table"})
#在用find_all把每行数据爬取出来

trs = table.find_all("tr")

for tr in trs:
    lst = tr.find_all("td")
    if len(lst) != 0:
        for td in lst:    #拿到每一个td
            print(td.text)       #文本数据
