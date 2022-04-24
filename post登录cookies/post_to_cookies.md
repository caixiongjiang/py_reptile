## post登录cookies

* post请求
    * 账号登录
    * 搜索内容
    * 上传图片
    * 往服务器传数据
* get
    * 正常打开网页
    * 不往服务器传数据

### 使用requests

requests是一个python的外部模块包，手动安装：
```shell
# python2+
pip install requests
# python 3+
pip3 install requests
```

一半来说登录模块的tag一般为form

### 登录
登录账号做了什么：
* 使用 post 方法登录了第一个红框的 url
* post 的时候, 使用了 Form data 中的用户名和密码
* 生成了一些 cookies

### 使用 Session 登录
不过每次都要传递 cookies 是很麻烦的, 好在 requests 有个很 handy 的功能, 那就是 Session. 在一次会话中, 我们的 cookies 信息都是相连通的, 它自动帮我们传递这些 cookies 信息. 

同样是执行上面的登录操作, 下面就是使用 session 的版本. 创建完一个 session 过后, 我们直接只用 session 来 post 和 get. 而且这次 get 的时候, 我们并没有传入 cookies. 但是实际上 session 内部就已经有了之前的 cookies 了.