from django.urls import path
from .views import get_user_details

urlpatterns = [
    path('users/<int:user_id>', get_user_details),
]
