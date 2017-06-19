from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
            url(r'^$', views.upload, name='upload'),
            url(r'^simple/$', views.simple_upload, name='simple_upload'),
            url(r'^form/$', views.model_form_upload, name='model_form_upload'),
]
