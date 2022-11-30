from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from json import loads
from .models import Setting

# Create your views here.


def login_(request):
    if request.method == 'POST':
        username = loads(request.body)['username']
        password = loads(request.body)['password']
        user = User.objects.filter(username=username) or User.objects.filter(email=username)
        if user:
            user = authenticate(username=user[0].username, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                    Setting.objects.create(last_ip=request.META['REMOTE_ADDR'], owner=user)
                    request.session['uname'] = user.username
                    request.session['admin'] = user.is_superuser
                    response = JsonResponse({'code': 0, 'msg': '登录成功！'})
                    response.set_cookie('uname', user.username)
                    return response
                return JsonResponse({'code': -1, 'msg': '用户状态不可用！'})
            return JsonResponse({'code': -2, 'msg': '用户名密码错误！'})
        return JsonResponse({'code': -3, 'msg': '用户名不存在！'})
    return JsonResponse({'code': 1, 'msg': '请求方法只能是POST方法！'})


def register(request):
    if request.method == 'POST':
        username = loads(request.body)['username']
        password = loads(request.body)['password']
        email = loads(request.body)['email']
        yzm = loads(request.body)['yzm']
        if User.objects.filter(username=username):
            return JsonResponse({'code': -1, 'msg': '用户名已存在！'})
        if request.session.get('email') != email or request.session.get('yzm') != yzm:
            return JsonResponse({'code': -2, 'msg': '邮箱验证码错误！'})
        user = User.objects.create_user(username=username, password=password, email=email)
        if user.username:
            return JsonResponse({'code': 0, 'msg': '注册成功！'})
        return JsonResponse({'code': -3, 'msg': '注册失败！请重新尝试注册！'})
    return JsonResponse({'code': 1, 'msg': '请求方法只能是POST方法！'})


def logout_(request):
    if request.user.is_authenticated:
        logout(request)
        return JsonResponse({'code': 0, 'msg': '您已登出！'})
    return JsonResponse({'code': -1, 'msg': '您尚未登录！'})


def info(request):
    if request.method == 'GET':
        setting = Setting.objects.filter(owner=request.user)
        data = {
            'username': request.user.username,
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
            'email': request.user.email,
            'is_superuser': request.user.is_superuser
        }
        if setting:
            setting = setting[0]
            data.update({
                'sex': setting.sex,
                'wx_rules': setting.wx_rules,
                'zfb_rules': setting.zfb_rules,
                'last_ip': setting.last_ip
            })
        return JsonResponse({'code': 0, 'msg': '成功获取个人信息！', 'data': data})
    return JsonResponse({'code': 1, 'msg': '请求方法只能是GET方法！'})
