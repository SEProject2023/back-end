from django.urls import path
from .views import AnswerCreateView, AnswerDetailView

urlpatterns = [
    path('answers', AnswerCreateView.as_view(), name='create_answer'),
    path('answers/<int:pk>', AnswerDetailView.as_view(), name='detail_answer'),
]
