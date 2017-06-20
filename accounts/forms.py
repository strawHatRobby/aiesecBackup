from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.conf import settings
from .models import User


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

# # class UserCreateForm(UserCreationForm):
#     class Meta:
#         fields = ("username", "email","display_name","first_name",
#         "last_name","password1", "password2", "department")
#         model = get_user_model()

#     def clean_password2(self):
#         cd = self.cleaned_data
#         if cd['password1'] != cd['password2']:
#             raise forms.ValidationError('Passwords don\'t match.')
#         return cd['password2']

#     def __init__(self, *args, **kwargs):
#         super(UserCreateForm, self).__init__(*args, **kwargs)
#         self.fields["username"].label = "Display name"
#         self.fields["email"].label = "Email address"

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password',
                                widget=forms.PasswordInput)

    class Meta:
        model = get_user_model()
        fields = ("username", "email","display_name","first_name",
        "last_name","password", "password2", "department")
        

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password']
