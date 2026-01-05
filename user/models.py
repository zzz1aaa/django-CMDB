from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Peofile(models.Model):
    name_cn=models.CharField(max_length=20)
    wechat=models.CharField(max_length=20)
    phone=models.CharField(max_length=20)
    info=models.TextField(verbose_name='个人简介')
    profile_pic=models.OneToOneField(User,on_delete=models.CASCADE)