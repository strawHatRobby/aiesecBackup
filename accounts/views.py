from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from django.views import generic
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from .models import User
from review.models import Review
from progress.models import Progress
from . import forms
from .forms import LoginForm, UserRegistrationForm

from django.views.decorators.csrf import csrf_protect

@login_required
def dashboard(request):
    return render(request,
                'accounts/dashboard.html',
                {'section':'dashboard'})

@csrf_protect
def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(
                user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return render(request,
                          'accounts/register_done.html',
                          {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request,
                  'accounts/register.html',
                  {'user_form': user_form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            clean_data = form.cleaned_data
            user = authenticate(username=clean_data['username'],
                                    password=clean_data['password'])
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return HttpResponse('Authenticated')
                else:
                    return HttpResponse('Disabled')
            else:
                return HttpResponse('Invalid Login')
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form':form})

class LoginView(generic.FormView):
    form_class = AuthenticationForm
    success_url = reverse_lazy("document:upload")
    template_name = "accounts/dashboard.html"

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()
        return form_class(self.request, **self.get_form_kwargs())

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super().form_valid(form)


class LogoutView(generic.RedirectView):
    url = reverse_lazy("home")

    def get(self, request, *args, **kwargs):
        logout(request)
        return super().get(request, *args, **kwargs)


# class SignUp(generic.CreateView):
#     form_class = forms.UserCreateForm
#     success_url = reverse_lazy("login")
#     template_name = "accounts/signup.html"
#
#

@login_required
def user_list(request):
    users = User.objects.filter(is_active=True)
    return render(request, 'accounts/user/list.html',
                            {'section':'people', 'users': users})

@login_required
def user_detail(request,pk):
    profile_user = get_object_or_404(User, pk=pk, is_active=True)
    reviews = Review.objects.filter(review_of=profile_user)
    progress_list = Progress.objects.filter(user=profile_user)
    return render(request, 'accounts/user/detail.html',
                            {'section':'people',
                            'pk':pk,
                            'profile_user':profile_user,
                            'reviews':reviews,
                            'progress_list':progress_list})
