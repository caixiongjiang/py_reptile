import time

from selenium.webdriver import Chrome #导入谷歌浏览器驱动
from selenium.webdriver.common.by import By

#创建浏览器对象
driver = Chrome()
#打开一个网址
driver.get("https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc&fs=%E5%8D%97%E6%98%8C,NCG&ts=%E8%B5%A3%E5%B7%9E,GZG&date=2022-04-28&flag=Y,N,Y")
time.sleep(1)

driver.find_element(By.XPATH, '/html/body').click()

driver.find_element(By.XPATH, '//*[@id="sear-result"]/span/label[2]').click()
index = 1
while index:
    item = driver.find_element(By.XPATH, '//*[@id="queryLeftTable"]/tr[' + str(index) + ']').text
    item1 = item.split('\n')
    print(item1)
    index += 2