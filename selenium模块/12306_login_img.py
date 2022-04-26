'''
图片验证版本
'''
#导入谷歌浏览器驱动模块,鼠标驱动模块
import time

from chaojiying import Chaojiying_Client
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

time.sleep(1)

web.find_element(By.XPATH, '//*[@id="toolbar_Div"]/div[2]/div[2]/ul/li[1]/a').click()
time.sleep(2)

#先处理验证码
verify_img_element = web.find_element(By.XPATH, '验证码图片的XPATH')
#初始化超级鹰
chaojiying = Chaojiying_Client('JarsonCai520', '6116226cai', '932445')
#识别验证码
dic = chaojiying.PostPic(verify_img_element.screenshot_as_png, 9004)
result = dic['pic_str'] # x1,y1|x2,y2|x3,y3 (字符串)
re_list = result.split("|")
for rs in re_list: #x1,y1
    p_temp = rs.split(",")
    x = int(p_temp[0])
    y = int(p_temp[1])
    #鼠标移动并进行点击 (事件量)
    ActionChains(web).move_to_element_with_offset(verify_img_element, x, y).click().perform() #移动到 以某个"地点"为基准的偏移量为...的地方 最后perform为执行操作的意思

time.sleep(1)
#输入用户名
web.find_element(By.XPATH, '//*[@id="J-userName"]').send_keys("18358927373")
#输入密码
web.find_element(By.XPATH, '//*[@id="J-password"]').send_keys("6116226cai")
#点击登录
web.find_element(By.XPATH, '//*[@id="J-login"]').click()

time.sleep(1)

'''
拖拽滑块
'''
#定位滑块
btn = web.find_element(By.XPATH, '//*[@id="nc_1_n1z"]')
ActionChains(web).drag_and_drop_by_offset(btn, 400, 0).perform()




