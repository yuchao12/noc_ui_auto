#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on 2021年10月24日
@author: yuchao
'''

class UserPublicLocators():
    sn_input = '//input[@placeholder="Gateway SN"]'
    search_button = '//button[@class="el-button el-button--primary el-button--medium"]'
    devices_status = '//div[@class="status"]/i'
    enter_devices = '//button[@class="el-button is-linkable el-button--text"]'
    # 消息中心菜单
    message_center_menu = '//div/span[text()="Message center"]'
    # 进度条加载
    loading = "//div[@id='nprogress']"
    # 消息中心第一行的操作类型
    operation_type = '//tbody/tr[1]/td[@class="el-table_1_column_1  "]/div/span'
    # 消息中心第一行的状态
    message_status = '//tbody/tr[1]/td[@class="el-table_1_column_3  "]/div/span'
    # 消息中心第一行的结果
    message_result = '//tbody/tr[1]/td[@class="el-table_1_column_4 is-right "]/div/button'

