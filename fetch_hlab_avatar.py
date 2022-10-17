import urllib.request
from urllib.request import urlopen
from bs4 import BeautifulSoup as bf
from urllib.request import urlretrieve
import argparse
import os
import socket

def get_host_ip():
    """
    查询本机ip地址
    :return: ip
    """
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip

def pachong(suffix, enable_proxy):
    # 设置代理
    proxy_handler = urllib.request.ProxyHandler({"https": 'http://'+get_host_ip()+':4780'})
    null_proxy_handler = urllib.request.ProxyHandler({})
    if enable_proxy:
        opener = urllib.request.build_opener(proxy_handler)
    else:
        opener = urllib.request.build_opener(null_proxy_handler)
    urllib.request.install_opener(opener)
    # 目标网址
    html = urlopen("https://www.roboticmanipulation.org/members/"+suffix)
    # html_text = bytes.decode(html.read())
    obj = bf(html.read(), 'html.parser')
    pic_info = obj.find_all('img')

    if os.path.exists(f'images/avatars_{suffix}'):
        print("文件夹已存在")
    else:
        os.mkdir(f'images/avatars_{suffix}')

    logo_pic_info = obj.find_all('img', class_="")
    for index, _ in enumerate(pic_info):
        logo_url = logo_pic_info[index]['data-src']
        print(logo_url)
        if os.path.exists(f'images/avatars_{suffix}/avatar_{index}.png'):
            print(f'文件 images/avatars_{suffix}/avatar_{index}.png 已存在')
        else:
            urlretrieve(logo_url, f'images/avatars_{suffix}/avatar_{index}.png')


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--suffix', type=str, default='', help='website suffix')
    parser.add_argument('-p', '--proxy', action='store_true', help='using a proxy')
    args = parser.parse_args()

    pachong(suffix=args.suffix, enable_proxy=args.proxy)
