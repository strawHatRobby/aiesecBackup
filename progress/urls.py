from django.conf.urls import url, include
from django.contrib import admin
from . import views
from django.contrib.auth.decorators import login_required, permission_required
urlpatterns = [
        url(r'progress_list/$',views.ProgressListView.as_view(), name='list_progress'),
        url(r'create_progress/$',permission_required('progress.can_add_progress')(views.ProgressCreateView.as_view()), name='create_progress'),
        url(r'edit_progress/(?P<pk>\d+)/$',permission_required('progresss.can_change_progress')(views.ProgressUpdateView.as_view()), name='edit_progress'),
        url(r'delete_progress/(?P<pk>\d+)/$',permission_required('progresss.can_delete_review')(views.ProgressDeleteView.as_view()), name='delete_review'),
]
