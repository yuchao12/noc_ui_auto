#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on 2021年10月22日
@author: yuchao
'''

import os
import time
from datetime import datetime
import pytest
from selenium import webdriver
from common.get_log import get_log
from common.login_fun import login_successfully
from common.user_public_fun import search_sn_and_click
from data import conf
from data.conf import root_password,root_username

# 自行选择是否每次运行前都清空日志，注释表示一直记录
@pytest.fixture(scope='session',autouse=True)
def delet_log():
    try:
        os.remove('./Logger/logs/'+datetime.now().strftime('%Y-%m-%d')+ '-all'+ '.log')
        os.remove('./Logger/logs/'+datetime.now().strftime('%Y-%m-%d')+ '-error'+ '.log')
        print("清空日志文件")
    except(FileNotFoundError):
        print("没有日志文件，直接写入")

@pytest.fixture(scope='session',autouse=True)
def driver():
    get_log().info('开始执行用例')
    driver = webdriver.Chrome(executable_path=r'C:\driver\chromedriver.exe')
    driver.get(conf.url)
    driver.maximize_window()
    driver.implicitly_wait(10)
    # 用户登录
    login_successfully(driver,root_username,root_password)
    time.sleep(3)
    # 进入设备列表
    js = 'document.getElementsByClassName("el-menu-item")[2].click()'
    driver.execute_script(js)
    time.sleep(1)
    driver.get_screenshot_as_file(r'C:\Project\noc_ui_auto\screenshot\{}.png'.format(datetime.now().strftime('%Y-%m-%d')))
    get_log().info('截图成功')
    time.sleep(3)
    # 选择指定设备
    search_sn_and_click(driver, conf.except_sn, "online", 3)
    yield driver
    get_log().info('用例执行结束')
    driver.quit()
