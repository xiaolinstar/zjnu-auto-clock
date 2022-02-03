import datetime
import os

import requests
session = requests.Session()
LOGIN_API = 'http://zyt.zjnu.edu.cn/Login/EIPV4/login.aspx'
INFO_API = 'http://zyt.zjnu.edu.cn/H5/ZJSFDX/FillIn.aspx'
FILL_CHECK_API = 'http://zyt.zjnu.edu.cn/H5/ZJSFDX/CheckFillIn.aspx'

users = eval(os.environ['USERS'])

HEADER = {
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN, zh; q=0.9',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko)',
    'Content-Type': 'application/x-www-form-urlencoded',
}

LOGIN_DATA = {
    '__EVENTTARGET': 'btn_Login',
    '__EVENTARGUMENT': '',
    '__VIEWSTATE': '/wEPDwUKLTkyNjc3Mjk5MA9kFgICAw9kFgQCAQ8WAh4JaW5uZXJodG1sBS3mtZnmsZ/luIjojIPlpKflrabmiJjnlqvpgJrkv6Hmga/nm7TmiqXns7vnu59kAgsPFgIfAAUy6LeD57+UT0Hlip7lhazns7vnu58g54mI5p2D5omA5pyJICYjMTY5OyAyMDA2LTIwMjJkZAgIyDDRQLxoyKDdShXw1zuRxSt+9zHP9pUa5LyPcnAf',
    '__VIEWSTATEGENERATOR': 'B88FCDAB',
    '__EVENTVALIDATION': '/wEdAAdgSVso869Er0OtjX6Ff9fj0elL860XNtv4rogmL6mawP3Vqw5XZsL40jZDizLHlCVw1VqEhL0Qs5iJV9Ksp6V6BSl8Pvpk36YxATXhqVvqZUi2aMKjuup8LZmcudbM9grwpqqjo0L5QYjSKkG6g7gBT3fFWs4JP+sq1oTpmykZOBivAatyb/7PAKkxtdcnNds=',
    'hdnUsbkey': '',
    # 'hdnToken': '9FE867A347AC9D54F3D8D73DD9C34F8E',
    # 'hdnToken': '683CC4D7EA38B61BD2C4D4BCB2FCDFCC',
    'hdnToken': '',
    'hdnLogin_Show_AppQcode': '1'
}

"""
    需要更新的键值对
    personname personcode txtCreateTime
"""
USER_DATA = {
    '__EVENTTARGET': 'btn_save',
    '__EVENTARGUMENT': '',
    '__VIEWSTATE': '/wEPDwUJOTMwMDE3NjU5ZGSrucGNcWZY4gj6odekPQTFlJVeAKR3Yd2XtPjXa0w0WQ==',
    '__VIEWSTATEGENERATOR': '3674067D',
    '__EVENTVALIDATION': '/wEdABl0THonuo/+ink4LkyDZtaKnPdgn5d6iO4LuTjGeN2JM3llOAzR6kycDzMfToHX0QOa6jYEaUq7hqoikcwmGDr/nmnPxOBQ7q1ly++ofgUcfBMeg5WVSSvtrjLjx3x5POv400VKLRNp/k6261iHtmxhYdp8PLLcr00Ykm6GIg/QPm2VAoUsguAjookCWDEX54sHQe9Pfyn7J2iyftT+Cg0mL0jfXWdOZUPTgbQHBDwymb6wlsA0YdypgcCl8awhDxBgYuHAmLDqwPtQh9HDEtJjr+c7NEwFf3c5FPeYdSyrXrYIOfZQS7Mh8jWxQ/3S2fHk/wGpGPyEyYtOtvQbZ7eyCWoEiO6Dd+V6RlHl9UDOJYVHlcFqi++psAvZk9q9RG5W1pRfvYYFhXg72yYOmnpySmm9X2U2t6Y11P+J4lVyalm+n0KUg6wbhm42RvKN577lL2zWcbD6zAaEib0znaI8tWsLH8H+NXQUYD4Kkws4BfoJpIr4b0DV7eZFh6tMLUyznw6pK1ioM6RKyI7TbQybieZNWBTk3CdEPnRsq5aC3CewTWOA8Ln02pcB5hhfE24=',
    'personname': '邢江波',
    'personcode': '202025200749',
    'txtCreateTime': '',
    'DATA_1': '体温正常',
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
    'DATA_16': '17周岁以上',
    'DATA_12': '',
    'DATA_13': '尚未返校',
    'DATA_14': '河南省 焦作市 沁阳市',
    'DATA_15': '我已知晓并如实填报',
    'hidDATA_1': '体温正常',
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
    'hidDATA_13': '尚未返校',
    'hidDATA_14': '河南省 焦作市 沁阳市',
    'hidDATA_15': '我已知晓并如实填报',
    'hidDATA_16': '17周岁以上',
    'hidDATA_17': '无法获取当前地理位置'
}


def get_token():
    try:
        index = session.get(
            url=LOGIN_API,
            headers={**HEADER}
        )
        return index.text[10284: 10316]
    except Exception as e:
        print('获取登陆页面发生错误', e)


def post_login(username, password):
    # hdnToken: 隐藏的一个token，每天会更新
    """data中的三个变量: hdnToken UserText Password"""
    try:
        login_in = session.post(
            url=LOGIN_API,
            data={**LOGIN_DATA, 'UserText': username, 'PasswordText': password},
            headers={
                **HEADER,
                'Content-Length': '684'
            }
        )
        if login_in.status_code != 200:
            print('状态码:', login_in.status_code)
        text_len = len(login_in.text)
        if text_len == 13278:
            print('成功登陆...')
        elif text_len == 11141:
            print('账号/密码错误，请核查...')
            print(LOGIN_API)
            return False
        else:
            print('请求错误，请通知管理员...')
            return False
    except Exception as e:
        print('登陆网页发生错误', e)
    return True


# 提交表单信息
def post_info():
    # 更新填报日期
    USER_DATA['txtCreateTime'] = str(datetime.date.today())
    try:
        info_res = session.post(
            url=INFO_API,
            data=USER_DATA,
            headers={
                **HEADER,
                'Content-Length': '2249',
            }
        )
        if info_res.status_code != 200:
            print('状态码', info_res.status_code)
    except Exception as e:
        print('提交用户信息发生错误', e)


# 判断是否已经提交过
def check_submit():
    try:
        check = session.get(
            url=FILL_CHECK_API,
            headers={**HEADER}
        )
        if check.status_code != 200:
            print('状态码:', check.status_code)
        if len(check.text) == 10749:
            print('你已经完成了今日的填报，请明天继续填报...')
            return True
    except Exception as e:
        print('检查是否已经填报是出错', e)
    return False


def auto_clock(username, password):
    if post_login(username, password):
        if not check_submit():
            post_info()
            if not check_submit():
                print('打卡失败，请手动填报，请通知管理员')


if __name__ == '__main__':
    token = get_token()
    LOGIN_DATA['hdnToken'] = token
    for person in users:
        name, uname, passwd = person
        print(name, '正在打卡...')
        auto_clock(uname, passwd)
        print()

