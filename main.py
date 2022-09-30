import urllib.request
from urllib.request import urlopen
from bs4 import BeautifulSoup as bf
from urllib.request import urlretrieve
import os
# 设置代理
enable_proxy = True
proxy_handler = urllib.request.ProxyHandler({"https": 'http://192.168.4.9:4780'})
null_proxy_handler = urllib.request.ProxyHandler({})
if enable_proxy:
    opener = urllib.request.build_opener(proxy_handler)
else:
    opener = urllib.request.build_opener(null_proxy_handler)
urllib.request.install_opener(opener)

# html = urlopen("https://www.roboticmanipulation.org/members/")
html = urlopen("https://www.roboticmanipulation.org/members/alumni/")
# html_text = bytes.decode(html.read())
# print(html_text)

obj = bf(html.read(), 'html.parser')
# title = obj.head.title
# print(title)

pic_info = obj.find_all('img')
# for i in pic_info:
#     print(i)
#

if os.path.exists('avatars'):
    print("文件夹已存在")
else:
    os.mkdir('avatars')

if os.path.exists('alumni_avatars'):
    print("文件夹已存在")
else:
    os.mkdir('alumni_avatars')

logo_pic_info = obj.find_all('img', class_="")
for index, _ in enumerate(pic_info):
    logo_url = logo_pic_info[index]['data-src']
    print(logo_url)
    # urlretrieve(logo_url, 'avatars/avatar_'+str(index)+'.png')
    urlretrieve(logo_url, 'alumni_avatars/avatar_' + str(index) + '.png')
