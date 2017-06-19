from django.shortcuts import render
from django.views.generic import (CreateView, ListView,
    DetailView, DeleteView, UpdateView)
# Create your views here.
from .models import Review
from django.core.urlresolvers import reverse_lazy

class ReviewCreateView(CreateView):
    model = Review
    fields = ['title','content']
    success_url = reverse_lazy('accounts:dashboard')

class ReviewListView(ListView):
    context_object_name = "reviews"
    model = Review

class ReviewUpdateView(UpdateView):
    model = Review
    fields = ['title','content']
    success_url = reverse_lazy('accounts:dashboard')

class ReviewDeleteView(DeleteView):
    model = Review
    success_url = reverse_lazy('accounts:dashboard')
