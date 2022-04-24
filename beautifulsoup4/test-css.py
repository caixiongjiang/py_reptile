from bs4 import BeautifulSoup #引入beautifulsoup4模块
from urllib.request import urlopen

# 全局取消证书验证(防止爬取网页源码的时候报错)
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

import re

def main():
    # if has Chinese, apply decode()
    html1 = urlopen("https://mofanpy.com/static/scraping/list.html").read().decode('utf-8')
    print(html1)
    soup = BeautifulSoup(html1, features='lxml') #解析形式为lxml（效率更高），需要单独下载库
    '''
    使用class去解析css
    '''
    month = soup.find_all('li', {"class": "month"})#返回class为month的所有标签内容（没有去掉标签的信息）
    print(month)#这里没有去掉标签信息
    for m in month:
        print(m.get_text()) #注意这里会自动换行

    jan = soup.find('ul', {"class": 'jan'})
    d_jan = jan.find_all('li')  # use jan as a parent
    for d in d_jan:
        print(d.get_text())

if __name__ == '__main__':
    main()