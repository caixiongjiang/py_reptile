from urllib.request import urlopen #网络爬虫头文件

# 全局取消证书验证(防止爬取网页源码的时候报错)
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

import re



def main():
    # if has Chinese, apply decode()
    html1 = urlopen("https://mofanpy.com/static/scraping/basic-structure.html").read().decode('utf-8')
    html2 = urlopen("https://caixiongjiang.github.io").read().decode('utf-8')

    res1 = re.findall(r"<title>(.+?)</title>", html1)
    print("\nPage title is: ", res1[0])

    res2 = re.findall(r"<p>(.*?)</p>", html1, flags=re.DOTALL)  # re.DOTALL if multi line
    print("\nPage paragraph is: ", res2[0])

    res3 = re.findall(r'href="(.*?)"', html2)
    print("\nAll links: ", res3)


if __name__ == '__main__':
    main()

