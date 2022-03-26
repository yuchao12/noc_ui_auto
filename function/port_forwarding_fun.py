#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on 2021年10月25日
@author: yuchao
'''

from telnetlib import EC
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from common.get_log import get_log
from common.user_public_fun import move_to_message_center
from data.conf import except_sn
from xpath.port_forwarding import port_forwarding

def move_to_port_forwarding_page(driver):
    """移动到端口转发的页面"""
    repeat_times = 1
    while repeat_times < 4:
        get_log().info(f'这是第{repeat_times}次进入')
        try:
            if port_forwarding.expect_url.format(except_sn) in driver.current_url:
                # 判断是否已经在端口转发的页面
                get_log().info('已经在端口转发页面，刷新页面')
                driver.refresh()
            else:
                get_log().info('开始进入到端口转发页面')
                driver.find_element(By.XPATH, port_forwarding.move_set).click()
                sleep(2)
                ActionChains(driver).click(driver.find_element_by_xpath(port_forwarding.move_Port_Forwarding)).perform()
                # 进入到端口转发的页面
                sleep(2)
            actul_url=driver.current_url
            #获取当前页面的url
            if actul_url==port_forwarding.expect_url.format(except_sn):
                get_log().info('进入端口转发页面成功')
                sleep(3)
                return True
        except:
            driver.refresh()
            sleep(2)
        finally:
            repeat_times += 1
    get_log().error('进入端口转发页面失败')
    assert False

def add_port_forwarding(driver,expect_portname,expect_Protocol,expect_portnum1,expect_portnum2,
                        expect_portnum3,expect_portnum4,expect_ip,expect_remote_ip=None):
    """添加端口转发"""
    move_to_port_forwarding_page(driver)
    repeat_times = 1
    while repeat_times < 4:
        get_log().info(f'这是第{repeat_times}次添加端口转发')
        try:
            ActionChains(driver).click(driver.find_element_by_xpath(port_forwarding.add_button)).perform()
            # 点击添加按钮
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, port_forwarding.input_name))
            ).send_keys(expect_portname)
            # 输入端口名
            driver.find_element(By.XPATH, port_forwarding.select).click()
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH,port_forwarding.protocol.format(expect_Protocol)))
            ).click()
            # 选择协议
            if expect_remote_ip is not None:
                driver.find_element_by_xpath(port_forwarding.remote_ip).send_keys(expect_remote_ip)
                # 输入外网ip
            driver.find_element(By.XPATH, port_forwarding.remote_port1).send_keys(expect_portnum1)
            driver.find_element(By.XPATH, port_forwarding.remote_port2).send_keys(expect_portnum2)
            # 输入外网端口号
            driver.find_element(By.XPATH, port_forwarding.local_ip).send_keys(expect_ip)
            # 输入本地ip
            driver.find_element(By.XPATH, port_forwarding.local_port1).send_keys(expect_portnum3)
            driver.find_element(By.XPATH, port_forwarding.local_port2).send_keys(expect_portnum4)
            # 输入本地端口号
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, port_forwarding.save))
            ).click()
            # 保存
            get_log().info('添加端口成功')
            return
        except:
            driver.refresh()
            sleep(10)
        finally:
            repeat_times += 1
    get_log().error('添加端口失败')
    assert False

def check_port_forwarding(driver,expect_operation_type,expect_ip,expect_portnum3,expect_portnum4,expect_portname=None,
                          expect_remote_ip=None,expect_portnum1=None,expect_portnum2=None,expect_Protocol=None):
    """检查配置是否与预期配置相同"""
    #根据本地ip和本地的两个端口号来定位所在行，所以此3项为必填项
    expect_local_ip = f"{expect_ip}/{expect_portnum3}-{expect_portnum4}"
    #预期的本地ip和端口号
    repeat_times = 1
    while repeat_times < 4:
        operation_type, message_status = move_to_message_center(driver)
        if operation_type == expect_operation_type and message_status == 'Succeeded':
            move_to_port_forwarding_page(driver)
            # 判断操作类型是否正确，当操作类型正确且状态为成功时切换到端口转发页面检查数据
        else:
            get_log().error('消息中心操作类型或状态错误')
            return False
        try:
            get_log().info(f'这是第{repeat_times}次检查端口转发配置')
            if expect_portname is not None:
                actul_name=WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located(
                        (By.XPATH, port_forwarding.edit_name.format(expect_local_ip)))).text
                get_log().info('实际的端口名 '+actul_name)
                get_log().info('预期的端口名 '+expect_portname)
                if actul_name != expect_portname:
                    if repeat_times == 3:
                        get_log().error('端口名不同，配置失败')
                        return False
                    assert False
            if expect_remote_ip is not None:
                remote_ip_port = WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located(
                        (By.XPATH, port_forwarding.edit_ip_port.format(expect_local_ip)))).text
                actul_remote_ip=remote_ip_port.split('/')[0]
                get_log().info('实际的外网ip '+actul_remote_ip)
                get_log().info('预期的外网ip '+expect_remote_ip)
                if actul_remote_ip != expect_remote_ip:
                    if repeat_times == 3:
                        get_log().error('实际的外网ip预期的不同，配置失败')
                        return False
                    assert False
            if expect_portnum1 is not None:
                remote_ip_port = WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located(
                        (By.XPATH, port_forwarding.edit_ip_port.format(expect_local_ip)))).text
                actul_remote_port=remote_ip_port.split('/')[1].split('-')[0]
                get_log().info('实际的第一个外网端口 '+actul_remote_port)
                get_log().info('预期的第一个外网端口 '+expect_portnum1)
                if actul_remote_port != expect_portnum1:
                    if repeat_times == 3:
                        get_log().error('实际的第一个外网端口预期的不同，配置失败')
                        return False
                    assert False
            if expect_portnum2 is not None:
                remote_ip_port = WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located(
                        (By.XPATH, port_forwarding.edit_ip_port.format(expect_local_ip)))).text
                actul_remote_port2=remote_ip_port.split('/')[1].split('-')[1]
                get_log().info('实际的第二个外网端口 '+actul_remote_port2)
                get_log().info('预期的第二个外网端口 '+expect_portnum2)
                if actul_remote_port2 != expect_portnum2:
                    if repeat_times == 3:
                        get_log().error('实际的第二个外网端口预期的不同，配置失败')
                        return False
                    assert False
            if expect_Protocol is not None:
                actul_Protocol =WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located(
                        (By.XPATH, port_forwarding.edit_protocol.format(expect_local_ip)))).text
                if expect_Protocol == 'TCP/UDP':
                    expect_Protocol = 'TCP&UDP'
                expect_protocol = expect_Protocol
                get_log().info('实际的协议 '+actul_Protocol)
                get_log().info('预期的协议 '+expect_protocol)
                if actul_Protocol != expect_Protocol:
                    if repeat_times == 3:
                        get_log().error('实际的协议与预期的协议不同，配置失败')
                        return False
                    assert False
            actul_local_ip=WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located(
                    (By.XPATH, port_forwarding.edit_local.format(expect_local_ip)))).text
            get_log().info('实际的本地ip和端口号 '+actul_local_ip)
            get_log().info('预期的本地ip和端口号 '+expect_local_ip)
            if actul_local_ip != expect_local_ip:
                if repeat_times == 3:
                    get_log().error('实际的本地ip和端口与预期的协议不同，配置失败')
                    return False
                assert False
            return True
        except:
            driver.refresh()
            sleep(5)
        finally:
            repeat_times += 1
    get_log().error('配置失败')

def edit_port_forwarding(driver,upd_ip,udp_port3,udp_port4,expect_portname=None,expect_remote_ip=None,expect_portnum1=None,expect_portnum2=None,
                         expect_portnum3=None,expect_portnum4=None,expect_ip=None,expect_Protocol=None):
    """测试编辑端口功能"""
    move_to_port_forwarding_page(driver)
    repeat_times = 1
    while repeat_times < 4:
        get_log().info(f'这是第{repeat_times}次编辑端口转发')
        try:
            driver.find_element_by_xpath(port_forwarding.edit_button.format(upd_ip,udp_port3,udp_port4)).click()
            #编辑刚刚添加的UDP协议的端口转发
            if expect_portname is not None:
                driver.find_element_by_xpath(port_forwarding.input_name).clear()
                sleep(1)
                driver.find_element_by_xpath(port_forwarding.input_name).send_keys(expect_portname)
                # 输入端口名
            if expect_Protocol is not None:
                driver.find_element(By.XPATH, port_forwarding.select).click()
                WebDriverWait(driver, 10).until(EC.visibility_of_element_located((
                    By.XPATH,(port_forwarding.protocol).format(expect_Protocol)))).click()
                # 编辑协议
            if expect_remote_ip is not None:
                driver.find_element_by_xpath(port_forwarding.remote_ip).clear()
                sleep(1)
                driver.find_element_by_xpath(port_forwarding.remote_ip).send_keys(expect_remote_ip)
                # 输入外网ip
            if expect_portnum1 is not None:
                driver.find_element_by_xpath(port_forwarding.remote_port1).clear()
                sleep(1)
                driver.find_element(By.XPATH, port_forwarding.remote_port1).send_keys(expect_portnum1)
                # 输入第一个外网端口号
            if expect_portnum2 is not None:
                driver.find_element_by_xpath(port_forwarding.remote_port2).clear()
                sleep(1)
                driver.find_element(By.XPATH, port_forwarding.remote_port2).send_keys(expect_portnum2)
                # 输入第二个外网端口号
            if expect_ip is not None:
                driver.find_element_by_xpath(port_forwarding.local_ip).clear()
                sleep(1)
                driver.find_element(By.XPATH, port_forwarding.local_ip).send_keys(expect_ip)
                # 输入本地ip
            if expect_portnum3 is not None:
                driver.find_element_by_xpath(port_forwarding.local_port1).clear()
                sleep(1)
                driver.find_element(By.XPATH, port_forwarding.local_port1).send_keys(expect_portnum3)
                # 输入第一个本地端口号
            if expect_portnum4 is not None:
                driver.find_element_by_xpath(port_forwarding.local_port2).clear()
                sleep(1)
                driver.find_element(By.XPATH, port_forwarding.local_port2).send_keys(expect_portnum4)
                # 输入第二个本地端口号
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, port_forwarding.save))
            ).click()
            # 保存
            get_log().info('编辑成功')
            return True
        except:
            driver.refresh()
            sleep(5)
        finally:
            repeat_times += 1
    get_log().error('编辑失败')
    assert False

def delete_port_forwarding(driver,expect_ip,expect_portnum3,expect_portnum4):
    """测试删除端口功能"""
    move_to_port_forwarding_page(driver)
    repeat_times = 1
    while repeat_times < 4:
        get_log().info(f'这是第{repeat_times}次删除端口转发')
        try:
            driver.find_element_by_xpath(port_forwarding.delete_button.format(expect_ip,expect_portnum3,expect_portnum4)).click()
            # 删除刚刚添加的TCP协议的端口转发
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, port_forwarding.delete_affirm))
            ).click()
            #点击确定按钮
            toast=WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, port_forwarding.toast))).text
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

def check_delet_port_forwarding(driver,expect_ip,expect_portnum3,expect_portnum4,expect_operation_type):
    """检查是否删除成功"""
    repeat_times = 1
    while repeat_times < 4:
        operation_type, message_status = move_to_message_center(driver)
        if operation_type == expect_operation_type and message_status == 'Succeeded':
            move_to_port_forwarding_page(driver)
            # 判断操作类型是否正确，当操作类型正确且状态为成功时切换到端口转发页面检查数据
        else:
            get_log().error('消息中心操作类型或状态错误')
            return False
        try:
            get_log().info(f'这是第{repeat_times}次检查删除是否成功')
            if driver.find_element_by_xpath(port_forwarding.delete_ip.format(expect_ip,expect_portnum3,expect_portnum4)):
                get_log().error('删除失败')
                return False
        except:
            driver.refresh()
            sleep(5)
        finally:
            repeat_times += 1
    get_log().info('删除成功')
    return True


















