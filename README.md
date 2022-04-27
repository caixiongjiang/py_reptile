## 爬虫入门学习

包含知识：
- 利用自动化测试工具selenium进行爬虫
- 正则表达式
- request请求
- beautifulSoup4
- 验证码第三方工具
    * 超级鹰验证码破解工具
- 下载source图片
- 反识别自动化控制工具使用
    * 如果你的chrome版本小于88，在启动浏览器的时候（此时没有加载任何内容），向页面潜入js代码，去掉webdriver：
  ```python
  from selenium.webdriver import Chrome
  web = Chrome()
  
  web.execute_cdp_cmd("Page.addScriptToEvaluateOnDocument", {
    "source" : """
    navigator.webdriver = undefined
        Object.defineProperty(navigator, 'webdriver', {
            get: () => undefined
        })
    """
  })  
    ```
    * 如果你的chrome版本大于88，引入option
    ```python
  from selenium.webdriver import Chrome
  #导入驱动选项包
  from selenium.webdriver.chrome.options import Options
  #去掉自动化标志(滑块能监测到自动化工具)
  option = Options()
  option.add_experimental_option('excludeSwitches', ['enable-automation'])
  option.add_argument('--disable-blink-features=AutomationControlled')
    ```
  
### 使用selenium 12306爬虫买票
- [12306.py]()