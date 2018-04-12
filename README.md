# webpy-github-login
------------------------
目标：web.py框架使用github登录
利用github的oauth2协议的code验证

* 

## 环境准备

为了让自己更易理解，在ubuntu上跑应用，在虚拟机的win7上演示
主机ubunut的IP地址：192.168.0.128
在win7的浏览器地址栏里访问：192.168.0.128:8080

## 注册github的oauth应用

![](https://raw.githubusercontent.com/D0ggy/MarkDownPhoto/master/webpy-gihub-login/develo-setting.png)
![](https://raw.githubusercontent.com/D0ggy/MarkDownPhoto/master/webpy-gihub-login/client_idsecrit_id.png)
![](https://raw.githubusercontent.com/D0ggy/MarkDownPhoto/master/webpy-gihub-login/url_callback.png)


## 大概流程

* 在界面写一个按钮，附带网址如下，`使用github登录`，跳转到github验证登录的页面，其中放进了client_id和redirect_url
**https://github.com/login/oauth/authorize?`client_id=19f2e6d6a157b86e559e&redirect_uri=http://192.168.0.128:8080/login`**

![](https://raw.githubusercontent.com/D0ggy/MarkDownPhoto/master/webpy-gihub-login/zhuye.png)
![](https://github.com/D0ggy/MarkDownPhoto/blob/master/webpy-gihub-login/github-hutao.png)

* 在同意后，一般情况下，用户被重定向之后会显示登录成功了，下面的几步是看不到的，下面是由webpy应用的后台完成的
github在重定向的网址上加了`code`,
**http://192.168.0.128:8080/login?code=0j23mf4nf09s0jf**

* 后台接收`code`后，带着这个参数去向`github`请求令牌
**https://github.com/login/oauth/access_token?client_id=19f2e6d6a157b86e559e&`code=0j23mf4nf09s0jf`&redirect_uri=http://192.168.0.128:8080/login**

* 上面的请求直接得到相应的令牌`access_token`,不会出现新网页，
携带者令牌获取用户信息
**https://api.github.com/user?access_token=××××××**


## 打印出用户的几条信息

![](https://raw.githubusercontent.com/D0ggy/MarkDownPhoto/master/webpy-gihub-login/hadToken.png)

