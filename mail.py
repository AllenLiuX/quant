import smtplib
from email.header import Header
from email.mime.text import MIMEText

# 第三方 SMTP 服务
mail_host = "smtp.163.com"  # SMTP服务器
# mail_user = "allenliux@163.com"  # 用户名
# mail_pass = "SPKRTDXDUUZXPXNF"  # 授权密码，非登录密码
mail_user = 'allenliux01@163.com'
mail_pass = 'QRSNTQRISGFLTXXS'

sender = 'allenliux01@163.com' # 发件人邮箱(最好写全, 不然会失败)
receivers = ['allenliux01@163.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱


def setupEmail():
    try:
        smtpObj = smtplib.SMTP_SSL(mail_host, 465)  # 启用SSL发信, 端口一般是465
        smtpObj.login(mail_user, mail_pass)  # 登录验证
        # smtpObj.sendmail(sender, receivers, message.as_string())  # 发送
        print("mail has been setup successfully.")
    except smtplib.SMTPException as e:
        print(e)
        return False
    return smtpObj

def quick_send_email(smtpObj, title, content):
    message = MIMEText(content, 'html', 'utf-8')  # 内容, 格式, 编码
    message['From'] = "{}".format(sender)
    message['To'] = ",".join(receivers)
    message['Subject'] = title
    try:
        smtpObj.sendmail(sender, receivers, message.as_string())  # 发送
        print("mail has been send successfully.")
    except smtplib.SMTPException as e:
        print(e)

def sendEmail(title, content, receivers):   # receivers should be in []
    message = MIMEText(content, 'html', 'utf-8')  # 内容, 格式, 编码
    message['From'] = "{}".format(sender)
    message['To'] = ",".join(receivers)
    message['Subject'] = title

    try:
        smtpObj = smtplib.SMTP_SSL(mail_host, 465)  # 启用SSL发信, 端口一般是465
        smtpObj.login(mail_user, mail_pass)  # 登录验证
        smtpObj.sendmail(sender, receivers, message.as_string())  # 发送
        print("mail has been send successfully.")
    except smtplib.SMTPException as e:
        print(e)
        return False
    return smtpObj


def send_email2(SMTP_host, from_account, from_passwd, to_account, subject, content):
    email_client = smtplib.SMTP(SMTP_host)
    email_client.login(from_account, from_passwd)
    # create msg
    msg = MIMEText(content, 'plain', 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')  # subject
    msg['From'] = from_account
    msg['To'] = to_account
    email_client.sendmail(from_account, to_account, msg.as_string())

    email_client.quit()


if __name__ == '__main__':
    content = '<html><body><h1>Hello</h1>' + \
              '<p>send by <a href="http://www.python.org">Python</a>...</p>' + \
              str(30000) + \
              '</body></html>'
    title = 'bitcoin report. Price: 30000'  # 邮件主题
    sendEmail(title, content)
    # send_email2(mail_host, mail_user, mail_pass, receiver, title, content)
