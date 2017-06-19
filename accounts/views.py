from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from django.views import generic
from django.shortcuts import render, redirect
from django.http import HttpResponse

from . import forms
from .forms import LoginForm, UserRegistrationForm


@login_required
def dashboard(request):
    return render(request,
                'accounts/dashboard.html',
                {'section':'dashboard'})


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
