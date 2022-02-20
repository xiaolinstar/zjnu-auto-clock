# 浙江师范大学-疫情打卡自动填报 Beta版本
浙江师范大学 每日信息填报自动打卡脚本，一次设置，自动打卡，再也不怕班长催，导员赶...</br>
免责声明：仅供学习技术交流，不作任何商业用途 </br>

<!-- PROJECT SHIELDS -->

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

 
## 目录

- [功能介绍](#功能介绍)
- [立即开始](#立即开始)
- [参数修改](#参数修改)
- [使用到到技术](#使用到的技术)
- [作者](#作者)

### 功能介绍
- 一次设置打卡参数，每天定时自动打卡
- 简单方便，可以多人打卡
- 支持必要的参数修改，在家or学校，更改一次即可

### 立即开始
你需要有：
- GitHub账户
- 注册登陆地址：https://github.com/

1、克隆该项目模版（下面方法二选一即可）
- fork: 点击右上角的fork，将项目拉去到自己的GitHub仓库 </br>
<img src='image/fork.png'></img>
- Use this template: 点击Code右端的**Use this template**，填写Repository name、Description (可选) </br>
<img src='image/use this template.png'></img> </br>
<img src='image/template.png'></img></br>
2、创建密钥
进入刚刚创建的仓库，点击
**Settings** -> **Secrets** -> **New repository secret** </br>
<img src='image/settings.png'></img></br>
<img src='image/secrets.png'></img></br>

3、添加密钥
添加学生的基本信息，包括学号和密码  
第四个参数可选
- 如果在学校，则可以不填
- 如果在家里，则填写家里的地址: 例如 **河南省 焦作市 沁阳市**  
**Name:**</br> 
  USERS
</br>
**Value:**
```python3
[
    ('汤师爷', '202011011002', 'dollar'),
    ('张麻子', '202011011001', 'gege', '河南省 焦作市 沁阳市'),
]
```
<img src='image/users.png'></img></br>

4、启动程序
手动点击**Actions**，运行workflow，等待运行... </br>
<img src='image/run.png'></img></br>

运行成功...</br>
如果运行失败可以去查看一下错误信息，联系作者...

### 参数修改(默认不需要修改)
1、修改打卡时间
在 .github/workflows/main.yml 中来设置每天运行的时间：
```bash
  on:
    schedule:
      - cron: "30 0 * * *"
```
上述代码表示程序的定时执行，时区是UTC: 分 时 日 月 日 </br>
默认情况下，该脚本定时每天08:30执行，你可以根据自己的需要更改该设置</br>
GitHub的actions提供的服务器定时系统有一定的误差误差和延迟，但是不影响使用</br>

### 使用到的技术

- [python3](https://www.python.org/)
- [python第三方处理http包：requests](https://pypi.org/project/requests/)
- [Github-Actions](https://docs.github.com/en/actions/learn-github-actions)


### 作者

email: xlxing@bupt.edu.cn

<!-- links -->
[contributors-shield]: https://img.shields.io/github/contributors/549506247xxl/zjnu-auto-clock.svg?style=flat-square
[contributors-url]: https://github.com/549506247xxl/zjnu-auto-clock/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/549506247xxl/zjnu-auto-clock.svg?style=flat-square
[forks-url]: https://github.com/549506247xxl/zjnu-auto-clock/network/members
[stars-shield]: https://img.shields.io/github/stars/549506247xxl/zjnu-auto-clock.svg?style=flat-square
[stars-url]: https://github.com/549506247xxl/zjnu-auto-clock/stargazers
[issues-shield]: https://img.shields.io/github/issues/549506247xxl/zjnu-auto-clock.svg?style=flat-square
[issues-url]: https://github.com/549506247xxl/zjnu-auto-clock/issues
