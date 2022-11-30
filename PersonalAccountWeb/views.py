# _*_ coding:utf-8 _*_
# FileName: views.py
# IDE: PyCharm

from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from django.conf import settings
from random import sample
from base64 import b64encode
from captcha.image import ImageCaptcha
import smtplib
from time import time
from json import loads
from email.header import Header
from email.mime.text import MIMEText


def verification_code(request):
    image = ImageCaptcha()
    # 获得随机生成的验证码
    captcha = ''.join(sample(list('abcdefghijklmnopqrstuvwxyz'), 4))
    print("生成的验证码为：", captcha)
    response = HttpResponse(image.generate(captcha), content_type='image/png')
    # response['Access-Control-Allow-Origin'] = '*'
    # response['Access-Control-Allow-Credentials'] = 'true'
    response.set_cookie('yzm', b64encode(captcha.encode()).decode(), max_age=60 * 5)
    return response


def send_email_(to_address, header, html):
    smtp_server = settings.EMAIL_HOST
    msg = MIMEText(html, 'html', 'utf-8')
    msg['From'] = Header(settings.EMAIL_HOST_USER)
    msg['To'] = Header(to_address)
    msg['Subject'] = Header(header)
    server = smtplib.SMTP_SSL(smtp_server)
    server.connect(smtp_server, settings.EMAIL_PORT)
    server.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)  # python_gjj
    server.sendmail(settings.EMAIL_HOST_USER, to_address, msg.as_string())
    server.quit()


def send_email(request):
    if request.method == 'POST':
        to_address = loads(request.body)['email']
        if User.objects.filter(email=to_address):
            response = JsonResponse({'code': -1, 'msg': '邮箱已被注册！'})
        else:
            captcha = ''.join(sample(list('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'), 6))
            print("生成的邮件验证码为：", captcha)
            send_email_(to_address=to_address, header='邮箱验证码', html=f"""
            <h1>【个人记账分析系统】</h1>
            <p>您好，您正在注册我们的网站：<span style='color: red'><a href="http://{settings.CSRF_TRUSTED_ORIGINS[0]}">个人记账分析系统</a></span></p>
            <p>您本次注册的验证码是：<span style='color: blue'>{captcha}</span></p>
            <p>如果您<span style='color: red'>没有注册</span>，请<span style='color: red'>忽略并删除</span>本邮件！</p>
            <p>感谢您对本系统的信赖！</p>
            """)
            request.session['yzm'] = captcha
            request.session['email'] = to_address
            response = JsonResponse({'code': 0, 'msg': '邮箱验证码发送成功！请注意查收！'})
    else:
        response = JsonResponse({'code': 1, 'msg': '请求方法只能是POST方法！'})
    response.set_cookie('last', str(time()), max_age=60)
    return response
