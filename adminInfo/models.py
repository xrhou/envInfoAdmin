#! /usr/bin/python
# -*- coding:utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


# Create your models here.

# 企业登录用户
@python_2_unicode_compatible
class EntUser(models.Model):
    entId = models.CharField(max_length=255, verbose_name='企业组织机构代码')
    entName = models.CharField(max_length=255, verbose_name='企业名称')
    entOrganizationCode = models.CharField(max_length=255, verbose_name='登陆企业名称')
    userpassword = models.URLField(verbose_name='登陆企业密码')
    loginTime = models.CharField(max_length=255, verbose_name='登陆时间')
    createDate = models.DateField(blank=False, verbose_name='登录用户创建时间')

    def __str__(self):
        return self.entName

    # 默认排序方式
    class Meta:
        ordering = ['entName']


# 企业所属地区
@python_2_unicode_compatible
class EntZone(models.Model):
    # 企业所属地区 安吉 德清 长兴 吴兴 南浔 开发区
    entZoneName = models.CharField(max_length=255, verbose_name='企业地区')
    entZoneCode = models.CharField(max_length=64, verbose_name='地区简称')

    def __str__(self):
        return self.entZoneCode


# 监测企业基本信息
@python_2_unicode_compatible
class Entprise(models.Model):
    entpriseId = models.CharField(max_length=32, blank=False, verbose_name='企业id')
    entUser = models.ForeignKey(EntUser, verbose_name='企业账号')
    entName = models.CharField(max_length=255, verbose_name='企业名称')
    entReperson = models.CharField(max_length=200, verbose_name='企业法人代表')
    entAddress = models.CharField(max_length=200, verbose_name='企业地址')
    entProduct = models.CharField(max_length=200, verbose_name='企业代表主要产品')
    entScale = models.CharField(max_length=200, verbose_name='企业生产规模')
    entproductCycle = models.CharField(max_length=200, verbose_name='企业生产周期')
    entCheckItem = models.CharField(max_length=200, verbose_name='主要检查项目')
    entZone = models.ForeignKey(EntZone, verbose_name='企业账号')
    entType = models.CharField(max_length=200, verbose_name='企业污染类型')  # 水污染|大气污染|固体废物|噪声|其他污染类型
    entBusiness = models.CharField(max_length=200, verbose_name='所属行业')  # 国控|省控|县区控
    entControl = models.CharField(max_length=200, verbose_name='企业被控属性')
    createDate = models.DateField(blank=True, verbose_name='企业创建时间')
    entPhone = models.DateField(max_length=20, verbose_name='联系电话')
    entPhoneName = models.CharField(max_length=20, verbose_name='联系人姓名')
    entProductAndManage = models.CharField(max_length=10240, verbose_name='企业生产和管理服务的主要内容')
    pollutionMethod = models.CharField(max_length=20, verbose_name='排放方式连续排放')
    entOtherInfo = models.CharField(max_length=20, verbose_name='企业其他信息')
    modifyDate = models.DateField(blank=True, verbose_name='修改日期')

    def __str__(self):
        return self.entName


# 企业 product 信息
@python_2_unicode_compatible
class EntProduct(models.Model):
    entprise = models.ForeignKey(Entprise, verbose_name='企业')
    entProduct = models.CharField(max_length=255, verbose_name='主要生产产品')
    entScale = models.CharField(max_length=255, verbose_name='产品生产规模')
    createDate = models.DateField(blank=True, verbose_name='创建日期')

    def __str__(self):
        return self.entProduct
