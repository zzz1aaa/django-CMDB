from django.db import models
from django.db.models import IntegerField


# Create your models here.
class Idc(models.Model):
    name = models.CharField(max_length=10, verbose_name='机房简称')
    name_cn = models.CharField(max_length=32, verbose_name='机房名称')
    address = models.CharField(max_length=64, verbose_name='机房地址')
    phone = models.CharField(max_length=11, verbose_name='机房座机电话')
    username = models.CharField(max_length=32, verbose_name='机房负责人姓名')
    username_email = models.EmailField(verbose_name='机房负责人邮箱')
    username_phone = models.CharField(max_length=11, verbose_name='机房负责人手机号')
    class Meta:
        default_permissions = []
        permissions = (
        ('add_idc', '添加IDC'),
        ('show_idc', '查看IDC'),
        ('delete_idc', '删除IDC'),
        ('update_idc', '更新IDC'),
        )
class serverUser(models.Model):
    name=models.CharField(max_length=32, verbose_name='名称')
    username = models.CharField(max_length=32, verbose_name='系统用户名')
    password = models.CharField(max_length=128, verbose_name='用户密码')
    info = models.CharField(max_length=64, verbose_name='备注')
    class Meta:
        default_permissions = []
        permissions = (
        ('add_serverUser', '添加服务器用户'),
        ('show_serverUser', '查看服务器用户'),
        ('delete_serverUser', '删除服务器用户'),
        ('update_serverUser', '更新服务器用户'),
        )

class Server(models.Model):
    hostname = models.CharField(max_length=32,verbose_name='主机名')
    cpu_info = models.CharField(max_length=100,verbose_name='CPU信息')
    cpu_count = models.IntegerField(verbose_name='CPU个数')
    mem_info = models.CharField(max_length=32,verbose_name='内存信息')
    os_system = models.CharField(max_length=32,verbose_name='操作系统')
    os_system_num = IntegerField(verbose_name='操作系统位数')
    uuid = models.CharField(max_length=64,verbose_name='uuid')
    sn = models.CharField(max_length=64,verbose_name='设备SN')
    scan_status_list=[
        (0,'连接异常'),
        (1,'连接正常')
    ]
    scan_status = models.IntegerField(choices=scan_status_list,verbose_name='状态')
    create_date = models.DateTimeField(auto_now_add=True,verbose_name='创建主机时间')
    update_date = models.DateTimeField(auto_now=True,verbose_name='更新主机时间')

class Disk(models.Model):
    name = models.CharField(max_length=32,verbose_name='硬盘名称')
    size = models.CharField(max_length=32,verbose_name='硬盘大小')
    server = models.ForeignKey('Server',on_delete=models.CASCADE)

class NetWork(models.Model):
    name = models.CharField(max_length=32,verbose_name='网卡名称')
    ip_address = models.CharField(max_length=32,verbose_name='网卡地址')
    server = models.ForeignKey('Server',on_delete=models.CASCADE)