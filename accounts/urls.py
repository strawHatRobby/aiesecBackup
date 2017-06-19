from django.conf.urls import url
from django.contrib.auth.views import (login,
    logout, logout_then_login)
from . import views

urlpatterns = [
    url(r'^$',views.dashboard,name='dashboard'),
    # url(r"login/$", views.user_login, name="login"),
    url(r"login/$", login, name="login"),
    url(r"logout/$",logout, {'next_page': 'accounts:login'}, name="logout"),
    url(r"logout-then-login/$",logout_then_login, name="logout_then_login"),
]
