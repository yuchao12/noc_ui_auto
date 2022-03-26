#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on 2021年10月26日
@author: yuchao
'''

import allure
import pytest
from function import vpn_fun
from common.get_log import get_log
from data.conf import L2TP_vpn, PPTP_vpn, edit_vpn, delet_vpn

@allure.feature('VPN模块')
@pytest.mark.vpn
class Test_vpn():
    @allure.title('【正确性检测】新增L2TP VPN成功后，所有的信息配置项正确【NOC-8680】')
    def test_1_add_L2TP_vpn(self,driver):
        """【正确性检测】新增L2TP VPN成功后，所有的信息配置项正确【NOC-8680】"""
        vpn_fun.add_vpn(driver,except_name = L2TP_vpn["name"],#vpn名称
                        except_server = L2TP_vpn["server"],# vpn 服务器
                        except_username=L2TP_vpn["username"],# vpn 用户名
                        except_protocol=L2TP_vpn["protocol"],# vpn 协议
                        except_password=L2TP_vpn["password"])# vpn 密码
        result=vpn_fun.check_vpn(driver,except_name = L2TP_vpn["name"],#vpn名称
                        expect_operation_type=L2TP_vpn["type"], # 操作类型
                        except_server = L2TP_vpn["server"],# vpn 服务器
                        except_username=L2TP_vpn["username"],# vpn 用户名
                        except_protocol=L2TP_vpn["protocol"],# vpn 协议
                        except_password=L2TP_vpn["password"])# vpn 密码
        if result:
            get_log().info('添加L2TP协议的VPN成功')
            assert True
        else:
            get_log().error('添加L2TP协议的VPN失败')
            assert False

    @allure.title('【正确性检测】新增PPTP VPN成功后，所有的信息配置项正确【NOC-9252】')
    def test_2_add_PPTP_vpn(self,driver):
        """【正确性检测】新增PPTP VPN成功后，所有的信息配置项正确【NOC-9252】"""
        vpn_fun.add_vpn(driver,except_name = PPTP_vpn["name"],#vpn名称
                        except_server = PPTP_vpn["server"],# vpn 服务器
                        except_username=PPTP_vpn["username"],# vpn 用户名
                        except_protocol=PPTP_vpn["protocol"],# vpn 协议
                        except_password=PPTP_vpn["password"],# vpn 密码
                        except_mppe=PPTP_vpn["mppe"], # vpn 勾选mppe
                        except_mppc=PPTP_vpn["mppc"]) # vpn 勾选mppc
        result=vpn_fun.check_vpn(driver,except_name = PPTP_vpn["name"],#vpn名称
                        expect_operation_type=PPTP_vpn["type"], # 操作类型
                        except_server = PPTP_vpn["server"],# vpn 服务器
                        except_username=PPTP_vpn["username"],# vpn 用户名
                        except_protocol=PPTP_vpn["protocol"],# vpn 协议
                        except_password=PPTP_vpn["password"],# vpn 密码
                        except_mppc=PPTP_vpn["checkbox_status"], # mppc复选框状态
                        except_mppe=PPTP_vpn["checkbox_status"]) # mppe复选框状态
        if result:
            get_log().info('添加PPTP协议的VPN成功')
            assert True
        else:
            get_log().error('添加PPTP协议的VPN失败')
            assert False

    @allure.title('【正确性检测】修改所有的信息能修改成功，并且配置项正确【NOC-9251】（修改刚刚添加的L2TP协议）')
    def test_3_modify_L2TP_vpn(self,driver):
        """【正确性检测】修改所有的信息能修改成功，并且配置项正确【NOC-9251】（修改刚刚添加的L2TP协议）"""
        vpn_fun.edit_vpn(driver,name=L2TP_vpn["name"],# 要修改的L2TP协议的名称
                        except_name = edit_vpn["name"],#vpn名称
                        except_server = edit_vpn["server"],# vpn 服务器
                        except_username=edit_vpn["username"],# vpn 用户名
                        except_protocol=edit_vpn["protocol"],# vpn 协议
                        except_password=edit_vpn["password"])# vpn 密码
        result=vpn_fun.check_vpn(driver,except_name = edit_vpn["name"],#vpn名称
                        expect_operation_type=edit_vpn["type"], # 操作类型
                        except_server = edit_vpn["server"],# vpn 服务器
                        except_username = edit_vpn["username"],# vpn 用户名
                        except_protocol=edit_vpn["protocol"],# vpn 协议
                        except_password=edit_vpn["password"])# vpn 密码
        if result :
            get_log().info("修改的预期值与实际的值一致，修改成功")
            assert True
        else:
            get_log().error("修改的预期值与实际的值不一致，修改失败")
            assert False

    @allure.title('【正确性检测】能正常删除VPN【NOC-8630】')
    def test_4_delete_PPTP_vpn(self,driver):
        """【正确性检测】能正常删除VPN【NOC-8630】"""
        vpn_fun.delet_vpn(driver,except_name=delet_vpn["name"]) # 要删除的vpn的名称
        result=vpn_fun.check_delet_vpn(driver,except_name=delet_vpn["name"] # 删除的vpn的名称
                                ,expect_operation_type=delet_vpn["type"]) # 操作类型
        if result:
            get_log().info('删除PPTP协议的VPN成功')
            assert True
        else:
            get_log().error('删除PPTP协议的VPN失败')
            assert False




