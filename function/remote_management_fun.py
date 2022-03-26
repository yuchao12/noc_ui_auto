#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on 2021年10月26日
@author: yuchao
'''

from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from common.get_log import get_log
from common.user_public_fun import move_to_message_center
from data.conf import except_sn
from xpath.remote_management import remote_management
def move_to_remote_management_fun_page(driver):
    """ 移动到remote_management的页面，即远程管理页面"""
    repeat_times = 1
    while repeat_times < 4:
        get_log().info(f'这是第{repeat_times}次进入')
        try:
            if remote_management.expect_url.format(except_sn) == driver.current_url:
                get_log().info('刷新页面')
                driver.refresh()
            else:
                driver.find_element(By.XPATH, remote_management.move_set).click()
                # 打开高级设置菜单
                sleep(2)
                ActionChains(driver).click(
                    driver.find_element_by_xpath(remote_management.move_remote_management)).perform()
                # 进入到远程管理的页面
                sleep(2)
            actul_url = driver.current_url
            # 获取当前页面的url
            if actul_url == remote_management.expect_url.format(except_sn):
                # 与远程管理相同URL相同
                get_log().info('进入远程管理页面成功')
                return True
        except:
            driver.refresh()
            sleep(5)
            pass
        finally:
            repeat_times += 1
    get_log().error('进入远程管理页面失败')
    assert False

def add_web_wan_access(driver,expect_status,expect_port,expect_ip=None):
    """添加远程管理"""
    sleep(3)
    move_to_remote_management_fun_page(driver)
    repeat_times = 1
    while repeat_times < 4:
        get_log().info(f'这是第{repeat_times}次进入')
        try:
            wwa_status_class = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, remote_management.access_button))
            ).get_attribute('class')
            # 查询web wan access 的开关状态
            if wwa_status_class == expect_status:
                get_log().info('web wan access 是勾选状态')
            else:
                get_log().info('web wan access 是未勾选状态')
                sleep(3)
                WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((
                        By.XPATH, remote_management.access_button))).click()
                #开启web wan access
            sleep(1)
            driver.find_element_by_xpath(remote_management.port).clear()
            #清空端口输入框
            sleep(2)
            driver.find_element_by_xpath(remote_management.port).send_keys(expect_port)
            #输入端口
            if expect_ip is not None:
                #ip地址可以为空
                sleep(1)
                driver.find_element_by_xpath(remote_management.ip).clear()
                # 清空ip地址输入框
                sleep(2)
                driver.find_element_by_xpath(remote_management.ip).send_keys(expect_ip)
                # 输入ip地址
            sleep(1)
            driver.find_element(By.XPATH, remote_management.save_button).click()
            # 保存设置
            toast=WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, remote_management.toast))).text
            get_log().info('toast提示'+toast)
            get_log().info('添加远程管理成功')
            return True
        except:
            driver.refresh()
            sleep(5)
        finally:
            repeat_times += 1
    get_log().error('添加远程管理失败')
    assert False

def check_web_wan_access(driver,expect_operation_type,expect_status=None,expect_port=None,expect_ip=None):
    """检查配置是否与预期的配置相同"""
    repeat_times = 1
    while repeat_times < 4:
        operation_type, message_status = move_to_message_center(driver)
        if operation_type == expect_operation_type and message_status == 'Succeeded':
            move_to_remote_management_fun_page(driver)
            # 判断操作类型是否正确，当操作类型正确且状态为成功时切换到端口转发页面检查数据
        else:
            get_log().error('消息中心操作类型或状态错误')
            return False
        try:
            get_log().info(f'这是第{repeat_times}次检查web wan access页面')
            if expect_status is not None:
                actual_status = WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located(
                        (By.XPATH, remote_management.access_button))).get_attribute("class")
                #获取到web wan access 的开启状态
                get_log().info("实际的状态：" + actual_status)
                get_log().info("期望的状态：" + expect_status)
                if actual_status != expect_status:
                    if repeat_times==3:
                        get_log().error('期望的状态与实际的状态不一致')
                        return False
                    assert False
            if expect_port is not None:
                #获取web wan access的端口值
                actual_port = WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located(
                        (By.XPATH, remote_management.port))).get_attribute('value')
                get_log().info("实际的端口号：" + actual_port)
                get_log().info("期望的端口号：" + expect_port)
                if actual_port != expect_port:
                    if repeat_times==3:
                        get_log().error('期望的端口号与实际的端口号不一致')
                        return False
                    assert False
            if expect_ip is not None:
                #获取web wan access的ip
                actual_ip = WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located(
                        (By.XPATH, remote_management.ip))).get_attribute('value')
                get_log().info("实际的ip：" + actual_ip)
                get_log().info("期望的ip：" + expect_ip)
                if actual_ip != expect_ip:
                    if repeat_times==3:
                        get_log().error('期望的ip与实际的ip不一致')
                        return False
                    assert False
            return True
        except:
            driver.refresh()
            sleep(3)
        finally:
            repeat_times += 1
    get_log().error('检查远程管理失败')
    assert False

def change_web_wan_access(driver, expect_status, expect_port=None, expect_ip=None):
    """测试编辑远程管理功能"""
    move_to_remote_management_fun_page(driver)
    repeat_times = 1
    while repeat_times < 4:
        get_log().info(f'这是第{repeat_times}次进入')
        try:
            wwa_status_class = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, remote_management.access_button))
            ).get_attribute('class')
            # 查询web wan access 的开关状态
            if wwa_status_class == expect_status:
                get_log().info('web wan access 是勾选状态')
            else:
                get_log().info('web wan access 是未勾选状态')
                sleep(3)
                WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((
                        By.XPATH, remote_management.access_button))).click()
                #开启web wan access
            if expect_port is not None:
                driver.find_element_by_xpath(remote_management.port).clear()
                #清空端口输入框
                driver.find_element_by_xpath(remote_management.port).send_keys(expect_port)
                #输入端口
            if expect_ip is not None:
                #ip地址可以为空
                driver.find_element_by_xpath(remote_management.ip).clear()
                # 清空ip地址输入框
                driver.find_element_by_xpath(remote_management.ip).send_keys(expect_ip)
                # 输入ip地址
            driver.find_element(By.XPATH, remote_management.save_button).click()
            # 保存设置
            toast=WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, remote_management.toast))).text
            get_log().info('toast提示'+toast)
            get_log().info('修改远程管理成功')
            return True
        except:
            driver.refresh()
            sleep(5)
        finally:
            repeat_times += 1
    get_log().error('修改远程管理失败')
    assert False
