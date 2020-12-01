from django.urls import path
from .views import UserCreation, CustomLoginView

app_name='users'
urlpatterns = [
    path('register/', UserCreation.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
]
