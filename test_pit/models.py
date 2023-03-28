from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Project(models.Model):
    # 产品类型字典
    PROJECT_TYPE = ((1, 'Web'), (2, 'App'), (3, '微服务'))
    # 自增字段，主键
    id = models.AutoField(primary_key=True)
    # 项目名称
    name = models.CharField(max_length=200, verbose_name='测试项目名称')
    # 版本
    version = models.CharField(max_length=20, verbose_name='版本')
    # 产品类型
    type = models.IntegerField(verbose_name='产品类型', choices=PROJECT_TYPE)
    # 描述
    description = models.CharField(max_length=200, verbose_name="项目描述", blank=True, null=True)
    # 状态
    status = models.BooleanField(default=True, verbose_name='状态')
    # 创建人
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name='创建人')
    # 创建时间
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    # 最后更新时间
    update_at = models.DateTimeField(auto_now=True, verbose_name='最近更新时间')

    # 项目成员（暂缓）TODD
    # 测试环境（暂缓）TODD

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "测试项目"
        verbose_name_plural = verbose_name
