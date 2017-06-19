from django.shortcuts import render
from django.views.generic import (CreateView, ListView,
    DetailView, DeleteView, UpdateView)
# Create your views here.
from .models import Progress
from django.core.urlresolvers import reverse_lazy
#
# class ProgressForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['quality1', 'quality2', 'quality3', 'quality4', 'quality5',
#         'quality6', 'quality7', 'quality8', ]
#         widgets = {
#             'quality1': forms.
#         }

class ProgressCreateView(CreateView):
    model = Progress
    success_url = reverse_lazy('accounts:profile')
    fields = ['quality1', 'quality2', 'quality3','quality4','quality5',
    'quality6',
    'quality7', 'quality8']

class ProgressListView(ListView):
    context_object_name = "progresss"
    model = Progress

class ProgressUpdateView(UpdateView):
    model = Progress
    success_url = reverse_lazy('accounts:profile')

class ProgressDeleteView(DeleteView):
    model = Progress
    success_url = reverse_lazy('accounts:profile')
