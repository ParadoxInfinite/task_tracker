from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import UserProfile
from .forms import RegisterUser
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView

class UserCreation(CreateView):
    '''
    Registration View
    TODO: Understand builtin methods for this class and utilize it to login the user automatically.
    TODO: Eventually add email verification for newly registered users.
    '''
    model = User
    form_class = RegisterUser
    template_name = 'users/register.html'
    success_url = reverse_lazy('tasks:home')


class CustomLoginView(LoginView):
    '''
    Login View
    TODO: TODO
    '''
    template_name = 'users/login.html'

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('users:login')