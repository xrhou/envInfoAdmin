# ! /usr/bin/python
# -*- coding:utf-8 -*-

# Register your models here.
from django.contrib import admin

from .models import Entprise, EntUser, EntProduct, EntZone


# EntUserAdmin
class EntUserAdmin(admin.ModelAdmin):
    list_display = ('entId', 'entName', 'entOrganizationCode', 'userpassword', 'createDate')
    search_fields = ('entName',)  # 企业名称
    list_per_page = 10


# EntpriseAdmin
class EntpriseAdmin(admin.ModelAdmin):
    list_display = ('entpriseId', 'entName', 'entReperson', 'entAddress', 'entPhone')
    search_fields = ('entName', 'entZone')  # 查询Entprise
    list_per_page = 10


# EntProductAdmin
class EntProductAdmin(admin.ModelAdmin):
    list_display = ('entProduct', 'entScale')
    search_fields = ('entProduct',)  # 查询product
    list_per_page = 10


# EntZoneAdmin
class EntZoneAdmin(admin.ModelAdmin):
    list_display = ('entZoneName', 'entZoneCode')
    search_fields = ('entZoneName',)  # 企业所属地区
    list_per_page = 10


admin.site.register(EntUser, EntUserAdmin)
admin.site.register(Entprise, EntpriseAdmin)
admin.site.register(EntProduct, EntProductAdmin)
admin.site.register(EntZone, EntZoneAdmin)
