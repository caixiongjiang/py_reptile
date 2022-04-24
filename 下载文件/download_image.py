import os


os.makedirs('./imgs/', exist_ok=True) #新建文件夹

# 全局取消证书验证(防止爬取网页源码的时候报错)
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

IMAGE_URL = "https://blog-1311257248.cos.ap-nanjing.myqcloud.com/imgs/stl/img10_3.jpg"

def urllib_download():
    from urllib.request import urlretrieve
    urlretrieve(IMAGE_URL, './imgs/image1.png')

def request_download():
    import requests
    r = requests.get(IMAGE_URL)
    with open('./imgs/image2.png', 'wb') as f:
        f.write(r.content)

def chunk_download():
    import requests
    r = requests.get(IMAGE_URL, stream=True)  # stream loading(实时下载)

    with open('./imgs/image3.png', 'wb') as f:
        for chunk in r.iter_content(chunk_size=32):#每次写入文件的字节数chunk_size
            f.write(chunk)

urllib_download()
request_download()
chunk_download()