from bs4 import BeautifulSoup #引入beautifulsoup4模块
from urllib.request import urlopen

# 全局取消证书验证(防止爬取网页源码的时候报错)
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

import re

def main():
    # if has Chinese, apply decode()
    html1 = urlopen("https://mofanpy.com/static/scraping/basic-structure.html").read().decode('utf-8')
    print(html1)
    soup = BeautifulSoup(html1, features='lxml') #解析形式为lxml（效率更高），需要单独下载库
    print(soup.h1)#返回h1标签的内容（没有去掉<h1></h1>）
    print('\n', soup.p)#返回p标签的内容（没有去掉<p></p>）

    all_href = soup.find_all('a')#找到所有的a标签的内容（没有去掉<a></a>）
    for l in all_href:
        print(l['href'])

    all_href = [l['href'] for l in all_href]
    print('\n', all_href)


if __name__ == '__main__':
    main()