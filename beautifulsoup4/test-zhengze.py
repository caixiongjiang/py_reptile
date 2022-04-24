from bs4 import BeautifulSoup #引入beautifulsoup4模块
from urllib.request import urlopen

# 全局取消证书验证(防止爬取网页源码的时候报错)
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

import re#正则表达式

def main():
    # if has Chinese, apply decode()
    html1 = urlopen("https://mofanpy.com/static/scraping/table.html").read().decode('utf-8')
    print(html1)
    soup = BeautifulSoup(html1, features='lxml') #解析形式为lxml（效率更高），需要单独下载库
    '''
    使用正则表达式
    '''
    img_links = soup.find_all("img", {"src": re.compile('.*?\.jpg')})#找到img的tag下的src中以.jpg结尾的内容
    print(img_links) #没有去掉标签
    # [<img src="/static/img/course_cover/tf.jpg"/>, <img src="/static/img/course_cover/rl.jpg"/>, <img src="/static/img/course_cover/scraping.jpg"/>]
    for link in img_links:
        print(link['src'])

    course_links = soup.find_all('a', {'href': re.compile('/tutorials*')})
    print(course_links)
    for link in course_links:
        print(link['href'])

if __name__ == '__main__':
    main()