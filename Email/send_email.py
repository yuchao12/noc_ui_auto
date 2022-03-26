#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on 2021年12月22日
@author: yuchao
'''
import os
import zipfile
import mimetypes
import smtplib
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
import  datetime

import pytest

from common.get_log import get_log

class send():
    def make_zip(self,source_dir, output_filename):
        #打包目录为zip文件（未压缩）
        zipf  =  zipfile.ZipFile(output_filename,  'w' )
        pre_len  =  len (os.path.dirname(source_dir))
        for  parent, dirnames, filenames  in  os.walk(source_dir):
            for  filename  in  filenames:
                pathfile  =  os.path.join(parent, filename)
                arcname  =  pathfile[pre_len:].strip(os.path.sep)      #相对路径
                zipf.write(pathfile, arcname)
        zipf.close()

    def send_emial(self):
        filepath = r'D:\noc_auto\测试报告文件.zip'
        smtp_server = "smtp.qq.com"
        username = "2373551676@qq.com"
        password = "xidhoahntzfpecbc"
        sender = '2373551676@qq.com'
        # 添加其他邮箱  用逗号分隔
        receivers = '3207707507@qq.com','chao.yu@hyku.com','2373551676@qq.com','1475083550@qq.com'
        time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        msg = MIMEMultipart()
        # 邮件正文
        msg.attach(MIMEText("请先下载附件之后,解开压缩包,使用pycharm打开里面的index.html文件。{}".format(time),'plain','utf-8'))
        msg['From'] = username  # 发件人
        msg['To'] = ";".join(receivers)   # 收件人
        subject = 'NOC自动化测试报告' # 邮件主题
        msg['Subject'] = subject
        data = open(filepath, 'rb')
        ctype, encoding = mimetypes.guess_type(filepath)
        if ctype is None or encoding is not None:
            ctype = 'application/octet-stream'
        maintype, subtype = ctype.split('/', 1)
        file_msg = MIMEBase(maintype, subtype)
        file_msg.set_payload(data.read())
        data.close()
        encoders.encode_base64(file_msg)  # 把附件编码
        file_msg.add_header('Content-Disposition', 'attachment', filename="测试报告.zip")  # 修改邮件头
        msg.attach(file_msg)
        try:
            server = smtplib.SMTP(smtp_server,25)
            server.login(username,password)
            server.sendmail(sender,receivers,msg.as_string())
            server.quit()
            get_log().info("发送成功")
        except Exception as err:
            get_log().info("发送失败")

