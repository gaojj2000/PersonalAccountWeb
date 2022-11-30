#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PersonalAccountWeb.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    # pip install django django-ninja
    # django-admin startproject PersonalAccountWeb  # 创建django项目
    # django-admin startapp payment  # 创建 Payment app
    # python manage.py makemigrations  # 生成牵引文件
    # python manage.py migrate  # 执行牵引
    # python manage.py createsuperuser  # 创建管理员（admin/gjj052027）
    # python manage.py shell  # 交互式
    # python manage.py runserver 127.0.0.1:8000  # 启动django
    main()
