import requests

def get():
    print("\nget")
    param = {"wd" : "莫烦Python"}
    r = requests.get('http://www.baidu.com/s', params = param)
    print(r.url)
    #print(r.text)

def post_name():
    print("\npost name")
    data = {'firstname': '莫烦', 'lastname': '周'}
    r = requests.post('http://pythonscraping.com/files/processing.php', data=data)#这里的网页是你登录请求之后显示的网页url
    print(r.text)
    # Hello there, 莫烦 周!

def post_image():
    print("\npost image")
    file = {"uploadFile" : open("./image.png", "rb")}#open里面放的是本体文件的路径
    r = requests.post("http://pythonscraping.com/files/processing2.php", files=file)
    print(r.text)

def post_login():
    print("\npost login")
    payload = {'username': 'Morvan', 'password': 'password'}
    r = requests.post('http://pythonscraping.com/pages/cookies/welcome.php', data=payload)
    print(r.cookies.get_dict())

    # {'username': 'Morvan', 'loggedin': '1'}

    r = requests.get('http://pythonscraping.com/pages/cookies/profile.php', cookies=r.cookies)
    print(r.text)

def session_login():
    print("\nsession login")
    session = requests.Session()
    payload = {'username': 'Morvan', 'password': 'password'}
    r = session.post('http://pythonscraping.com/pages/cookies/welcome.php', data=payload)
    print(r.cookies.get_dict())

    # {'username': 'Morvan', 'loggedin': '1'}

    r = session.get("http://pythonscraping.com/pages/cookies/profile.php")
    print(r.text)

get()
post_name()
#post_image()
post_login()
session_login()