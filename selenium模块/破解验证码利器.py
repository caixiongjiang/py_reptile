# 1.手动写图像识别(对于特定网站，换一个网站就要重写)
# 2.选择互联网上成熟的验证码破解工具
# 超级鹰验证码识别

#使用超级鹰工具 干掉超级鹰登录的验证码
import time

from selenium.webdriver import Chrome
web =  Chrome()
web.get("http://www.chaojiying.com/user/login/")

#导入超级鹰
from chaojiying import Chaojiying_Client

#先处理验证码
img = web.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/form/div/img').screenshot_as_png  #提取页面上的图像截屏保存（字节信息）


chaojiying = Chaojiying_Client('JarsonCai520', '6116226cai', '932445')
dic = chaojiying.PostPic(img, 1902)
verify_code = dic['pic_str'] #解析出来的验证码

# 向页面中填入用户名，密码，验证码
web.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/form/p[1]/input').send_keys("JarsonCai520")
web.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/form/p[2]/input').send_keys("6116226cai")
web.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/form/p[3]/input').send_keys(verify_code)

time.sleep(5)

#登录
web.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/form/p[4]/input').click()