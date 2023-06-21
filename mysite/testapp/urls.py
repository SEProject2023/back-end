from django.urls import path
from . import views

urlpatterns = [
    path('welcome.html/', views.welcome, name='welcome'),
    path('index.html/', views.index, name='index'),
]
