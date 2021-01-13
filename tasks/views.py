from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Task

# Create your views here.
class LandingView(TemplateView):
    template_name = "tasks/index.html"

class HomeView(LoginRequiredMixin, ListView):
    login_url = '/login'
    model = Task
    context_object_name = 'tasks'
    template_name = "tasks/home.html"