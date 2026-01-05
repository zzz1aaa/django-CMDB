from operator import index
from user.views import *
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('list/',UserListView.as_view(),name='user'),
    path('testdata/',TestDataView.as_view(),name='testdata')
]