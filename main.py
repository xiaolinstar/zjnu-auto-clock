import datetime
import os

import requests
from bs4 import BeautifulSoup

session = requests.Session()
users = eval(os.environ['USERS'])

# 进入登陆页面url
INDEX_API = 'http://zyt.zjnu.edu.cn/h5/index.aspx'

# 账户密码登陆url
LOGIN_API = 'http://zyt.zjnu.edu.cn/H5/Login.aspx?OP=phone_html5'

# 提交打卡信息url
SUBMIT_API = 'http://zyt.zjnu.edu.cn/H5/ZJSFDX/FillIn.aspx'

# 校验是否已经打卡url
FILL_CHECK_API = 'http://zyt.zjnu.edu.cn/H5/ZJSFDX/CheckFillIn.aspx'

INDEX_HEADER = {
    'Upgrade-Insecure-Requests': '1',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) '
                  'Mobile/15E148 MicroMessenger/8.0.26(0x18001a2e) NetType/WIFI Language/zh_CN ',
    'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'keep-alive'
}

LOGIN_HEADER = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) '
                  'Mobile/15E148 MicroMessenger/8.0.26(0x18001a2e) NetType/WIFI Language/zh_CN',
    'Origin': 'http://zyt.zjnu.edu.cn',
    'Upgrade-Insecure-Requests': '1',
    'Referer': 'http://zyt.zjnu.edu.cn/H5/Login.aspx?OP=phone_html5',
    'Content-Length': '475',
    'Connection': 'keep-alive'
}

LOGIN_FORM = {
    # '__VIEWSTATE': '/wEPDwUKMjAwMjg1NDgwNQ9kFgICAw9kFgQCAQ8PFgIeBFRleHQFLea1meaxn+W4iOiMg+Wkp+WtpuaImOeWq+mAmuS/oeaBr'
    #                '+ebtOaKpeezu+e7n2RkAgsPFgIfAGVkZH2Rr9MyTMRw0PsuxdZE7+cP9Kf23Q1a7i9TGaTbOav6',
    '__VIEWSTATE': '/wEPDwUKMjAwMjg1NDgwNQ9kFgICAw9kFgQCAQ8PFgIeBFRleHQFLea1meaxn+W4iOiMg+Wkp+WtpuaImOeWq+mAmuS/oeaBr+ebtOaKpeezu+e7n2RkAgsPFgIfAGVkZOfldlp8yilernQ77ANYC4MaK+y1',
    '__VIEWSTATEGENERATOR': 'C483C0FE',
    'UserText': '',
    'PasswordText': '',
    'btn_Login': '登录 Log In'
}

"""
    需要更新的键值对
    personname personcode txtCreateTime
"""
SUBMIT_HEADER = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'http://zyt.zjnu.edu.cn',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) '
                  'Mobile/15E148 MicroMessenger/8.0.26(0x18001a2e) NetType/WIFI Language/zh_CN',
    'Upgrade-Insecure-Requests': '1',
    'Referer': 'http://zyt.zjnu.edu.cn/H5/ZJSFDX/FillIn.aspx',
    'Content-Length': '2163',
    'Connection': 'keep-alive'
}

