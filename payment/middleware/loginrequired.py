# _*_ coding:utf-8 _*_
# FileName: loginrequired.py
# IDE: PyCharm

from django.shortcuts import render  # redirect
from django.conf import settings


class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.login_url = settings.LOGIN_URL
        self.open_urls = [self.login_url] + settings.OPEN_URLS

    def __call__(self, request):
        if not request.user.is_authenticated:
            print(f'request.path_info {request.path_info}')
            if request.path_info not in self.open_urls:
                return render(request, template_name='index.html')
                # return redirect(self.login_url + '?next=' + request.path_info)
        return self.get_response(request)
