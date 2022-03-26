#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on 2021年10月25日
@author: yuchao
'''

import allure
import pytest
from function import port_forwarding_fun
from common.get_log import get_log
from data.conf import TCP_UDP_Port_forwarding, TCP_Port_forwarding, UDP_Port_forwarding, edit_Port_forwarding, \
    delete_Port_forwarding

@allure.feature('端口转发模块')
@pytest.mark.port_forwarding
class Test_port_forwarding():
    @allure.title('新增一条协议为”TCP&UDP“的端口转发[NOC-8365]')
    def test_1_add_tcp_udp_port_forwarding(self,driver):
        """新增一条协议为”TCP&UDP“的端口转发[NOC-8365]"""
        port_forwarding_fun.add_port_forwarding(driver,expect_portname=TCP_UDP_Port_forwarding["name"],#端口名
                                                expect_remote_ip=TCP_UDP_Port_forwarding["remote_ip"], # 外网ip
                                                expect_portnum1=TCP_UDP_Port_forwarding["port_num1"],# 第一个外网端口号
                                                expect_portnum2=TCP_UDP_Port_forwarding["port_num2"],# 第二个外网端口号
                                                expect_portnum3=TCP_UDP_Port_forwarding["port_num3"],# 第一个本地端口号
                                                expect_portnum4=TCP_UDP_Port_forwarding["port_num4"],# 第二个本地端口号
                                                expect_ip=TCP_UDP_Port_forwarding["local_ip"],# 本地ip地址
                                                expect_Protocol=TCP_UDP_Port_forwarding["Protocol_TCP/UDP"]) # TCP/UDP协议
        result=port_forwarding_fun.check_port_forwarding(driver,expect_ip=TCP_UDP_Port_forwarding["local_ip"],
                                                         expect_portname=TCP_UDP_Port_forwarding["name"],#本地ip地址
                                                         expect_remote_ip=TCP_UDP_Port_forwarding["remote_ip"],# 外网ip
                                                         expect_portnum1=TCP_UDP_Port_forwarding["port_num1"],# 第一个外网端口号
                                                         expect_portnum2=TCP_UDP_Port_forwarding["port_num2"],# 第二个外网端口号
                                                         expect_portnum3=TCP_UDP_Port_forwarding["port_num3"],# 第一个本地端口号
                                                         expect_portnum4=TCP_UDP_Port_forwarding["port_num4"],# 第二个本地端口号
                                                         expect_operation_type=TCP_UDP_Port_forwarding["type"],# 预期的操作类型
                                                         expect_Protocol=TCP_UDP_Port_forwarding["Protocol_TCP/UDP"]) # TCP/UDP协议
        if result:
            get_log().info('添加TCP&UDP协议的端口转发成功')
            assert True
        else:
            get_log().error('添加TCP&UDP协议的端口转发失败')
            assert False

    @allure.title('新增一条协议为”TCP“的端口转发[NOC-8366]')
    def test_2_add_tcp_port_forwarding(self,driver):
        """新增一条协议为”TCP“的端口转发[NOC-8366]"""
        port_forwarding_fun.add_port_forwarding(driver,expect_portname=TCP_Port_forwarding["name"],#端口名
                                                expect_remote_ip=TCP_Port_forwarding["remote_ip"], # 外网ip
                                                expect_portnum1=TCP_Port_forwarding["port_num1"],# 第一个外网端口号
                                                expect_portnum2=TCP_Port_forwarding["port_num2"],# 第二个外网端口号
                                                expect_portnum3=TCP_Port_forwarding["port_num3"],# 第一个本地端口号
                                                expect_portnum4=TCP_Port_forwarding["port_num4"],# 第二个本地端口号
                                                expect_ip=TCP_Port_forwarding["local_ip"],# 本地ip地址
                                                expect_Protocol=TCP_Port_forwarding["Protocol_TCP"]) # TCP协议
        result=port_forwarding_fun.check_port_forwarding(driver,expect_ip=TCP_Port_forwarding["local_ip"],
                                                         expect_portname=TCP_Port_forwarding["name"],#本地ip地址
                                                         expect_remote_ip=TCP_Port_forwarding["remote_ip"],# 外网ip
                                                         expect_portnum1=TCP_Port_forwarding["port_num1"], # 第一个外网端口号
                                                         expect_portnum2=TCP_Port_forwarding["port_num2"], # 第二个外网端口号
                                                         expect_portnum3=TCP_Port_forwarding["port_num3"], # 第一个本地端口号
                                                         expect_portnum4=TCP_Port_forwarding["port_num4"],# 第二个本地端口号
                                                         expect_operation_type=TCP_Port_forwarding["type"],# 预期的操作类型
                                                         expect_Protocol=TCP_Port_forwarding["Protocol_TCP"]) # TCP协议
        if result:
            get_log().info('添加TCP协议的端口转发成功')
            assert True
        else:
            get_log().error('添加TCP协议的端口转发失败')
            assert False

    @allure.title('新增一条协议为”UDP“的端口转发[NOC-8367]')
    def test_3_add_udp_port_forwarding(self,driver):
        """新增一条协议为”UDP“的端口转发[NOC-8367]"""
        port_forwarding_fun.add_port_forwarding(driver, expect_portname=UDP_Port_forwarding["name"],  # 端口名
                                                expect_remote_ip=UDP_Port_forwarding["remote_ip"],  # 外网ip
                                                expect_portnum1=UDP_Port_forwarding["port_num1"],  # 第一个外网端口号
                                                expect_portnum2=UDP_Port_forwarding["port_num2"],  # 第二个外网端口号
                                                expect_portnum3=UDP_Port_forwarding["port_num3"],  # 第一个本地端口号
                                                expect_portnum4=UDP_Port_forwarding["port_num4"],  # 第二个本地端口号
                                                expect_ip=UDP_Port_forwarding["local_ip"],  # 本地ip地址
                                                expect_Protocol=UDP_Port_forwarding["Protocol_UDP"])  # UDP协议
        result = port_forwarding_fun.check_port_forwarding(driver, expect_ip=UDP_Port_forwarding["local_ip"],
                                                           expect_portname=UDP_Port_forwarding["name"],  # 本地ip地址
                                                           expect_remote_ip=UDP_Port_forwarding["remote_ip"],  # 外网ip
                                                           expect_portnum1=UDP_Port_forwarding["port_num1"],  # 第一个外网端口号
                                                           expect_portnum2=UDP_Port_forwarding["port_num2"],  # 第二个外网端口号
                                                           expect_portnum3=UDP_Port_forwarding["port_num3"],  # 第一个本地端口号
                                                           expect_portnum4=UDP_Port_forwarding["port_num4"],  # 第二个本地端口号
                                                           expect_operation_type=UDP_Port_forwarding["type"],  # 预期的操作类型
                                                           expect_Protocol=UDP_Port_forwarding["Protocol_UDP"])  # UDP协议
        if result:
            get_log().info('添加UDP协议的端口转发成功')
            assert True
        else:
            get_log().error('添加UDP协议的端口转发失败')
            assert False

    @allure.title('修改所有的信息能修改成功[NOC-8329]')
    def test_4_edit_port_forwarding(self,driver):
        """修改所有的信息能修改成功[NOC-8329]"""
        port_forwarding_fun.edit_port_forwarding(driver,upd_ip=UDP_Port_forwarding['local_ip'], # UPD协议的本地ip
                                                 udp_port3=UDP_Port_forwarding["port_num3"], # UPD协议的第一个本地端口
                                                 udp_port4=UDP_Port_forwarding["port_num4"], # UPD协议的第二个本地端口
                                                 expect_portname=edit_Port_forwarding["name"],# 端口名
                                                 expect_remote_ip=edit_Port_forwarding['remote_ip'], # 外网ip
                                                 expect_portnum1=edit_Port_forwarding["port_num1"],# 第一个外网端口号
                                                 expect_portnum2=edit_Port_forwarding["port_num2"],# 第二个外网端口号
                                                 expect_portnum3=edit_Port_forwarding["port_num3"],# 第一个本地端口号
                                                 expect_portnum4=edit_Port_forwarding["port_num4"],# 第二个本地端口号
                                                 expect_ip=edit_Port_forwarding["local_ip"],# 本地ip地址
                                                 expect_Protocol=edit_Port_forwarding["Protocol_TCP/UDP"])  # TCP/UDP协议
        result=port_forwarding_fun.check_port_forwarding(driver,expect_ip=edit_Port_forwarding["local_ip"],
                                                         expect_portname=edit_Port_forwarding["name"],#本地ip地址
                                                         expect_remote_ip=edit_Port_forwarding["remote_ip"],# 外网ip
                                                         expect_portnum1=edit_Port_forwarding["port_num1"], # 第一个外网端口号
                                                         expect_portnum2=edit_Port_forwarding["port_num2"], # 第二个外网端口号
                                                         expect_portnum3=edit_Port_forwarding["port_num3"], # 第一个本地端口号
                                                         expect_portnum4=edit_Port_forwarding["port_num4"],# 第二个本地端口号
                                                         expect_operation_type=edit_Port_forwarding["type"],# 预期的操作类型
                                                         expect_Protocol=edit_Port_forwarding["Protocol_TCP/UDP"]) # TCP/UDP协议
        if result:
            get_log().info('修改UDP协议的端口转发成功')
            assert True
        else:
            get_log().error('修改UDP协议的端口转发失败')
            assert False

    @allure.title('端口转发：列表删除按钮，点击有toast提示[NOC-8386]')
    def test_5_delete_port_forwarding(self,driver):
        """端口转发：列表删除按钮，点击有toast提示[NOC-8386]"""
        port_forwarding_fun.delete_port_forwarding(driver,expect_ip=delete_Port_forwarding["local_ip"] # TCP协议的本地ip
                                                   ,expect_portnum3=delete_Port_forwarding["port_num3"],# 第一个本地端口号
                                                   expect_portnum4=delete_Port_forwarding["port_num4"])# 第二个本地端口号
        #因为删除的是刚刚创建的TCP协议，所以这里的第一个端口号和第二个本地端口号与TCP协议中的两个端口一致
        result=port_forwarding_fun.check_delet_port_forwarding(driver,expect_ip=delete_Port_forwarding["local_ip"],# TCP协议的本地ip
                                                               expect_portnum3=delete_Port_forwarding["port_num3"],# 第一个本地端口号
                                                               expect_portnum4=delete_Port_forwarding["port_num4"],# 第二个本地端口号
                                                               expect_operation_type=delete_Port_forwarding["type"])# 操作类型
        if result:
            get_log().info('删除TCP协议的端口转发成功')
            assert True
        else:
            get_log().error('删除TCP协议的端口转发失败')
            assert False