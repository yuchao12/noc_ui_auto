#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on 2021年10月26日
@author: yuchao
'''

from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.get_log import get_log
from common.user_public_fun import move_to_message_center
from data.conf import except_sn
from xpath.vpn import vpn


def move_to_vpn_page(driver):
    #移动到vpn页面
    repeat_times = 1
    while repeat_times < 4:
        get_log().info(f'这是第{repeat_times}次进入')
        try:
            if  vpn.expect_url.format(except_sn) in driver.current_url:
                # 判断是否已经在VPN页面
                get_log().info('刷新页面')
                driver.refresh()
            else:
                get_log().info('开始进入到VPN页面')
                driver.find_element(By.XPATH, vpn.move_set).click()
                sleep(2)
                ActionChains(driver).click(driver.find_element_by_xpath(vpn.move_vpn)).perform()
                # 进入到VPN的页面
                sleep(2)
            actul_url = driver.current_url
            # 获取当前页面的url
            if actul_url == vpn.expect_url.format(except_sn):
                get_log().info('进入VPN页面成功')
                sleep(3)
                return True
        except:
            driver.refresh()
            sleep(2)
        finally:
            repeat_times += 1
    get_log().error('进入VPN页面失败')
    assert False

def add_vpn(driver,except_name,except_server,except_username,except_protocol,
            except_password=None,except_mppe=None,except_mppc=None):
    #添加vpn
    move_to_vpn_page(driver)
    repeat_times = 1
    while repeat_times < 4:
        get_log().info(f'这是第{repeat_times}次进入')
        try:
            driver.find_element(By.XPATH, vpn.add_button).click()
            # 添加按钮
            driver.find_element(By.XPATH, vpn.input_name).send_keys(except_name)
            # 输入vpn名称
            driver.find_element(By.XPATH, vpn.input_server).send_keys(except_server)
            # 输入服务器
            driver.find_element(By.XPATH, vpn.input_username).send_keys(except_username)
            # 输入用户名
            driver.find_element(By.XPATH, vpn.input_password).send_keys(except_password)
            # 输入密码
            if except_protocol == 'PPTP':
                WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, vpn.select))
                ).click()
                WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, vpn.protocol.format(except_protocol)))
                ).click()
                # 选择PPTP协议
                if except_mppe is not None:
                    driver.find_element(By.XPATH, vpn.mppe.format(except_mppe)).click()
                    # 勾选 MPPE
                if except_mppc is not None:
                    driver.find_element(By.XPATH, vpn.mppc.format(except_mppc)).click()
                    # 勾选 MPPC
            else:
                driver.find_element(By.XPATH, vpn.select).click()
                WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, vpn.protocol.format(except_protocol)))
                ).click()
                # 选择L2TP协议
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, vpn.save_button))).click()

            driver.find_element(By.XPATH, vpn.save_button).click()
            # 保存配置
            get_log().info('添加VPN成功')
            return
        except:
            driver.refresh()
            sleep(2)
        finally:
            repeat_times += 1
    get_log().error('添加VPN失败')
    assert False

def check_vpn(driver,except_name,expect_operation_type,except_server=None,except_username=None,except_protocol=None,
              except_password=None,except_mppe=None,except_mppc=None):
    """检查配置的vpn的值,根据VPN名称定位"""
    repeat_times = 1
    while repeat_times < 4:
        operation_type, message_status = move_to_message_center(driver)
        if operation_type == expect_operation_type and message_status == 'Succeeded':
            move_to_vpn_page(driver)
            # 判断操作类型是否正确，当操作类型正确且状态为成功时切换到VPN页面检查数据
        else:
            get_log().error('消息中心操作类型或状态错误')
            return False
        try:
            get_log().info(f'这是第{repeat_times}次检查VPN配置')
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, vpn.edit.format(except_name)))).click()
            if except_name is not None:
                actual_name=WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, vpn.input_name))).get_attribute('value')
                get_log().info('预期的名称为 '+except_name)
                get_log().info('实际的名称为 '+actual_name)
                if actual_name != except_name:
                    if repeat_times == 3:
                        get_log().error('预期的名称和实际的名称不一致，配置失败')
                        return False
                    assert False
            if except_server is not None:
                actual_server = WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, vpn.input_server))).get_attribute('value')
                get_log().info('预期的服务器为 '+except_server)
                get_log().info('实际的服务器为 '+actual_server)
                if actual_server != except_server:
                    if repeat_times == 3:
                        get_log().error('预期的服务器和实际的服务器不一致，配置失败')
                        return False
                    assert False
            if except_username is not None:
                actual_username = WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, vpn.input_username))).get_attribute('value')
                get_log().info('预期的用户名为 '+except_username)
                get_log().info('实际的用户名为 '+actual_username)
                if actual_username != except_username:
                    if repeat_times == 3:
                        get_log().error('预期的用户名和实际的用户名不一致，配置失败')
                        return False
                    assert False
            if except_protocol is not None:
                actual_protocol = WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, vpn.select))).get_attribute('value')
                get_log().info('预期的协议为 '+except_protocol)
                get_log().info('实际的协议为 '+actual_protocol)
                if actual_protocol != except_protocol:
                    if repeat_times == 3:
                        get_log().error('预期的协议和实际的协议不一致，配置失败')
                        return False
                    assert False
            if except_password is not None:
                actual_password = WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, vpn.input_password))).get_attribute('value')
                get_log().info('预期的密码为 '+except_password)
                get_log().info('实际的密码为 '+actual_password)
                if actual_password != except_password:
                    if repeat_times == 3:
                        get_log().error('预期的密码和实际的密码不一致，配置失败')
                        return False
                    assert False
            if except_mppe is not None:
                actual_mppe = WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, vpn.check_mppe))).get_attribute('class')
                get_log().info('mppe预期的勾选状态为 '+except_mppe)
                get_log().info('mppe实际的勾选状态为 '+actual_mppe)
                if actual_mppe != except_mppe:
                    if repeat_times == 3:
                        get_log().error('预期的勾选状态和实际的勾选状态不一致，配置失败')
                        return False
                    assert False
            if except_mppc is not None:
                actual_mppc = WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, vpn.check_mppc))).get_attribute('class')
                get_log().info('mppc预期的勾选状态为 '+except_mppc)
                get_log().info('mppc实际的勾选状态为 '+actual_mppc)
                if actual_mppc != except_mppc:
                    if repeat_times == 3:
                        get_log().error('预期的勾选状态和实际的勾选状态不一致，配置失败')
                        return False
                    assert False
            return True
        except:
            driver.refresh()
            sleep(5)
        finally:
            repeat_times += 1
    get_log().error('检查配置失败')
    assert False

def edit_vpn(driver,name,except_name,except_server=None,except_username=None,except_protocol=None,
              except_password=None,except_mppe=None,except_mppc=None):
    # 编辑vpn
    move_to_vpn_page(driver)
    repeat_times = 1
    while repeat_times < 4:
        get_log().info(f'这是第{repeat_times}次进入')
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, vpn.edit.format(name)))).click()
        try:
            if except_name is  not None:
                driver.find_element(By.XPATH, vpn.input_name).clear()
                sleep(1)
                driver.find_element(By.XPATH, vpn.input_name).send_keys(except_name)
                # 输入vpn名称
            if except_server is not None:
                driver.find_element(By.XPATH, vpn.input_server).clear()
                sleep(1)
                driver.find_element(By.XPATH, vpn.input_server).send_keys(except_server)
                # 输入服务器
            if except_username is  not None:
                driver.find_element(By.XPATH, vpn.input_username).clear()
                sleep(1)
                driver.find_element(By.XPATH, vpn.input_username).send_keys(except_username)
                # 输入用户名
            if except_password is not None:
                driver.find_element(By.XPATH, vpn.input_password).clear()
                sleep(1)
                driver.find_element(By.XPATH, vpn.input_password).send_keys(except_password)
                # 输入密码
            if except_protocol is not None:
                if except_protocol == 'PPTP':
                    driver.find_element(By.XPATH, vpn.select).click()
                    WebDriverWait(driver, 10).until(
                        EC.visibility_of_element_located((By.XPATH, vpn.protocol.format(except_protocol)))
                    ).click()
                    # 选择PPTP协议
                    if except_mppe is not None:
                        driver.find_element(By.XPATH, vpn.mppe.format(except_mppe)).click()
                        # 勾选 MPPE
                    if except_mppc is not None:
                        driver.find_element(By.XPATH, vpn.mppc.format(except_mppc)).click()
                        # 勾选 MPPC
                else:
                    driver.find_element(By.XPATH, vpn.select).click()
                    WebDriverWait(driver, 10).until(
                        EC.visibility_of_element_located((By.XPATH, vpn.protocol.format(except_protocol)))
                    ).click()
                    # 选择L2TP协议
            driver.find_element(By.XPATH, vpn.save_button).click()
            # 保存配置
            get_log().info('编辑VPN成功')
            return
        except:
            driver.refresh()
            sleep(2)
        finally:
            repeat_times += 1
    get_log().error('编辑VPN失败')
    assert False

def delet_vpn(driver,except_name):
    #删除刚刚添加的PPTP协议的VPN
    move_to_vpn_page(driver)
    repeat_times = 1
    while repeat_times < 4:
        get_log().info(f'这是第{repeat_times}次删除VPN')
        try:
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, vpn.delete.format(except_name)))
            ).click()
            # 删除刚刚添加的PPTP协议的VPN
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, vpn.delete_affirm))
            ).click()
            #点击确定按钮
            toast=WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, vpn.toast))).text
            get_log().info('toast提示'+toast)
            #删除成功的toast提示
            get_log().info('删除成功')
            return True
        except:
            driver.refresh()
            sleep(5)
        finally:
            repeat_times += 1
    get_log().error('删除失败')
    assert False

def check_delet_vpn(driver,except_name,expect_operation_type):
    """检查是否删除成功"""
    repeat_times = 1
    while repeat_times < 4:
        operation_type, message_status = move_to_message_center(driver)
        if operation_type == expect_operation_type and message_status == 'Succeeded':
            move_to_vpn_page(driver)
            # 判断操作类型是否正确，当操作类型正确且状态为成功时切换到VPN页面检查数据
        else:
            get_log().error('消息中心操作类型或状态错误')
            return False
        try:
            get_log().info(f'这是第{repeat_times}次检查删除是否成功')
            if driver.find_element_by_xpath(vpn.name).fomart(except_name):
                get_log().error('删除失败')
                return False
        except:
            driver.refresh()
            sleep(5)
        finally:
            repeat_times += 1
    get_log().info('删除成功')
    return True


























