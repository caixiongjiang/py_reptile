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
#查找存放数据的位置，进行数据提取
#找到页面中所有存放数据的item
item_list = web.find_elements_by_xpath('//*[@id="jobList"]/div[1]/div')
for item in item_list:
    job_name = item.find_element_by_tag_name("a").text
    company_name = item.find_element_by_xpath("./div/div[2]/div/a").text
    job_price = item.find_element_by_xpath("./div/div/div[2]/span").text
    print(job_name, company_name, job_price)

