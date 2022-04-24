#导入谷歌浏览器驱动模块,鼠标驱动模块
import time

from selenium.webdriver import Chrome, ActionChains
from selenium.webdriver.common.by import By
#导入驱动选项包
from selenium.webdriver.chrome.options import Options

#去掉自动化标志
option = Options()
option.add_experimental_option('excludeSwitches', ['enable-automation'])
option.add_argument('--disable-blink-features=AutomationControlled')


web = Chrome(options=option)
web.get("https://kyfw.12306.cn/otn/resources/login.html")

'''
目前使用滑块验证
'''
#输入用户名
web.find_element(By.XPATH, '//*[@id="J-userName"]').send_keys("18358927373")
#输入密码
web.find_element(By.XPATH, '//*[@id="J-password"]').send_keys("6116226cai")
#点击登录
web.find_element(By.XPATH, '//*[@id="J-login"]').click()

#添加隐式等待
web.implicitly_wait(5)

'''
破解滑块验证
'''
#定位滑块
box = web.find_element(By.XPATH, '//*[@id="nc_1_n1z"]')
#使用action操作鼠标
action = ActionChains(web)
#鼠标移动到滑块
action.move_to_element(box)
#鼠标按住滑块
action.click_and_hold(box)
#水平拖动滑块（12306大约为340，这里设置为400）
action.move_by_offset(400,0)
#放开鼠标
action.release()
#执行
action.perform()
time.sleep(2)


