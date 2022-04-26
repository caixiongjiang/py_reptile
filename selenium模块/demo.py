import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import Chrome #导入谷歌浏览器驱动
from selenium.webdriver.common.by import By

#创建浏览器对象
opt = Options()
opt.add_argument("--headless")
opt.add_argument("--disable-gpu") #不显示

driver = Chrome(options=opt)

#打开一个网址
driver.get("https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc&fs=%E5%8D%97%E6%98%8C,NCG&ts=%E8%B5%A3%E5%B7%9E,GZG&date=2022-04-28&flag=Y,N,Y")
time.sleep(1)

driver.find_element(By.XPATH, '/html/body').click()

driver.find_element(By.XPATH, '//*[@id="sear-result"]/span/label[2]').click()
#解析车次信息
WebDriverWait(driver,1000).until(
    EC.presence_of_all_elements_located((By.XPATH,"//tbody[@id='queryLeftTable']/tr"))
)
tran_trs=driver.find_elements_by_xpath("//tbody[@id='queryLeftTable']/tr[not(@datatran)]")
selects = driver.find_elements(By.TAG_NAME, 'b')
for tran_tr in tran_trs:
    infos=tran_tr.text.replace('\n',' ').split(' ')
    print(infos)
num = 1
id = input("id:")
for select in selects:
    if num == id:
        select.click()
        break
    num += 1

