#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Haoran Chen"
# Date: 2020/6/22

from selenium import webdriver
import sqlite3
# import cx_Oracle as cx
from selenium.webdriver.support import expected_conditions as EC  # 导入显性等待的包
from selenium.webdriver.support.wait import WebDriverWait  # 判断所需要的元素是否已经被加载出来
from selenium.webdriver.common.by import By  # 定位
import random
# smtplib 用于邮件的发信动作
import smtplib
from email.mime.text import MIMEText
# email 用于构建邮件内容
from email.header import Header
import time


def f_dbconnect():
    '''访问数据库提取用户信息'''
    con = sqlite3.connect("testsqlite.db")  # 创建连接
    cursor = con.cursor()  # 创建游标
    # cursor.execute("select * from automatic_logon_user t where t.user_id = 171330")
    cursor.execute(
        "select user_id,user_pwd,user_name,user_mail from automatic_logon_user where user_id not in (171330)")  # 执行sql语句
    data = list(cursor.fetchall())  # 获取所有数据
    cursor.close()  # 关闭游标
    con.close()  # 关闭数据库连接
    return data


def f_sendemile(emile):
    # 用于构建邮件头

    # 发信方的信息：发信邮箱，QQ 邮箱授权码
    from_addr = '850318517@qq.com'
    password = 'flrxmranmfakbddj'  # 'qnqhakospqfwbfjb'

    # 收信方邮箱
    to_addr = emile

    # 发信服务器
    smtp_server = 'smtp.qq.com'

    # 邮箱正文内容，第一个参数为内容，第二个参数为格式(plain 为纯文本)，第三个参数为编码
    msg = MIMEText('日志填写成功', 'plain', 'utf-8')

    # 邮件头信息
    msg['From'] = Header(from_addr)
    msg['To'] = Header(to_addr)
    msg['Subject'] = Header('自动填写日志')

    # 开启发信服务，这里使用的是加密传输
    server = smtplib.SMTP_SSL(smtp_server)
    server.connect(smtp_server, 465)
    # 登录发信邮箱
    server.login(from_addr, password)
    # 发送邮件
    server.sendmail(from_addr, to_addr, msg.as_string())
    # 关闭服务器
    server.quit()

    print('邮件发送成功')


def week_report(driver):
    i = 0
    try:
        while driver.find_element_by_xpath('//*[@id="Repeater1_ctl02_a_Title"]'):
            title = driver.find_element_by_xpath('//*[@id="Repeater1_ctl02_a_Title"]')
            # Repeater1_ctl01_a_Title
            text = title.get_attribute('textContent')
            print(text)

            if '周报' in text:
                print('执行周报')
                driver.find_element_by_xpath('//*[@id="Repeater1_ctl02_a_Title"]').click()
                # //*[@id="Repeater1_ctl02_a_Title"]
                # //*[@id="Repeater1_ctl01_a_Title"]
                # //*[@id="Repeater1_ctl00_a_Title"]
                i = i + 1
                print('有周报需要审批')
                wait = WebDriverWait(driver, 30)
                wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="gv_dataInfo"]/tbody/tr[1]/th[1]')))
                # 在30s内，每隔0.5s检查一次所需要的元素是否被加载出来，加载出来了就执行下一步，没有加载出来就继续等待，
                driver.find_element_by_xpath('//*[@id="gv_dataInfo"]/tbody/tr[1]/th[1]')

                print('找到需要审批的周报')
                wait = WebDriverWait(driver, 30)
                wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="gv_dataInfo"]/tbody/tr[2]/td[1]/a')))
                title = driver.find_element_by_xpath('//*[@id="gv_dataInfo"]/tbody/tr[2]/td[1]/a')
                # //*[@id="gv_dataInfo"]/tbody/tr[2]/td[1]/a
                text = title.get_attribute('textContent').strip()
                print(text)

                driver.find_element_by_id('gv_dataInfo').find_element_by_link_text(text).click()
                driver.find_element_by_id('rdlListIsSatisfied_1').click()
                driver.find_element_by_id('txtScoreDesc').click()
                driver.find_element_by_id('txtScoreDesc').send_keys('满意')

                driver.find_element_by_id('txtSubtractionDesc').click()
                driver.find_element_by_id('txtSubtractionDesc').send_keys('满意')

                driver.find_element_by_id('txtSuggestion').click()
                driver.find_element_by_id('txtSuggestion').send_keys('满意')

                driver.find_element_by_id('lblReview').click()
                wait = WebDriverWait(driver, 20)
                wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="jbox-state-state0"]/div[2]/button')))
                driver.find_element_by_xpath('//*[@id="jbox-state-state0"]/div[2]/button').click()
                print('找到确认')
                print('第{}次执行完毕'.format(i))
                driver.switch_to.default_content()
                driver.find_element_by_xpath('/html/body/div[1]/a').click()
                print('返回')
                driver.switch_to.frame('mainPage')  # 跳转到对应的frame
                # break
            else:
                print('周报已审批完毕')
                print(text)
                break

    except Exception as e:
        print('str(Exception):\t', str(Exception))
        print('str(e):\t\t', str(e))
        print('没有周报需要审批')
    finally:
        driver.switch_to.default_content()
        # driver.find_element_by_xpath('/html/body/div[1]/div/a[2]/img').click()


