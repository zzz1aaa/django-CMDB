from django.shortcuts import render
from django.http import JsonResponse
from resources.models import *
from django.views.generic import View,TemplateView,ListView
from django.contrib.auth.hashers import make_password
import json

# Create your views here.
class ResListView(ListView):
    template_name = 'idc_list.html'
    model = Idc

class ResAddView(TemplateView):
    template_name = 'idc_add.html'
    model = Idc
    def post(self, request):
        data=request.POST
        print(data)
        res={'status':0,'msg':'添加成功'}
        try:
            idc = Idc()
            idc.name = data.get('name')
            idc.name_cn = data.get('name_cn')
            idc.address = data.get('address')
            idc.phone = data.get('phone')
            idc.username=data.get('username')
            idc.username_email=data.get('username_email')
            idc.username_phone=data.get('username_phone')
            idc.save()
        except Exception as e:
            print(e)
            res={'status': 1 , 'msg' : '添加失败'}
        return JsonResponse(res)

class ResUpdateView(View):
    def get(self,request):
        id=request.GET.get('id')
        data=Idc.objects.get(id=id)
        print(data)
        return render(request,'idc_update.html',{'idc_obj':data})
    def post(self,request):
        data=request.POST
        res={'status':0,'msg':'修改成功'}
        try:
            idc = Idc.objects.get(id=data.get('id'))
            idc.name = data.get('name')
            idc.name_cn = data.get('name_cn')
            idc.address = data.get('address')
            idc.phone = data.get('phone')
            idc.username = data.get('username')
            idc.username_email = data.get('username_email')
            idc.username_phone = data.get('username_phone')
            idc.save()
        except Exception as e:
            print(e)
            res = {'status': 1, 'msg': '添加失败'}
        return JsonResponse(res)

class ResDeleteView(View):
    def post(self,request):
        res={'status':0,'msg':'删除成功'}
        try:
            print(request.POST.get('id'))
            Idc.objects.get(id=request.POST.get('id')).delete()
        except Exception as e:
            print(e)
            res={'status': 1 , 'msg' : '删除失败'}
        return JsonResponse(res)
class ServerUserListView(ListView):
    template_name = 'serverUser_list.html'
    model = serverUser

class ServerUserAddView(TemplateView):
    template_name = 'serverUser_add.html'
    model = serverUser
    def post(self, request):
        data=request.POST
        print(data)
        res={'status':0 ,'msg':'添加成功'}
        try:
            serveruser=serverUser()
            serveruser.name=data.get('name')
            serveruser.username=data.get('username')
            serveruser.password=make_password(data.get('password'))
            serveruser.info=data.get('info')
            serveruser.save()
        except Exception as e:
            print(e)
            res = {'status': 1, 'msg': '添加失败'}
        return JsonResponse(res)


class ServerUserDeleteView(View):
    def post(self,request):
        res={'status':0,'msg':'删除成功'}
        try:
            serverUser.objects.get(id=request.POST.get('id')).delete()
        except Exception as e:
            print(e)
            res={'status':1,'msg':'删除失败'}
        return JsonResponse(res)


class ServerUserUpdateView(View):
    def get(self,request):
        id=request.GET.get('id')
        data=serverUser.objects.get(id=id)
        print(data)
        return render(request,'serveruser_update.html',{'serveruser_obj':data})
    def post(self,request):
        data=request.POST
        res={'status':0,'msg':'修改成功'}
        try:
             serveruser=serverUser.objects.get(id=request.POST.get('id'))
             serveruser.name = data.get('name')
             serveruser.username = data.get('username')
             serveruser.password = make_password(data.get('password'))
             serveruser.info = data.get('info')
             serveruser.save()
        except Exception as e:
            print(e)
            res={'status':1,'msg':'修改失败'}
        return JsonResponse(res)

class ServerListView(ListView):
    template_name = 'server_list.html'
    model = Server
class ServerApiView(View):
    def post(self,request):
        data=request.body
        print(data)
        data=json.loads(data.decode())
        res={'status':0,'msg':'OK'}
        # b'{"hostname": "server2", "cpu_info": "11th Gen Intel(R) Core(TM) i5-11260H @ 2.60GHz", "cpu_count": 2,
        # "mem_info": "0.95", "disk_info": {"sda": "20G"}, "ip_info": {"lo": "127.0.0.1", "ens33": "192.168.200.163",
        # "virbr0": "192.168.122.1", "virbr0-nic": "52:54:00:d1:ab:4a"}, "os_system": "CentOS Linux 7",
        # "os_system_num": "64", "uuid": "c0f14d56-16fa-ac01-11ad-d9e142af4350",
        # "sn": "VMware-56 4d f1 c0 fa 16 01 ac-11 ad d9 e1 42 af 43 50"}'
        # print(data.get('cpu_info'))
        # print(Server.objects.filter(uuid=data.get('uuid')))
        try:
            #判断是否已存在
            server = Server.objects.filter(uuid=data.get('uuid')).exists()
            if not server:
                server=Server()
                server.network_set.all().delete()
                server.disk_set.all().delete()
                server.hostname=data.get('hostname')
                server.cpu_info=data.get('cpu_info')
                server.cpu_count=data.get('cpu_count')
                server.mem_info=data.get('mem_info')
                server.os_system=data.get('os_system')
                server.os_system_num=data.get('os_system_num')
                server.uuid=data.get('uuid')
                server.sn=data.get('sn')
                server.scan_status=1
                server.save()
            else:
                server=Server.objects.get(uuid=data.get('uuid'))
                server.network_set.all().delete()
                server.disk_set.all().delete()
                server.hostname = data.get('hostname')
                server.cpu_info = data.get('cpu_info')
                server.cpu_count = data.get('cpu_count')
                server.mem_info = data.get('mem_info')
                server.os_system = data.get('os_system')
                server.os_system_num = data.get('os_system_num')
                server.uuid = data.get('uuid')
                server.sn = data.get('sn')
                server.scan_status = 1
                server.save()
            for k,v in data.get('ip_info').items():
                NetWork.objects.create(server=server,name=k,ip_address=v)
            for k,v in data.get('disk_info').items():
                Disk.objects.create(server=server,name=k,size=v)
        except Exception as e:
            print(e)
            res={'status':1,'msg':'error'}
        return JsonResponse(res)
class ServerDeleteView(View):
    def post(self,request):
        server=Server()
        res={'status':0,'msg':'删除成功'}
        try:
            server.objects.get(id=request.POST.get('id')).delete()
        except Exception as e:
            print(e)
            res={'status':1,'msg':'删除失败'}


