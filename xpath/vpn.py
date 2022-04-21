#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on 2021年10月26日
@author: yuchao
'''

class vpn (object):
    add_button = '//span[text()=" Add "]' #添加按钮
    move_set = '//div[text()="Advanced"]'  # 移动到Advanced settings
    move_vpn = '//li[contains(text(), " VPN ")]'  # 移动到vpn
    expect_url= 'https://noc-test.merckuwifi.com/mesh/{}/setting/vpn' # vpn网址
    select = '//label[text()="Protocol"]/following::input[1]'  # 选择协议的下拉框
    protocol = '//span[text()="{}"]' # 选择协议
    input_name = '//label[text()="Name"]/following::input[1]' # 名字输入框
    input_username = '//label[text()="Username"]/following::input[1]' # 用户名输入框
    input_password = '//label[text()="Password(optional)"]/following::input[1]' # 密码输入框
    input_server = '//label[text()="server"]/following::input[1]' # 服务器输入框
    mppe = '//span[text()=" {} "] ' # mppe开关
    mppc = '//span[text()=" {} "] ' # mppe开关
    save_button = '//button[@class="el-button el-button--primary"]'  # 保存按钮
    edit = '//div[text()="{}"]//following::button[1]' # 编辑按钮
    delete = '//div[text()="{}"]//following::button[2]' # 删除按钮
    delete_affirm = '//div[@class="el-message-box"]/div[3]/button[2]' #确认删除
    check_mppe = '//span[text()=" MPPE "]/parent::label' # mppe的勾选状态
    check_mppc = '//span[text()=" MPPC "]/parent::label' # mppc的勾选状态
    toast = '//p[@class="el-message__content"]'  # 操作提示
    name = '//div[text()="{}"]' #vpn名称






