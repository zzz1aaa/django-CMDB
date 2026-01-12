from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User,Group,Permission
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
from django.views.generic import View,TemplateView
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
    paginate_by = 8
    def get_context_data(self, **kwargs):
        context = super(UserListView, self).get_context_data(**kwargs)
        context['page_range'] = self.page_range(context['page_obj'])
        return context
    def page_range(self, page_obj):
        current_index = page_obj.number
        start = current_index - 2
        end = current_index + 3
        #左限制
        if start < 1:
            start = 1
        #右限制
        if end > page_obj.paginator.num_pages:
            end = page_obj.paginator.num_pages
        return range(start,end)
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

class UserAddView(TemplateView):
    template_name = 'user_add.html'
    def post(self, request):
        data=request.POST
        res={'status':0,'msg':'添加成功'}
        try:
            user = User()
            profile = Peofile()
            user.username = data.get('username')
            user.password = make_password(data.get('password'))
            user.email = data.get('email')
            user.save()
            profile.name_cn = data.get('name_cn')
            profile.wechat = data.get('wechat')
            profile.phone = data.get('phone')
            profile.info = data.get('name_cn')
            profile.profile_pic=user
            profile.save()
        except Exception as e:
            print(e)
            res={'status': 1 , 'msg' : '添加失败'}
        return JsonResponse(res)

class UserUpdateView(View):
    def get(self,request):
        return render(request,'user_update.html',{'user_obj':User.objects.get(id=request.GET.get('id'))})
    def post(self, request):
        data=request.POST
        res={'status':0,'msg':'修改成功'}
        try:
            user = User.objects.get(id=data.get('uid'))
            profile = Peofile.objects.get(profile_pic=data.get('uid'))
            user.username = data.get('username')
            user.password = make_password(data.get('password'))
            user.email = data.get('email')
            user.save()
            profile.name_cn = data.get('name_cn')
            profile.wechat = data.get('wechat')
            profile.phone = data.get('phone')
            profile.info = data.get('name_cn')
            profile.profile_pic=user
            profile.save()
        except Exception as e:
            print(e)
            res={'status': 1 , 'msg' : '修改失败'}
        return JsonResponse(res)

class UserDeleteView(View):
    def get(self, request):
        res={'status':0,'msg':'删除成功'}
        try:
            User.objects.get(id=request.GET.get('id')).delete()
        except Exception as e:
            print(e)
            res={'status': 1 , 'msg' : '删除失败'}
        return JsonResponse(res)

class UserStatusView(View):
    def get(self,request):
        res={'status':0,'msg':'修改成功'}
        try:
            #查看当前状态
            print(type(User.objects.get(id=request.GET.get('id'))))
            status=User.objects.get(id=request.GET.get('id')).is_active
            if status:
                User.objects.filter(id=request.GET.get('id')).update(is_active=0)
            else:
                User.objects.filter(id=request.GET.get('id')).update(is_active=1)
        except Exception as e:
            print(e)
            res={'status': 1 , 'msg' : '修改失败'}
        return JsonResponse(res)
class GroupListView(ListView):
    template_name = 'group_list.html'
    model = Group
    paginate_by = 8

class GroupAddView(ListView):
    template_name = 'group_add.html'
    model = User
    def post(self, request):
        data=request.POST
        res={'status':0,'msg':'添加成功'}
        try:
            group = Group()
            group.name = data.get('name')
            group.save()
            for i in data.getlist('group_user'):
                group.user_set.add(User.objects.get(id=i))
        except Exception as e:
            print(e)
            res={'status': 1 , 'msg' : '添加失败'}
        return JsonResponse(res)

class GroupUpdateView(ListView):
    template_name = 'group_update.html'
    model = User
    def get_context_data(self, **kwargs):
        context = super(GroupUpdateView, self).get_context_data(**kwargs)
        context['group_obj'] = Group.objects.get(id=self.request.GET.get('id'))
        return context
    def post(self, request):
        data=request.POST
        res={'status':0,'msg':'修改成功'}
        try:
            group = Group.objects.get(id=data.get('gid'))
            group.name = data.get('name')
            group.save()
            group.user_set.clear()
            for i in data.getlist('group_user'):
                group.user_set.add(User.objects.get(id=i))
        except Exception as e:
            print(e)
            res={'status': 1 , 'msg' : '修改失败'}
        return JsonResponse(res)

class PermListView(ListView):
    template_name = 'perm_list.html'
    model = Permission
    paginate_by = 8
    def get_queryset(self):
        queryset = super(PermListView, self).get_queryset()
        queryset = queryset.exclude(name__regex='[a-zA-Z]')
        return queryset

class PermUserSetView(ListView):
    template_name = 'user_set_perm.html'
    model = Permission
    paginate_by = 8
    def get_context_data(self, **kwargs):
        context = super(PermUserSetView, self).get_context_data(**kwargs)
        context['user_obj'] = User.objects.get(id=self.request.GET.get('id'))
        return context
    def get_queryset(self):
        queryset = super(PermUserSetView, self).get_queryset()
        queryset = queryset.exclude(name__regex='[a-zA-Z]')
        return queryset
    def post(self, request):
        data=request.POST
        print(data)
        res={'status':0,'msg':'修改成功'}
        try:
            user = User.objects.get(id=data.get('uid'))
            user.user_permissions.clear()
            for i in data.getlist('perm_list[]'):
                user.user_permissions.add(Permission.objects.get(id=i))
            #下面这种方法现在不能使用，因为你试图直接赋值给用户的 user_permissions 这个多对多字段（比如 user.user_permissions =
            # [perm1, perm2]），而 Django 明确禁止这种操作，要求使用 set() 方法来修改多对多关系。
            # print(data.get('uid'))
            # print(data.getlist('perm_list[]'))
            # user = User.objects.get(id=data.get('uid'))
            # user.user_permissions = data.getlist('perm_list[]')
            # user.save()
        except Exception as e:
            print(e)
            res={'status': 1 , 'msg' : '修改失败'}
        return JsonResponse(res)
