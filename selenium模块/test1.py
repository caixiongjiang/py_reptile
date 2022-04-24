from selenium.webdriver import Chrome #导入谷歌浏览器驱动

#创建浏览器对象
web = Chrome()
#打开一个网址
web.get("http://www.baidu.com")

print(web.title)
