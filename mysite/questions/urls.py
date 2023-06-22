from django.urls import path
from .views import QuestionCreateView, QuestionDetailView

urlpatterns = [
    path('questions', QuestionCreateView.as_view(), name='create_question'),
    path('questions/<int:pk>', QuestionDetailView.as_view(), name='detail_question'),
]
