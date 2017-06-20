from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
        url(r'^$',views.home,name='home'),
        url(r'awdocuments$',views.awdocuments,name='awdocuments'),
        url(r'contacts$',views.contacts,name='contacts'),
        url(r'guidesigt$',views.guidesigt,name='guidesigt'),
        url(r'guidesigv$',views.guidesigv,name='guidesigv'),
        url(r'igt$',views.igt,name='igt'),
        url(r'igv$',views.igt,name='igv'),
        url(r'ldmresources$',views.ldmresources,name='ldmresources'),
        url(r'notices$',views.notices,name='notices'), #convert to notifications later
        url(r'opportunities$',views.opportunities,name='opportunities'),
        url(r'projects$',views.projects,name='projects'),
        url(r'visa_for_externals$',views.visa_for_externals,name='visa_for_externals'),

]
