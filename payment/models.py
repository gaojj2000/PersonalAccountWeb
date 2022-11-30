from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Setting(models.Model):
    sex = models.CharField(null=True, blank=True, verbose_name='性别', max_length=2)
    heads = models.ImageField(null=True, blank=True, verbose_name='头像')  # pip install pillow
    wx_rules = models.TextField(null=True, blank=True, verbose_name='微信收支规则')
    zfb_rules = models.TextField(null=True, blank=True, verbose_name='支付宝收支规则')
    last_ip = models.GenericIPAddressField(null=True, blank=True, verbose_name='上次登录IP地址')
    owner = models.ForeignKey(User, models.CASCADE)

    class Meta:
        verbose_name = '用户设置'
        verbose_name_plural = verbose_name
        db_table = 'setting'
        ordering = ('-id',)


class Wechat(models.Model):
    trading_time = models.DateTimeField(null=True, blank=True, verbose_name='交易时间')
    transaction_type = models.CharField(null=True, blank=True, verbose_name='交易类型', max_length=8)
    other_trade = models.CharField(null=True, blank=True, verbose_name='交易对方', max_length=255)
    goods = models.CharField(null=True, blank=True, verbose_name='商品', max_length=255)
    in_out = models.CharField(null=True, blank=True, verbose_name='收/支', max_length=4)
    amount = models.CharField(null=True, blank=True, verbose_name='金额(元)', max_length=11)
    payment_method = models.CharField(null=True, blank=True, verbose_name='支付方式', max_length=22)
    current_status = models.CharField(null=True, blank=True, verbose_name='当前状态', max_length=10)
    transaction_order_number = models.CharField(blank=True, verbose_name='交易单号', max_length=255, primary_key=True)
    business_order_number = models.CharField(null=True, blank=True, verbose_name='商户单号', max_length=255)
    remarks = models.CharField(null=True, blank=True, verbose_name='备注', max_length=255)
    owner = models.ForeignKey(User, models.CASCADE)

    class Meta:
        verbose_name = '微信账单流水'
        verbose_name_plural = verbose_name
        db_table = 'wechat'
        ordering = ('-transaction_order_number',)


class Alipay(models.Model):
    in_out = models.CharField(null=True, blank=True, verbose_name='收/支', max_length=4)
    trade_user = models.CharField(null=True, blank=True, verbose_name='交易对方', max_length=255)
    other_account = models.CharField(null=True, blank=True, verbose_name='对方账号', max_length=255)
    product_description = models.CharField(null=True, blank=True, verbose_name='商品说明', max_length=255)
    in_out_method = models.CharField(null=True, blank=True, verbose_name='收/付款方式', max_length=22)
    amount = models.CharField(null=True, blank=True, verbose_name='金额', max_length=11)
    trading_status = models.CharField(null=True, blank=True, verbose_name='交易状态', max_length=10)
    transactions_classification = models.CharField(null=True, blank=True, verbose_name='交易分类', max_length=8)
    transaction_order_number = models.CharField(blank=True, verbose_name='交易订单号', max_length=255, primary_key=True)
    business_order_number = models.CharField(null=True, blank=True, verbose_name='商家订单号', max_length=255)
    trading_time = models.DateTimeField(null=True, blank=True, verbose_name='交易时间')
    owner = models.ForeignKey(User, models.CASCADE)

    class Meta:
        verbose_name = '支付宝账单流水'
        verbose_name_plural = verbose_name
        db_table = 'alipay'
        ordering = ('-transaction_order_number',)
