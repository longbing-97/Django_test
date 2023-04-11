from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Project(models.Model):
    """测试项目"""
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
    members = models.ManyToManyField(User, related_name='project_members', through='ProjecMember',
                                     through_fields=('project', 'user'))

    # 测试环境（暂缓）TODD

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "测试项目"
        verbose_name_plural = verbose_name


class ProjecMember(models.Model):
    """
    项目成员（项目和用户之间的关系）
    """
    MEMBER_ROLE = ((1, '测试员'), (2, '测试组长'), (3, '测试经理'), (4, '开发'), (5, '运维'), (6, '项目经理'))
    # 主键
    id = models.AutoField(primary_key=True)
    # 项目
    project = models.ForeignKey(Project, on_delete=models.PROTECT, verbose_name='测试项目')
    # 用户
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name='用户')
    # 加入日期
    join_date = models.DateField(verbose_name='加入日期')
    # 角色
    role = models.IntegerField(choices=MEMBER_ROLE, verbose_name='角色')
    # 状态
    status = models.BooleanField(default=True, verbose_name='状态')
    # 退出日期
    quit_date = models.DateField(null=True, blank=True, verbose_name='退出日期')
    # 备忘录
    memo = models.CharField(max_length=200, verbose_name='备忘录', blank=True, null=True)

    def __str__(self):
        if self.user:
            return '_'
        firstname = self.user.first_name if self.user else '_'
        username = self.user.username
        return f"{firstname}({username})"

    class Meta:
        verbose_name = "项目成员"
        verbose_name_plural = verbose_name


class DeployEnv(models.Model):
    # 主键
    id = models.AutoField(primary_key=True)
    # 项目
    project = models.ForeignKey(Project, on_delete=models.PROTECT, verbose_name='测试项目')
    # 名称
    name = models.CharField(max_length=50, verbose_name='环境名称')
    # 主机名（IP）
    hostname = models.CharField(max_length=50, verbose_name='主机名', help_text='主机名（IP）')
    # 端口
    port = models.IntegerField(verbose_name='端口')
    # 状态
    status = models.BooleanField(default=True, verbose_name='状态')
    memo = models.CharField(max_length=200, verbose_name='备忘录', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '部署环境'
        verbose_name_plural = verbose_name
