import re
import requests
import csv
#-*- coding:utf-8 -*-

url = 'https://movie.douban.com/top250'
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36"
}
res = requests.get(url,headers=header).text
# print(res)

#解析数据，正则表达式
obj = re.compile(r'<li>.*?<div class="item">.*?<span class="title">(?P<name>.*?)</span>.*?'
                 r'<br>(?P<year>.*?)&nbsp.*?<span class="rating_num" property="v:average">(?P<score>.*?)</span>' ,re.S)   #re.S可以匹配换行符
#开始匹配
result = obj.finditer(res)
f = open("data.csv",mode="w")
csvwriter = csv.writer(f)
for i in result:
    # #电影名
    name = i.group("name")
    # #年份
    year = i.group("year")
    # #评分
    score = i.group("score")
    print("片名:"+name,"年份:"+year.strip(),"评分:"+score)
      #写到文件里
#     dic = i.groupdict()
#     dic['year'] = dic['year'].strip()
#     csvwriter.writerow(dic.values())
# f.close()
# print("over")