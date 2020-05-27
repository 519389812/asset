from django.contrib import admin
from user.models import User
from django.contrib.auth.admin import UserAdmin


admin.site.register(User, UserAdmin)

admin.site.site_header = '资产管理系统'
admin.site.site_title = '资产管理系统'
admin.site.index_title = '资产管理系统'
