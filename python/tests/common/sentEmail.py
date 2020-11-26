# coding=utf-8
import smtplib
import os.path
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
def sent(title=None,text=None,touser=None,reports=None):
    #标题，如果为空则默认
    if title== None:
        title = '默认的邮件标题'
    else:
        title =title
    # 正文，如果为空则默认
    if text == None:
        text = '默认的正文内容'
    else:
        text = text
    # 发送人，如果为空则默认
    if touser == None:
        touser = ['954087620@qq.com']
    else:
        touser = touser
    # 发送人
    msg_to = touser

    # 创建一个带附件的实例
    msg = MIMEMultipart()
    # subject = '测试一下邮件发送功能带附件'
    subject = title
    msg['Subject'] = Header(subject, 'utf-8')

    # 邮件正文内容
    msg.attach(MIMEText(text, 'plain', 'utf-8'))

    #附件，没有就不发送
    if reports != None:
        # 构造附件1，传送当前目录下的 test.txt 文件
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../"+reports)
        att1 = MIMEText(open(path, 'rb').read(), 'base64', 'utf-8')
        att1["Content-Type"] = 'application/octet-stream'
        # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
        att1["Content-Disposition"] = 'attachment; filename='+ reports
        msg.attach(att1)
    msg_from = '3538187083@qq.com'#发送邮件的账号
    passwd = 'wkcvjqvxsjjpcijf'#发送邮件的密码
    msg['From'] = msg_from
    msg['To'] = ','.join(msg_to)
    try:
        s = smtplib.SMTP_SSL("smtp.qq.com", 465)
        s.login(msg_from, passwd)
        s.sendmail(msg_from, msg_to, msg.as_string())
        print("发送邮件成功")
        return ("发送成功")
    except Exception as e:
        print("发送邮件失败")
        print(e.args)
        print(str(e))
        print(repr(e))
        return ("发送失败")
