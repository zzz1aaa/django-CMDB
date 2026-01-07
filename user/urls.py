from operator import index
from user.views import *
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('list/',UserListView.as_view(),name='user_list'),
    path('add/',UserAddView.as_view(),name='user_add'),
    path('testdata/',TestDataView.as_view(),name='testdata'),
    path('update/',UserUpdateView.as_view(),name='user_update'),
    path('delete/',UserDeleteView.as_view(),name='user_delete'),
    path('status/',UserStatusView.as_view(),name='user_status'),
]