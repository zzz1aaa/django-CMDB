from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.models import User
# Create your views here.
class UserListView(View):
    def get(self, request):
        data=User.objects.all()
        return render(request, 'user_list.html',{'data':data})