import time

from selenium.webdriver import Chrome #导入谷歌浏览器驱动
from selenium.webdriver.common.keys import Keys #导入键盘按钮包

#创建浏览器对象
web = Chrome()
#打开一个网址
web.get("http://lagou.com")
#找到某个元素，点击它："全国"
el = web.find_element_by_xpath('//*[@id="changeCityBox"]/p[1]/a')
el.click() #点击事件
'''
加载需要时间
'''
time.sleep(1) #缓冲1s，加载东西

#找到输入框，输入c++ => 回车或者点击搜索
el1 = web.find_element_by_xpath('//*[@id="search_input"]').send_keys("c++", Keys.ENTER)

time.sleep(1)

#点击跳转页面 打开新窗口
web.find_element_by_xpath('//*[@id="jobList"]/div[1]/div[4]/div[1]/div[1]/div[1]/a').click()

#进入新窗口进行提取，（在selenium眼中，新窗口是默认不切换过来的）
web.switch_to.window(web.window_handles[-1]) #切换到最后一个选项卡

#在新窗口中提取内容
job_detail = web.find_element_by_xpath('//*[@id="job_detail"]/dd[2]/div').text
print(job_detail)

#关掉子窗口
web.close()
#变更selenium视角，回到原来窗口中
web.switch_to.window(web.window_handles[0])
print(web.find_element_by_xpath('//*[@id="jobList"]/div[1]/div[4]/div[1]/div[1]/div[1]/a').text)
