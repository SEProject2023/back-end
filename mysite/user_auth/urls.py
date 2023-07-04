from django.urls import path
from .views import RegisterView, LoginView, LogoutView

urlpatterns = [
    path('users/register', RegisterView.as_view(), name='register'),
    path('users/login', LoginView.as_view(), name='login'),
    path('users/logout', LogoutView.as_view(), name='logout'),
]
