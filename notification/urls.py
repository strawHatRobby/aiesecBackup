from django.conf.urls import url, include
from django.contrib import admin
from . import views
from django.contrib.auth.decorators import login_required, permission_required
urlpatterns = [
        url(r'^notification_list/$',views.NotificationListView.as_view(), name='list_notification'),
        url(r'^create_notification/$',permission_required('notification.can_add_notification')(views.NotificationCreateView.as_view()), name='create_notification'),
        url(r'^edit_notification/(?P<pk>\d+)/$',permission_required('notifications.can_change_notification')(views.NotificationUpdateView.as_view()), name='edit_notification'),
        url(r'^delete_notification/(?P<pk>\d+)/$',permission_required('notifications.can_delete_review')(views.NotificationDeleteView.as_view()), name='delete_review'),
]
