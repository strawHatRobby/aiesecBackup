from django.conf.urls import url, include
from django.contrib import admin
from . import views
from django.contrib.auth.decorators import login_required, permission_required
urlpatterns = [
        url(r'^review_list/$',views.ReviewListView.as_view(), name='list_review'),
        url(r'^create_review/$',permission_required('review.can_add_review')(views.ReviewCreateView.as_view()), name='create_review'),
        url(r'^edit_review/(?P<pk>\d+)/$',permission_required('reviews.can_change_review')(views.ReviewUpdateView.as_view()), name='edit_review'),
        url(r'^delete_review/(?P<pk>\d+)/$',permission_required('reviews.can_delete_review')(views.ReviewDeleteView.as_view()), name='delete_review'),
]
