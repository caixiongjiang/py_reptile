import time

from selenium.webdriver import Chrome #导入谷歌浏览器驱动
from selenium.webdriver.common.keys import Keys #导入键盘按钮包

#创建浏览器对象
web = Chrome()

#如果页面遇到了iframe如何处理
web.get("https://91kanju.com/vod-play/33706-3-1.html")
time.sleep(1)

#处理iframe的话，必须先拿到iframe，然后切换视角到iframe(也就是iframe是一个子网页)，然后才可以拿数据
iframe = web.find_element_by_xpath('//*[@id="player_iframe"]')
web.switch_to.frame(iframe) #切换到iframe
#web.switch_to.default_content() #切回默认窗口（往回切）
#在iframe内部找东西

