from bs4 import BeautifulSoup #引入beautifulsoup4模块
from urllib.request import urlopen
import re #正则表达式
import random

# 全局取消证书验证(防止爬取网页源码的时候报错)
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

base_url = "https://baike.baidu.com"
his = ["/item/%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB/5162711"]



def main():
    # if has Chinese, apply decode()
    for i in range(20):
        url = base_url + his[-1] #his[-1]代表列表his里面的倒数第一位元素
        html1 = urlopen(url).read().decode('utf-8')
        soup = BeautifulSoup(html1, features='lxml') #解析形式为lxml（效率更高），需要单独下载库
        print(soup.find('h1').get_text(),  'url:', his[-1])

        '''
        找到所有的链接页
        '''
        sub_urls = soup.find_all("a", {"target": "_blank", "href" : re.compile("/item/(%.{2})+$")})
        #for m in sub_urls:
        #  print(m)

        if len(sub_urls) != 0:
            his.append(random.sample(sub_urls, 1)[0]["href"])
        else:
            his.pop()

if __name__ == '__main__':
    main()