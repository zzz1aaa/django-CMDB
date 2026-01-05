from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View
from django.views.generic import ListView

from user.models import Peofile


# Create your views here.
# class UserListView(View):
#     def get(self, request):
#         data=User.objects.all()
#         return render(request, 'user_list.html',{'data':data})

#listview高级视图类
class UserListView(ListView):
    template_name = 'user_list.html'
    model = User
class TestDataView(View):
    def get(self, request):
        for i in range(3,100):
            user=User()
            profile=Peofile()
            user.username='user{}'.format(i)
            user.password=make_password('123456')
            user.email='{}@163.com'.format(i)
            user.save()
            profile.name_cn='用户{}'.format(i)
            profile.wechat='wechat_user{}'.format(i)
            profile.phone='2222333312{}'.format(i)
            profile.info='用户{}的简介'.format(i)
            profile.profile_pic=user
            profile.save()
        return HttpResponse('测试数据添加成功')