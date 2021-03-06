from django.shortcuts import render
from django.views.generic import (CreateView, ListView,
    DetailView, DeleteView, UpdateView)
# Create your views here.
from .models import Notification
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required


class NotificationCreateView(CreateView):
    model = Notification
    fields = ['title','content']
    success_url = reverse_lazy('notification:list_notification')

class NotificationListView(ListView):
    context_object_name = "notifications"
    model = Notification


class NotificationUpdateView(UpdateView):
    model = Notification
    fields = ['title','content']
    success_url = reverse_lazy('accounts:dashboard')


class NotificationDeleteView(DeleteView):
    model = Notification
    success_url = reverse_lazy('accounts:dashboard')
