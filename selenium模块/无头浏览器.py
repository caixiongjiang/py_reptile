#浏览器在后台默默运行
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select #引入select包，为了下拉列表使用

#准备好参数配置（无头浏览器）
opt = Options()
opt.add_argument("--headless")
opt.add_argument("--disable-gpu") #不显示

web = Chrome(options=opt)

web.get("https://ys.endata.cn/BoxOffice/Ranking")
'''
#如果为下拉列表如何定位？
select_element = web.find_element_by_xpath('//*[@id="OptionDate"]')
#对元素进行包装，包装成下拉菜单
select = Select(select_element)
#调整选项（option标签）
for i in range(len(select.options)):
    # i 为每一个下拉框的索引位置
    select.select_by_index(i) #根据索引选择
    time.sleep(2)
    table = web.find_element_by_xpath('//*[@id="TableList"]/table')
    print(table.text) #打印所有的文本信息
    #select.select_by_value() #根据value值进行选择
    #select.select_by_visible_text() #按照文本值进行切换
'''

#定位到国产片页面
web.find_element_by_xpath('//*[@id="app"]/section/main/div/div[1]/div/section/section/section/div/label[2]/span').click()
table = web.find_element_by_xpath('//*[@id="app"]/section/main/div/div[1]/div/section/section/section/section/div[1]').text
print(table)

# 如何拿到页面代码（转码生效之后的效果elements而不是页面源代码）
print(web.page_source)