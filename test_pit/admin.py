from django.contrib import admin
from .models import Project
from django.contrib.admin import ModelAdmin


# 第一步创建ModelAdmin的继承类
class ProjectAdmin(ModelAdmin):
    # 第二步：指定要显示的字段
    list_display = ['id', 'name', 'version', 'type', 'status', 'created_by', 'created_at']
    list_display_links = ['id', 'name']
    # 第三步：指定可过滤的列
    list_filter = ['created_at', 'type']
    # 第四步：指定可查询的列
    search_fields = ['name']



# Register your models here.
admin.site.register(Project, ProjectAdmin)

admin.site.site_header = '自动化测试平台后台管理'
admin.site.site_title = '测试平台后台'