SUBMIT_FORM = {
    '__EVENTTARGET': 'btn_save',
    '__EVENTARGUMENT': '',
    '__VIEWSTATE': '/wEPDwUINzYyMjY0MDVkZBrwT90i7l6LtADspTComrtkJ3qr',
    '__VIEWSTATEGENERATOR': '3674067D',
    '__EVENTVALIDATION': '/wEdABmDiPh5NiN/sNOZA+C1WGvLnPdgn5d6iO4LuTjGeN2JM3llOAzR6kycDzMfToHX0QOa6jYEaUq7hqoikcwmGDr/+NNFSi0Taf5OtutYh7ZsYZ5pz8TgUO6tZcvvqH4FHHwTHoOVlUkr7a4y48d8eTzrYdp8PLLcr00Ykm6GIg/QPm2VAoUsguAjookCWDEX54sHQe9Pfyn7J2iyftT+Cg0mL0jfXWdOZUPTgbQHBDwymb6wlsA0YdypgcCl8awhDxBgYuHAmLDqwPtQh9HDEtJjr+c7NEwFf3c5FPeYdSyrXrYIOfZQS7Mh8jWxQ/3S2fHk/wGpGPyEyYtOtvQbZ7eyCWoEiO6Dd+V6RlHl9UDOJYVHlcFqi++psAvZk9q9RG5W1pRfvYYFhXg72yYOmnpySmm9X2U2t6Y11P+J4lVyalm+n0KUg6wbhm42RvKN577lL2zWcbD6zAaEib0znaI8tWsLH8H+NXQUYD4Kkws4BfoJpIr4b0DV7eZFh6tMLUyznw6pK1ioM6RKyI7TbQybM6GxmPMSYX84o4wEmyaB5xD8mMW4pVwMDPFQsiBJWTs=',
    'personname': '邢江波',
    'personcode': '202025200749',
    'txtCreateTime': '',  # 待添加
    'DATA_1': '空白项',
    'DATA_2': '正常',
    'DATA_3': '体温正常',
    'DATA_4': '否',
    'DATA_5': '绿码',
    'DATA_6': '否',
    'DATA_7': '否',
    'DATA_8': '否',
    'DATA_10': '否',
    'DATA_11': '',
    'DATA_9': '是，已经接种加强针',
    'DATA_16': '否',
    'DATA_12': '',
    'DATA_13': '',  # 尚未返校
    'DATA_14': '',  # '家庭地址'
    'DATA_15': '我已知晓并如实填报',
    'hidDATA_1': '空白项',
    'hidDATA_2': '正常',
    'hidDATA_3': '体温正常',
    'hidDATA_4': '否',
    'hidDATA_5': '绿码',
    'hidDATA_6': '否',
    'hidDATA_7': '否',
    'hidDATA_8': '否',
    'hidDATA_9': '是，已经接种加强针',
    'hidDATA_10': '否',
    'hidDATA_11': '',
    'hidDATA_12': '',
    'hidDATA_13': '',  # 尚未返校
    'hidDATA_14': '',  # '家庭地址'
    'hidDATA_15': '我已知晓并如实填报',
    'hidDATA_16': '否',
    'hidDATA_17': ''  # 这个需要再次实验
}

SCHOOL = [
    '浙江师范大学本部校区',
    '浙江师范大学杭州校区',
    '浙江师范大学兰溪校区'
]
USER = 'xlxing@bupt.edu.cn'


