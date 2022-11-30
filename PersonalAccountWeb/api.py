# _*_ coding:utf-8 _*_
# FileName: api.py
# IDE: PyCharm

from time import time
from ninja import NinjaAPI

api = NinjaAPI()


@api.get('/server_timestamp')
def hello(request):
    return time()
