#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on 2021年9月22日
@author: yuchao
'''

# ===========================================================================
"""进入noc"""
#url = model_select.url
url ='https://noc.merckuwifi.net/login'
# ===========================================================================
"""登录账号密码"""
#root_password = model_select.root_username
#root_username = model_select.root_password
root_password = '12345678'
root_username = '123456'
"""搜索sn"""
#except_sn='060052102000892'
except_sn='060052041000034'
#except_sn='010011832201609'
"""web wan access  远程管理模块====================================================================================="""
"""remote_management"""
"""【保存】开关打开时，且当端口号和IP地址格式都正确，点击“保存”后有toast提示【NOC-7391】"""
add_web_wan_access = {
 "port_num":"15451", #端口号
"ip_ad":"192.168.127.223" ,#ip地址
"swith_on":"el-checkbox__input is-checked" ,# web wan access 勾选的状态
 "type":"Web WAN Access" # 操作类型
}
"""【正确性检查】能正常修改配置，并下发成功【NOC-10087】"""
change_web_wan_access = {
 "port_num":"2333", #端口号
"ip_ad":"192.168.127.133" ,#ip地址
"swith_on":"el-checkbox__input is-checked" ,# web wan access 开启的状态
 "type":"Web WAN Access" # 操作类型
}
"""端口转发模块====================================================================================================="""
"""Port_Forwarding"""
"""新增一条协议为”TCP&UDP“的端口转发[NOC-8365]"""
TCP_UDP_Port_forwarding = {
 "local_ip" : "192.168.127.126", # 本地ip
 "remote_ip": "12.11.0.0",  #  外网ip
 "name" : "121x00x2", # 端口名
 "port_num1" : "20000" , # 第一个外网端口号
 "port_num2" : "20005" , # 第二个外网端口号
 "port_num3" : "20000" , # 第一个本地端口号
 "port_num4" : "20005" , # 第二个本地端口号
 "Protocol_TCP/UDP" : "TCP/UDP",  # TCP/UDP协议
 "type" :"Add port forwarding"  #操作类型
}
"""新增一条协议为”TCP“的端口转发[NOC-8366]"""
TCP_Port_forwarding = {
 "local_ip" : "192.168.127.139", # 本地ip
 "remote_ip": "10.70.0.2",  #  外网ip
 "name" : "2333SD", # 端口名二
 "port_num1" : "20006" , # 第一个外网端口号
 "port_num2" : "20009" , # 第二个外网端口号
 "port_num3" : "20006" , # 第一个本地端口号
 "port_num4" : "20009", # 第二个本地端口号
 "Protocol_TCP" : "TCP" , # TCP 协议
"type" :"Add port forwarding"  #操作类型
}
"""新增一条协议为”UDP“的端口转发[NOC-8367]"""
UDP_Port_forwarding = {
 "local_ip" : "192.168.127.122", # 本地ip
 "remote_ip": "199.70.0.2",  #  外网ip
 "name" : "2SADSAD", # 端口名
 "port_num1" : "1" , # 第一个外网端口号
 "port_num2" : "2" , # 第二个外网端口号
 "port_num3" : "1" , # 第一个本地端口号
 "port_num4" : "2", # 第二个本地端口号
 "Protocol_UDP" : "UDP",  # UDP 协议
"type" :"Add port forwarding"  #操作类型
}
"""修改所有的信息能修改成功[NOC-8329]"""
"""修改上条用例添加的UDP协议的端口转发"""
edit_Port_forwarding = {
 "local_ip" : "192.168.127.141", # 本地ip
 "remote_ip": "199.10.1.3",  #  外网ip
 "name" : "29xx89D", # 端口名
 "port_num1" : "3" , # 第一个外网端口号
 "port_num2" : "4" , # 第二个外网端口号
 "port_num3" : "3" , # 第一个本地端口号
 "port_num4" : "4", # 第二个本地端口号
 "Protocol_TCP/UDP" : "TCP/UDP",  # TCP/UDP 协议
"type" :"Modify port forwarding"  #操作类型
}
"""端口转发：列表删除按钮，点击有toast提示[NOC-8386]"""
"""删除上条用例添加的TCP协议的端口转发"""
delete_Port_forwarding = {
 "local_ip" : "192.168.127.139", # 本地ip
 "port_num3" : "20006" , # 第一个本地端口号
 "port_num4" : "20009",  # 第二个本地端口号
"type" :"Remove port forwarding"  #操作类型
}
"""vpn 模块=========================================================================================================="""
PPTP_vpn={
"name" : "张三123abcABC../", # vpn 名称
"server" : "vpn.hyku.org",  # 服务器名称
"username" : "ycccccc", # 用户名
"protocol" : "PPTP", # pptp协议
"password" : "123456789" , # 密码
 "mppe" : "MPPE", # 勾选mppe
 "mppc": "MPPC", # 勾选mppc
 "checkbox_status" : "el-checkbox is-checked", # 复选框状态
 "type" :"Add VPN" #操作类型
}
L2TP_vpn={
"name" : "dasdaskjx", # vpn 名称
"server" : "vpn.hyku",  # 服务器名称
"username" : "cccc", # 用户名
"protocol" : "L2TP", # pptp协议
"password" : "123456789" , # 密码
 "type" :"Add VPN" #操作类型
 }

edit_vpn={
"name" : "dsdsasad", # vpn 名称
"server" : "vpn.org",  # 服务器名称
"username" : "sdsl12sd", # 用户名
"protocol" : "PPTP", # pptp协议
"password" : "1dsf2589" , # 密码
 "mppe" : "MPPE", # 勾选mppe
 "mppc": "MPPC", # 勾选mppc
 "checkbox_status" : "el-checkbox is-checked", # 复选框状态
 "type" :"Modify VPN"  } #操作类型

delet_vpn={
"name" : "张三123abcABC../", # vpn 名称
 "type": "Delete VPN"  # 操作类型
}