class AutoAgent:
    """
    自动打卡机器人，可以实现疫情信息每天自动填报。
    Agent can accomplish automatic filling of epidemic information every day.
    """

    def __init__(self):
        self.index_api = INDEX_API
        self.index_header = INDEX_HEADER

        self.login_api = LOGIN_API
        self.login_header = LOGIN_HEADER
        self.login_form = LOGIN_FORM

        self.submit_api = SUBMIT_API
        self.submit_header = SUBMIT_HEADER
        self.submit_form = SUBMIT_FORM

    def set_cookie(self):
        """
        进入登陆页面，系统随机分配一个cookie
        通过实践发现，该方法可用可不用，直接提交表单也会分配cookie
        为了模拟真实手机请求，加上该段，更不容易被服务器发现是脚本提交
        :return:
        """
        try:
            _ = session.get(
                url=self.index_api,
                headers={**self.index_header}
            )
            # print(session.cookies)
        except Exception as e:
            """
            出现错误，向管理员发送信息...
            """
            print(e)
            print('获取登陆页面发生错误，请联系作者: {}'.format(USER))

    # 输入用户名和密码登陆
    def post_login(self, username, password):
        """
        :param username: 用户名
        :param password: 密码
        :return:
        """

        try:
            """
            post登陆请求，填充header和data，在data中以变量的形势传入'UserText'和'PasswordText'
            """
            login_in = session.post(
                url=self.login_api,
                data={**self.login_form, 'UserText': username, 'PasswordText': password},
                headers={
                    **self.login_header,
                }
            )
            """
                提交表单后，需要对post请求结果进行处理，可能会出现三种情况
                - 请求成功，成功登陆
                - 请求成功，但账号密码错误
                - 请求失败，post请求发生错误
                
                分析：
                请求成功，状态码 200
                请求失败，状态码 非200
                
                登陆成功和失败进入不同但网页界面，可以根据成功登陆和账号密码错误时的response进行判断
            """
            if login_in.status_code != 200:
                print('状态码:', login_in.status_code)
                return False

            result = BeautifulSoup(login_in.text, 'html.parser')
            text_list = result.get_text().split()
            if '用户名或密码错误!' in text_list:
                print('账号/密码错误，请核查...')
                return False
            else:
                print('成功登陆...')
                return True
        except Exception as e:
            """出现错误，向管理员发送错误信息"""
            print(e)
            print('登陆网页发生错误，请联系作者: {}'.format(USER))

    # 提交表单信息
    def submit_info(self, name, username, loc='浙江师范大学本部校区'):
        """
        :param name: 姓名如 张三
        :param username: 账户名如 1234567890
        :param loc: 打卡地址
        :return:
        """
        # 更新填报日期
        self.submit_form['txtCreateTime'] = str(datetime.date.today())
        self.submit_form['personname'] = name
        self.submit_form['personcode'] = username

        if loc not in SCHOOL:
            self.submit_form['DATA_13'] = '尚未返校'
            self.submit_form['DATA_14'] = loc
            self.submit_form['hidDATA_13'] = '尚未返校'
            self.submit_form['hidDATA_14'] = loc
            live = loc.split()
            self.submit_form['hidDATA_17'] = '{}✰{}✰{}'.format(live[0], live[1], live[2])
        else:
            self.submit_form['DATA_13'] = loc
            self.submit_form['hidDATA_13'] = loc
            if loc == SCHOOL[0]:
                live = ['浙江省', '金华市', '婺城区']
            elif loc == SCHOOL[1]:
                live = ['浙江省', '杭州市', '西湖区']
            else:
                live = ['浙江省', '金华市', '兰溪市']
            self.submit_form['hidDATA_17'] = '{}✰{}✰{}'.format(live[0], live[1], live[2])
        try:
            submit_res = session.post(
                url=self.submit_api,
                data={**self.submit_form},
                headers={
                    **self.submit_header,
                }
            )
            if submit_res.status_code != 200:
                print('状态码', submit_res.status_code)
                print('提交发生错误，请联系作者: {}'.format(USER))
        except Exception as e:
            print(e)
            print('提交用户时信息发生错误，请联系作者: {}'.format(USER))

    # 判断是否已经提交过
    def check_submit(self):
        try:
            check = session.get(
                url=FILL_CHECK_API,
                headers={**self.index_header}
            )
            if check.status_code != 200:
                print('状态码:', check.status_code)
                return False
            result = BeautifulSoup(check.text, 'html.parser')
            text_list = result.find(style='display:;').text.split()
            if '感谢您已完成今日表格信息，请明天继续填报。' in text_list:
                print('你已经完成了今日的填报...')
                return True
            elif '根据校防疫工作要求，请您务必每天上午12点之前完成打卡，并确保“手机定位”功能已经开通，谢谢配合。' in text_list:
                return False
            else:
                print('检测今日是否打卡出现错误，请联系作者: {}'.format(USER))
        except Exception as e:
            print(e)
            print('检查是否已经填报是出错，请联系作者: {}'.format(USER))
        return False

    def auto_clock(self, name, username, password, loc):
        # 1. 进入登陆页面获取cookie
        self.set_cookie()
        # 2. 账户密码登录获取完整cookie
        if self.post_login(username, password):
            # 3. 校验是否已完成今日打卡
            if not self.check_submit():
                print('正在打卡...')
                res = self.submit_info(name, username, loc) and self.check_submit()
                if res:
                    print('打卡失败，请手动填报，并联系作者: {}'.format(USER))


if __name__ == '__main__':
    agent = AutoAgent()
    # agent.auto_clock('邢江波', '202025200749', '262511', '浙江师范大学本部校区')

    for person in users:
        real_name, uname, passwd, location = person
        print(real_name, '正在打卡...')
        agent.auto_clock(real_name, uname, passwd, location)
        print()
