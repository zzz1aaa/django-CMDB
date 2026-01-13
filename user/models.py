from django.db import models
from django.contrib.auth.models import User,Group
# Create your models here.

class Peofile(models.Model):
    name_cn=models.CharField(max_length=20)
    wechat=models.CharField(max_length=20)
    phone=models.CharField(max_length=20)
    info=models.TextField(verbose_name='个人简介')
    profile_pic=models.OneToOneField(User,on_delete=models.CASCADE)
    class Meta:
        default_permissions=[]
        permissions=(
            ('add_user','添加用户'),
            ('update_user','修改用户'),
            ('delete_user','删除用户'),
            ('show_user','查看用户'),
        )
class NewGroup(Group):
    class Meta:
        default_permissions=[]
        permissions=(
            ('add_group','添加用户组'),
            ('update_group','修改用户组'),
            ('delete_group','删除用户组'),
            ('show_group','查看用户组'),
        )