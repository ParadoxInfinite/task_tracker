from django.urls import path
from .views import LandingView, HomeView

app_name='tasks'
urlpatterns = [
    path('', LandingView.as_view(), name="landing"),
    path('home/', HomeView.as_view(), name="home"),
]
