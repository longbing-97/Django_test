from django.contrib import admin
from .models import Project, ProjecMember, DeployEnv
from django.contrib.admin import ModelAdmin


# 项目内联类
class ProjectMemberInline(admin.TabularInline):
    # 定义需要内联的models数据类
    model = ProjecMember


class DeployEnvInline(admin.TabularInline):
    model = DeployEnv
    extra = 2


# 第一步创建ModelAdmin的继承类
class ProjectAdmin(ModelAdmin):
    # 第二步：指定要显示的字段
    list_display = ['id', 'name', 'version', 'type', 'status', 'created_by', 'created_at']
    list_display_links = ['id', 'name']
    # 第三步：指定可过滤的列
    list_filter = ['created_at', 'type']
    # 第四步：指定可查询的列
    search_fields = ['name']
    # 项目内联
    inlines = [ProjectMemberInline, DeployEnvInline]


# Register your models here.
admin.site.register(Project, ProjectAdmin)


class ProjecMemberAdmin(ModelAdmin):
    list_display = ['id', 'project', '__str__', 'join_date', 'role', 'status']
    list_display_links = ['__str__']
    list_filter = ['join_date', 'role', 'status']
    search_fields = ['user__first_name', 'user__username']


admin.site.register(ProjecMember, ProjecMemberAdmin)


class DeployEnvAdmin(ModelAdmin):
    list_display = ['id', 'project', 'name', 'hostname', 'port', 'status']
    list_display_links = ['name']
    list_filter = ['status']
    search_fields = ['name', 'hostname', 'memo']


admin.site.register(DeployEnv, DeployEnvAdmin)
admin.site.site_header = '自动化测试平台后台管理'
admin.site.site_title = '测试平台后台'
