from django.shortcuts import render
from django.views.generic import (CreateView, ListView,
    DetailView, DeleteView, UpdateView)
# Create your views here.
from .models import Progress

class ProgressCreateView(CreateView):
    model = Progress
    success_url = reverse_lazy('accounts:profile')

class ProgressListView(ListView):
    context_object_name = "progresss"
    model = models.Progress

class ProgressUpdateView(UpdateView):
    model = Progress
    success_url = reverse_lazy('accounts:profile')

class ProgressDeleteView(DeleteView):
    model = Progress
    success_url = reverse_lazy('accounts:profile')
