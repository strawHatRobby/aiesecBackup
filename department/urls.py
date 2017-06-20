from django.conf.urls import url, include
from django.contrib import admin
from . import views
urlpatterns = [
            url(r'department_list/$',views.department_list, name='list_department'),
            url(r'detail/(?P<pk>\d+)/$',views.department_detail,name='department_detail'),
]
