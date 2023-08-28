from django.shortcuts import render
from django.views.generic import CreateView
from account.forms import TodoUserCreationForm,UserAuthenticationForm
from django.contrib.auth.views import LoginView
# Create your views here.


class UserCreateView(CreateView):
    form_class = TodoUserCreationForm
    template_name = "account/sign-up.html"
    success_url = "/"

class UserLoginView(LoginView):
    template_name = "account/login.html"
    authentication_form = UserAuthenticationForm
    
