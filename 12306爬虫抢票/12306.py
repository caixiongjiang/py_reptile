import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver import ChromeOptions
from selenium.webdriver.support.select import Select #引入select包，为了下拉列表使用
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class Login12306():
    # Chrome浏览器绕过webdriver检测，可以成功滑窗
    # 这种方式浏览器没监测到是自动测试工具
    def __init__(self, url, login_user, login_passwd):
        option = ChromeOptions()
        option.add_experimental_option('excludeSwitches', ['enable-automation'])
        self.driver = webdriver.Chrome(options=option)
        self.driver.get(url)
        script = 'Object.defineProperty(navigator, "webdriver", {get:()=>undefined,});'
        self.driver.execute_script(script)
        self.driver.maximize_window() #最大化窗口
        self.login_user = login_user
        self.login_passwd = login_passwd
        self.init_url = url

    def Login(self):
        # 点击选择账号登录
        wait = WebDriverWait(self.driver, 60, 0.1)
        account_login = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.login-hd-code a')))#J-password
        account_login.click()

        # 输入用户名密码
        user_input = self.driver.find_element(By.XPATH, '//*[@id="J-userName"]')
        user_input.send_keys(self.login_user)
        time.sleep(1)
        passwd_input = self.driver.find_element(By.XPATH, '//*[@id="J-password"]')
        passwd_input.send_keys(self.login_passwd)
        time.sleep(1)
        login_btn = self.driver.find_element(By.XPATH, '//*[@id="J-login"]')
        login_btn.click()

        # 滑窗验证处理
        time.sleep(1)
        span = self.driver.find_element(By.XPATH, '//*[@id="nc_1_n1z"]')
        actions = ActionChains(self.driver)
        actions.click_and_hold(span)
        actions.drag_and_drop_by_offset(span, 350, 0)
        actions.perform()

        # 通过url变化与否判断是否登录成功
        time.sleep(2)
        print('current_url: ', self.driver.current_url)
        if self.driver.current_url == self.init_url:
            # 网页没跳转, 判断是否提示错误信息
            err_login = self.driver.find_element(By.CSS_SELECTOR, 'div.login-error')
            if err_login:
                if err_login.is_displayed():
                    print('Login Error!')
        else:
            try:
                # 登录成功后，关闭弹出的对话框
                modal = self.driver.find_element(By.CSS_SELECTOR, 'div.modal')
                confirm_btn = self.driver.find_element(By.CSS_SELECTOR, 'div.modal > div.modal-ft > a')
                confirm_btn.click()
                print("登录成功")
            except NoSuchElementException:
                print('NoSuchElementException')
            self.driver.find_element(By.XPATH, '//*[@id="J-index"]/a').click()

    def Purchase(self):
        #点击跳到首页
        departure = input("请输入出发地：")
        destination = input("请输入目的地：")
        date = input("请输入日期（年-月-日）：")
        isStudent = input("是否为学生票（输入Y代表是，其他代表不是）：")
        print("座位类型：特等座/商务座  一等座 二等座/二等包座 高级软卧 软卧/一等卧 动卧 硬卧/二等卧 软座 硬座 无座 其他")
        type = input("请输入座位类型：")
        if isStudent == "y" or isStudent == "Y":
            flag = True
        else:
            flag = False
        #time.sleep(5)
        self.driver.find_element(By.XPATH, '//*[@id="toolbar_Div"]/div[3]/div[2]/div/div[1]/div/div[2]/div[1]/div[1]/div[1]/div[1]/label').click()
        self.driver.find_element(By.XPATH, '//*[@id="fromStationText"]').send_keys(departure, Keys.ENTER)
        #time.sleep(2)
        self.driver.find_element(By.XPATH, '//*[@id="toolbar_Div"]/div[3]/div[2]/div/div[1]/div/div[2]/div[1]/div[1]/div[1]/div[2]/label').click()
        self.driver.find_element(By.XPATH, '//*[@id="toStationText"]').send_keys(destination, Keys.ENTER)
        #time.sleep(2)
        #先将默认值清空,再输入
        self.driver.find_element(By.XPATH, '//*[@id="train_date"]').clear()
        self.driver.find_element(By.XPATH, '//*[@id="train_date"]').send_keys(date)
        #time.sleep(2)
        if flag:
            self.driver.find_element(By.XPATH, '//*[@id="isStudentDan"]').click()
        #time.sleep(2)
        self.driver.find_element(By.XPATH, '//*[@id="search_one"]').click()

        #转换到最后一个页面
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.driver.find_element(By.XPATH, '//*[@id="qd_closeDefaultWarningWindowDialog_id"]').click()

        #点击到能预定的车次
        self.driver.find_element(By.XPATH, '//*[@id="sear-result"]/span/label[2]').click()
        # 解析车次信息
        WebDriverWait(self.driver, 1000).until(
            EC.presence_of_all_elements_located((By.XPATH, "//tbody[@id='queryLeftTable']/tr"))
        )
        tran_trs = self.driver.find_elements(By.XPATH, "//tbody[@id='queryLeftTable']/tr[not(@datatran)]")

        infos = [[] for y in range(40)] #定义一个二维数组，y的维度定为40，因为1天的车次一般不会超过40

        types = ["特等座/商务座", "一等座", "二等座/二等包座", "高级软卧", "软卧/一等卧", "动卧", "硬卧/二等卧", "软座", "硬座", "无座", "其他"]
        for i in range(len(types)):
            if types[i] == type:
                type_id = i + 7
                break
        '''
        注意infos存储的是网页上所有车次的信息，没有筛选座位类型的结果
        '''
        index = 1 #网页上真实的次序
        for tran_tr in tran_trs:
            infos[index - 1] = tran_tr.text.replace('\n', ' ').split(' ')
            #去除多余字段
            if infos[index - 1][1] == "复":
                infos[index - 1].remove("复")
            if infos[index - 1][type_id] == "--" or infos[index - 1][type_id] == "无":
                index += 1
                continue
            #打印有此座位类型的余票信息
            print("=============================================================================================================================================================================")
            print("序号：", end = "")
            print(str(index), end="")
            print("  车次：" + infos[index - 1][0], end="")
            print("  出发站-到达站：" + infos[index - 1][1] + "-" + infos[index - 1][2], end="")
            print("  出发时间-到达时间：" + infos[index - 1][3] + "-" + infos[index - 1][4], end="")
            print("  历时：" + infos[index - 1][5] + " " + infos[index - 1][6], end="")
            print("  特等座/商务座：" + infos[index - 1][7], end="")
            print("  一等座：" + infos[index - 1][8], end="")
            print("  二等座/二等包座：" + infos[index - 1][9], end="")
            print("  高级软卧：" + infos[index - 1][10], end="")
            print("  软卧/一等卧：" + infos[index - 1][11], end="")
            print("  动卧：" + infos[index - 1][12], end="")
            print("  硬卧/二等卧：" + infos[index - 1][13], end="")
            print("  软座：" + infos[index - 1][14], end="")
            print("  硬座：" + infos[index - 1][15], end="")
            print("  无座：" + infos[index - 1][16], end="")
            print("  其他：" + infos[index - 1][17])
            index += 1

        while(1):
            select = input("请输入要选择的班次序号：")
            if int(select) > index:
                print("请输入正确的次序号！")
                continue
            break

        #点击预定
        btns = self.driver.find_elements(By.CLASS_NAME, 'btn72')
        for i in range(len(btns)):
            if i == int(select) - 1: #select从1开始，i从0开始
                btns[i].click()
                break
        time.sleep(1)
        #如果操作时间过长就要继续进行验证（虽然前面已经登录了还是要验证）

        #输入用户名和密码,点击登录
        # self.driver.find_element(By.XPATH, '//*[@id="J-userName"]').send_keys(self.login_user)
        # self.driver.find_element(By.XPATH, '//*[@id="J-password"]').send_keys(self.login_passwd)
        # self.driver.find_element(By.XPATH, '//*[@id="J-login"]').click()
        # time.sleep(0.5)

        #滑块验证
        # span = self.driver.find_element(By.XPATH, '//*[@id="nc_1_n1z"]')
        # actions = ActionChains(self.driver)
        # actions.click_and_hold(span)
        # actions.drag_and_drop_by_offset(span, 350, 0)
        # actions.perform()


        #选择票类型和乘客类型
        if flag: #(学生票)
            self.driver.find_element(By.XPATH, '//*[@id="normal_passenger_id"]/li[1]/label').click()
        self.driver.find_element(By.XPATH, '//*[@id="dialog_xsertcj_ok"]').click()

        #下拉框选择
        options_element = self.driver.find_element(By.XPATH, '//*[@id="seatType_1"]')
        options = Select(options_element)
        for i in range(len(options)):
            select.select_by_visible_text(type)

        #提交订单
        self.driver.find_element(By.XPATH, '//*[@id="submitOrder_id"]').click()
        print(" 窗 | A | B | C | 过道 | D | F | 窗 ")
        dest_el = self.driver.find_elements(By.CSS_SELECTOR, 'rect')
        while(1):
            dest = input("请选择你的座位序号：")
            if dest == 'A':
                dest_el[0].click()
            elif dest == 'B':
                dest_el[1].click()
            elif dest == 'C':
                dest_el[2].click()
            elif dest == 'D':
                dest_el[3].click()
            elif dest == 'F':
                dest_el[4].click()
            else:
                print("请输入正确的座位")
                continue
            break
        time.sleep(1)
        #最后确认
        self.driver.find_element(By.XPATH, '//*[@id="qr_submit_id"]').click()
        print("订票成功！")

def main():
    url = 'https://kyfw.12306.cn/otn/resources/login.html'
    login_user = input("Input Username: ")
    login_passwd = input("Input Password: ")
    global login  # 避免chrome浏览器驱动在程序执行完后自动关闭浏览器
    login = Login12306(url, login_user, login_passwd)
    login.Login()
    login.Purchase()



if __name__ == '__main__':
    main()