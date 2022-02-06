# 浙江师范大学-疫情打卡自动填报
<h2>待完成...</h2></br>
浙江师范大学 每日信息填报自动打卡脚本，一次设置，自动打卡，再也不怕班长催，导员赶...</br>
作者：邢小林 </br>
免责声明：仅供学习技术交流，不作任何商业用途 </br>

<!-- PROJECT SHIELDS -->

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

 
## 目录

- [功能介绍](#功能介绍)
- [立即开始](#立即开始)
- [参数修改](#参数修改)
- [部署](#部署)
- [使用到的框架](#使用到的框架)
- [贡献者](#贡献者)
  - [如何参与开源项目](#如何参与开源项目)
- [版本控制](#版本控制)
- [作者](#作者)
- [鸣谢](#鸣谢)

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

**Name:**</br> 
USERS
</br>
**Value:**
```python3
[
    ('张麻子', '202011011001', 'gege'),
    ('汤师爷', '202011011002', 'dollar')
]
```
<img src='image/users.png'></img></br>

4、启动程序
手动点击**Actions**，运行workflow，等待运行... </br>
<img src='image/run.png'></img></br>

运行成功...</br>
如果运行失败可以去查看一下错误信息，联系作者...

### 参数修改
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



### 文件目录说明
eg:

```
filetree 
├── ARCHITECTURE.md
├── LICENSE.txt
├── README.md
├── /account/
├── /bbs/
├── /docs/
│  ├── /rules/
│  │  ├── backend.txt
│  │  └── frontend.txt
├── manage.py
├── /oa/
├── /static/
├── /templates/
├── useless.md
└── /util/

```





### 开发的架构 

请阅读[ARCHITECTURE.md](https://github.com/shaojintian/Best_README_template/blob/master/ARCHITECTURE.md) 查阅为该项目的架构。

### 部署

暂无

### 使用到的框架

- [xxxxxxx](https://getbootstrap.com)
- [xxxxxxx](https://jquery.com)
- [xxxxxxx](https://laravel.com)

### 贡献者

请阅读**CONTRIBUTING.md** 查阅为该项目做出贡献的开发者。

#### 如何参与开源项目

贡献使开源社区成为一个学习、激励和创造的绝佳场所。你所作的任何贡献都是**非常感谢**的。


1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



### 版本控制

该项目使用Git进行版本管理。您可以在repository参看当前可用版本。

### 作者

xxx@xxxx

知乎:xxxx  &ensp; qq:xxxxxx    

 *您也可以在贡献者名单中参看所有参与该项目的开发者。*

### 版权说明

该项目签署了MIT 授权许可，详情请参阅 [LICENSE.txt](https://github.com/shaojintian/Best_README_template/blob/master/LICENSE.txt)

### 鸣谢


- [GitHub Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet)
- [Img Shields](https://shields.io)
- [Choose an Open Source License](https://choosealicense.com)
- [GitHub Pages](https://pages.github.com)
- [Animate.css](https://daneden.github.io/animate.css)
- [xxxxxxxxxxxxxx](https://connoratherton.com/loaders)

<!-- links -->
[your-project-path]:shaojintian/Best_README_template
[contributors-shield]: https://img.shields.io/github/contributors/shaojintian/Best_README_template.svg?style=flat-square
[contributors-url]: https://github.com/shaojintian/Best_README_template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/shaojintian/Best_README_template.svg?style=flat-square
[forks-url]: https://github.com/shaojintian/Best_README_template/network/members
[stars-shield]: https://img.shields.io/github/stars/shaojintian/Best_README_template.svg?style=flat-square
[stars-url]: https://github.com/shaojintian/Best_README_template/stargazers
[issues-shield]: https://img.shields.io/github/issues/shaojintian/Best_README_template.svg?style=flat-square
[issues-url]: https://img.shields.io/github/issues/shaojintian/Best_README_template.svg
[license-shield]: https://img.shields.io/github/license/shaojintian/Best_README_template.svg?style=flat-square
[license-url]: https://github.com/shaojintian/Best_README_template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/shaojintian
