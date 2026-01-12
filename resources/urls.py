from operator import index
from django.urls import path
from .views import *
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('list/',ResListView.as_view(),name='idc_list'),
    path('add/',ResAddView.as_view(),name='idc_add'),
    path('update/',ResUpdateView.as_view(),name='idc_update'),
    path('delete/',ResDeleteView.as_view(),name='idc_delete'),

]