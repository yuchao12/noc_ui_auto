#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on 2021年10月24日
@author: yuchao
'''

from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from common.get_log import get_log
from xpath.user_public import UserPublicLocators

"""公共功能"""
# 搜索sn，进入到设备详情页【前提条件是设备已经上报noc】
def search_sn_and_click(driver, expect_sn, except_status, check_times=1):
    # 输入框输入sn
    while check_times > 0:
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, UserPublicLocators.sn_input))).click()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, UserPublicLocators.sn_input))).send_keys(expect_sn)
        # 点击查询
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, UserPublicLocators.search_button))).click()
        time.sleep(1)
        try:
            devices_status = driver.find_elements_by_xpath(UserPublicLocators.devices_status)[0].get_attribute("class")
            get_log().info('设备状态是'+devices_status)
            if except_status in devices_status:
                # 进入某设备详情页
                driver.find_elements_by_xpath(UserPublicLocators.enter_devices)[0].click()
                time.sleep(5)
                get_log().info('选择指定设备成功')
                return
            else:
                assert False
        except:
            driver.refresh()
            time.sleep(5)
        finally:
            check_times -= 1
    get_log().error('设备不在线')
    assert False


def move_to_message_center(driver, result=None):
    repeat_times = 3
    while repeat_times > 0:
        get_log().info(f'这是进入setting/messages页倒数第{repeat_times}次')
        try:
            # 判断当前页面是否为消息中心页
            if "setting/messages" in driver.current_url:
                get_log().info('刷新')
                driver.refresh()
            else:
                # 鼠标移动到消息中心
                ActionChains(driver).move_to_element(
                    driver.find_element_by_xpath(UserPublicLocators.message_center_menu)).perform()
                time.sleep(0.5)
                # 点击消息中心菜单
                driver.find_element_by_xpath(UserPublicLocators.message_center_menu).click()
                time.sleep(0.5)
            # 等待进度条加载完成
            WebDriverWait(driver, 20).until_not(
                EC.element_to_be_clickable((By.XPATH, UserPublicLocators.loading))
            )
            time.sleep(0.5)
            get_log().info('进入消息中心页面成功')
            time.sleep(20)
            driver.refresh()
            # 获取第一行的操作方法
            operation_type = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, UserPublicLocators.operation_type))
            ).text
            # 获取第一行的状态
            message_status = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, UserPublicLocators.message_status))
            ).text
            get_log().info('公共用例: '+operation_type + ' ' + message_status)
            # 如果结果行显示View，进行点击
            if result == 'View':
                WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, UserPublicLocators.message_result))
                ).click()
            return operation_type, message_status
        except:
            driver.refresh()
            time.sleep(2)
        finally:
            repeat_times -= 1
    get_log().error("进入消息页面获取数据失败")
    assert False