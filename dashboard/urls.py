from operator import index

from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('index', views.IndexView.as_view(),name='index'),
    path('user/',include('user.urls')),
]