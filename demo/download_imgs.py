from bs4 import BeautifulSoup
import requests
import os
os.makedirs('./imgs/', exist_ok=True)

URL = "https://caixiongjiang.github.io/blog/2022/stl%E6%BA%90%E7%A0%81%E5%89%96%E6%9E%90/stl%E6%BA%90%E7%A0%81%E5%89%96%E6%9E%90%E7%AC%AC10%E8%AE%B2-%E5%AD%A6%E4%B9%A0%E7%AC%94%E8%AE%B0/"

html = requests.get(URL).text
soup = BeautifulSoup(html, "lxml")
img_url = soup.find_all("div",{"class" : "post-list-container post-list-container-shadow"} )

for ul in img_url:
    imgs = ul.find_all('img')
    for img in imgs:
        url = img['src']
        r = requests.get(url, stream=True)
        img_name = url.split('/')[-1] #提取'/'分割后的最后一个元素（也就是最后一个/之后的名字）
        with open("./imgs/%s" % img_name, "wb") as f:
            for chunk in r.iter_content(chunk_size=128):
                f.write(chunk)
        print('Saved %s' %img_name)

os.system("clear")