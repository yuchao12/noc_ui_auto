#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on 2021年10月25日
@author: yuchao
'''

class  port_forwarding (object):
    move_set = '//div[text()="Advanced"]' #移动到Advanced settings
    move_Port_Forwarding = '//li[contains(text(), "Port Forwarding ")]'#移动到Port_Forwarding
    add_button = '//span[text()=" Add "]'#添加按钮
    input_name = '//label[text()="Name"]/following::input[1]' #输入用户名
    select = '//input[@placeholder="Select"]'  #选择协议的下拉框
    remote_ip = '//label[text()="Remote IP"]/following::input[1]' #外网ip输入框
    local_ip = '//label[text()="Local IP"]/following::input[1]' #本地ip地址输入框
    save = '//button[@class="el-button el-button--primary"]' #保存按钮
    expect_url = 'https://noc-test.merckuwifi.com/mesh/{}/setting/portforwarding' #预期网址,引用设备的SN号
    protocol = '//span[text()="{}"]'  # 选择协议
    edit_name = "//div[text()=' {} ' ]/preceding::td[2]/div" # 编辑的行的端口转发名
    edit_ip_port = "//div[text()=' {} ' ]/preceding::td[1]/div" # 编辑的行的外网ip和端口号
    edit_protocol = "//div[text()=' {} ' ]/following::td[1]/div" #编辑的行的协议
    edit_local = "//div[text()=' {} ']" # 编辑的本地ip和端口号
    edit_button = "//div[text()=' {}/{}-{} ']/following::button[1]" #编辑按钮
    delete_button = "//div[text()=' {}/{}-{} ']/following::button[2]" # 删除按钮
    delete_affirm = '//div[@class="el-message-box"]/div[3]/button[2]' #确认删除
    toast = '//p[@class="el-message__content"]' # 操作提示
    delete_ip = "//div[text()=' {}/{}-{} ']"  #被删除的本地ip和端口
    remote_port1 = '//label[text()="Local port range"]/following::input[1]'#第一个外网端口
    remote_port2 = '//label[text()="Local port range"]/following::input[2]'#第二个外网端口
    local_port1 = '//label[text()="Remote port range"]/following::input[1]' #第一个本地端口
    local_port2 = '//label[text()="Remote port range"]/following::input[2]' #第二个本地端口