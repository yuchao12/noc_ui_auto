#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on 2021年10月26日
@author: yuchao
'''

class  remote_management (object):
    move_set = '//div[text()="Advanced"]'  # 移动到Advanced settings
    move_remote_management = '//li[contains(text(), " Remote Management ")]'  # 移动到remote_management
    access_button='//span[text()=" Web WAN Access "]/preceding::span[1]/..'  # Web WAN Access 复选框
    port='//label[text()="Port"]/following::input[1]' # 端口输入框
    ip='//label[text()="IP"]/following::input[1]' # IP地址输入框
    save_button='//button[@type="button"]'# 保存按钮
    expect_url='https://noc-test.merckuwifi.com/mesh/{}/setting/remote'
    #预期的网址
    toast = '//p[@class="el-message__content"]'  # 操作提示
