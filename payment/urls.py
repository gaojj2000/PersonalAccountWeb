# _*_ coding:utf-8 _*_
# FileName: urls.py
# IDE: PyCharm

from django.urls import path
from .views import info, login_, logout_, register

urlpatterns = [
    path('info/', info),
    path('login/', login_),
    path('logout/',logout_),
    path('register/', register)
]
