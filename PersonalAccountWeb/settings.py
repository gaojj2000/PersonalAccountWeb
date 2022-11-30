"""
Django settings for PersonalAccountWeb project.

Generated by 'django-admin startproject' using Django 3.2.16.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

# 默认：chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
# SECRET_KEY= django-insecure-wqs_ya&nsui-dr6(-#(sx%naw3gt#gj3sioxjfqq-e@3iu-54j
SECRET_KEY = 'django-insecure-gjj&zgl&zyy&xlh@ljl&wly&wyf#hcz&xyh&qld&cml#gj&wsy'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',  # pip install django-cors-headers
    'payment',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',  # pip install django-cors-headers
    'payment.middleware.loginrequired.LoginRequiredMiddleware'
]

ROOT_URLCONF = 'PersonalAccountWeb.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'PersonalAccountWeb.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',  # mysqlclient（需要手动搜索安装）
#         'HOST': '127.0.0.1',
#         'PORT': '3306',
#         'NAME': 'PA',
#         'USER': 'root',
#         'PASSWORD': 'hczgjjXXXXXX',
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# 添加白名单
CORS_ORIGIN_WHITELIST = (
    'http://127.0.0.1:3000',
    'https://127.0.0.1:3000',
    'http://localhost:3000',
    'https://localhost:3000',
)
CORS_ALLOW_CREDENTIALS = True  # 允许携带cookie

LOGIN_URL = 'http://127.0.0.1:3000/Home/Login'
OPEN_URLS = ['/login/', '/register/', '/yzm/', '/email/', '/api/', '/api/server_timestamp']

X_FRAME_OPTIONS = 'ALLOW-FROM http://127.0.0.1:3000'
CSRF_TRUSTED_ORIGINS = ['127.0.0.1:3000']
CSRF_COOKIE_SAMESITE = None

CSRF_COOKIE_NAME = 'csrf'  # CSRF 的 key 名称
CSRF_COOKIE_AGE = 60 * 60 * 24 * 7  # 存活时间
CSRF_COOKIE_DOMAIN = None  # 在那个域名下生效
CSRF_HEADER_NAME = 'HTTP_X_CSRFTOKEN'  # 请求头的名称

SESSION_ENGINE = 'django.contrib.sessions.backends.db'   # 引擎（默认）
SESSION_COOKIE_AGE = 60 * 30  # 设置session过期时间为30分钟（默认2周）
SESSION_COOKIE_NAME = "sessionid"  # Session的cookie保存在浏览器上时的key，即：sessionid＝随机字符串（默认）
SESSION_COOKIE_PATH = "/"  # Session的cookie保存的路径（默认）
SESSION_COOKIE_DOMAIN = None  # Session的cookie保存的域名（默认）
SESSION_COOKIE_SECURE = True  # 是否Https传输cookie（默认False）
SESSION_COOKIE_HTTPONLY = True  # 是否Session的cookie只支持http传输（默认）,如果设置为 True，客户端的 JavaScript 将无法访问会话 cookie。
SESSION_COOKIE_SAMESITE = 'None'  # 会话 cookie 上的 SameSite 标志的值。这个标志可以防止 cookie 在跨站请求中被发送，从而防止 CSRF 攻击，使一些窃取会话 cookie 的方法变得不可能。(默认Lax)
SESSION_SAVE_EVERY_REQUEST = True  # 每次请求都要保存一下session（默认修改后才保存）
SESSION_EXPIRE_AT_BROWSER_CLOSE = True  # 当浏览器被关闭的时候将session失效，但是不能删除数据库的session数据（为True时 SESSION_COOKIE_AGE 将失效）

# SESSION_ENGINE 配置的可能值为：
# django.contrib.sessions.backends.db：数据库，数据库用于做持久化
# django.contrib.sessions.backends.cached_db：缓存+数据库，缓存用于提高效率
# django.contrib.sessions.backends.signed_cookies：加密 cookie session

# SESSION_COOKIE_SAMESITE 配置的可能值为：
# 'Strict'：防止浏览器在所有跨站点浏览的情况下向目标站点发送 cookie，即使在使用常规链接时也是如此。
# 'Lax'：为希望在用户从外部链接到达后保持用户登录会话的网站提供安全和可用性之间的平衡。
# 'None'：会话 cookie 将随所有同站和跨站请求发送。（此时需要配合 SESSION_COOKIE_SECURE 为 True ，否则浏览器会拦截）
# False：停用该标志。
# 现代浏览器为 SameSite 标志提供了一个更安全的默认策略，并将假定 Lax 为没有明确配置值的 cookies。

# 邮箱引擎
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# 邮箱服务器地址
EMAIL_HOST = 'smtp.sina.com'
# 邮箱服务器端口
EMAIL_PORT = 465
# 发送邮件的邮箱
EMAIL_HOST_USER = 'python_362@sina.com'
# 在邮箱中设置的客户端授权密码
EMAIL_HOST_PASSWORD = '7949683787d361a1'
# 收件人看到的发件人
EMAIL_FROM = '个人记账分析系统<gjj>'