def f_logon(*list):
    '''登录eds系统'''
    print(list)
    # options = webdriver.ChromeOptions()
    # options.binary_location = "C:\Program Files\Google\Chrome\Application\chrome.exe"
    # browser = webdriver_type(chrome_options=options)
    url = 'http://eds.newtouch.cn/eds3/login.html'
    # driver = webdriver.Chrome('C:\Program Files\Google\Chrome\Application\chromedriver.exe')#虚拟一个Chrome浏览器
    driver = webdriver.Chrome('D:\ChromeDriver\chromedriver.exe')
    driver.maximize_window()  # 窗口最大化
    driver.get(url)  # 访问网站
    driver.implicitly_wait(30)

    for data1 in list:
        print(data1)
        for data in data1:
            print(data)
            driver.find_element_by_id('UserId').click()  # 点击用户名输入框
            print('登录公司网址成功')
            driver.find_element_by_id('UserId').clear()  # 清空输入框
            driver.find_element_by_id('UserId').send_keys(str(data[0]))  # 自动敲入用户名

            driver.find_element_by_id('UserPassword').click()  # 点击密码输入框
            driver.find_element_by_id('UserPassword').clear()  # 清空输入框
            print(data[1])
            driver.find_element_by_id('UserPassword').send_keys(str(data[1]))  # 自动敲入密码

            driver.find_element_by_id('btnSubmit').click()  # 点击登录按钮

            driver.switch_to.frame('mainPage')  # 跳转到对应的frame
            print('用户登录成功')
            time.sleep(1)
            print(type(data[0]))
            if str(data[0]) == '171330':
                driver.find_element_by_xpath('//*[@id="form1"]/div[3]/div[3]/ul/li[4]/a').click()
                date_div = '//*[@id="calendar"]/tbody/tr[1]/th/p[1]/img'
            else:
                driver.find_element_by_xpath('//*[@id="Form1"]/div[3]/div[2]/ul/li[4]/a').click()
                date_div = '//*[@id="calendar"]/tbody/tr[1]/th/p[1]/img'
            # // *[ @ id = "Form1"] / div[3] / div[2] / ul / li[4] / a
            # //*[@id="form1"]/div[3]/div[3]/ul/li[4]/a
            # //*[@id="Form1"]/div[3]/div[2]/ul/li[4]/a

            list = ['需求分析', '测试环境开发', '类生产开发', '同其他系统联调', '上线发布', '用户需求数据提取']
            for i in range(2):
                time.sleep(3)
                print(i)
                # if i == 0 :
                # driver.find_element_by_xpath('//*[@id="calendar"]/tbody/tr[1]/th/p[1]/img').click()
                #     driver.find_element_by_xpath(date_div).click()
                # // *[ @ id = "calendar"] / tbody / tr[1] / th / p[1] / img
                driver.find_element_by_xpath('//*[@id="29"]').click()
                # '//*[@id="calendar"]/tbody/tr[8]/td[2]/div'
                # //*[@id="23"]
                # driver.find_element_by_id('2').click()
                print('跳转至对应日期')
                time.sleep(1)
                driver.find_element_by_xpath('//*[@id="txtMemo"]').click()
                send_key = list[random.randint(0, len(list) - 1)]
                print(send_key)
                driver.find_element_by_xpath('//*[@id="txtMemo"]').send_keys(send_key)  # 自动敲入文本
                driver.find_element_by_xpath('//*[@id="btnSave"]').click()  # 提交
                try:
                    if EC.alert_is_present:
                        print("Alert exists")
                        wait = WebDriverWait(driver, 10)
                        wait.until(EC.alert_is_present())
                        alert = driver.switch_to.alert
                        print(alert.text)
                        alert.accept()
                        print("Alert accepted")
                    else:

                        print("NO alert exists")
                except:
                    pass
                print('{}的第{}次工作日志提交成功'.format(data[2], i + 1))
                time.sleep(1)

            if data[0] == 171330:
                driver.switch_to.default_content()
                driver.find_element_by_xpath('/html/body/div[1]/a/span[1]/img').click()
                print('跳转成功')
                driver.switch_to.frame('mainPage')  # 跳转到对应的frame
                time.sleep(2)
                week_report(driver)

            driver.switch_to.default_content()
            if str(data[0]) == '171330':
                driver.find_element_by_xpath('/html/body/div[1]/div/a[2]/img').click()
            else:
                driver.find_element_by_xpath('/html/body/div[1]/div/a/img').click()

            print('用户已退出')
            # driver.quit()#关闭浏览器
            print(data[3])
            f_sendemile(str(data[3]))


f_logon(f_dbconnect())
