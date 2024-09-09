import requests
from bs4 import BeautifulSoup

url = 'https://unsplash.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# 在网页源代码中找到所有图片标签
images = soup.find_all('img')

# 遍历每个图片标签，获取图片地址
for image in images:
    src = image['src']
    print(src)
