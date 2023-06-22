from django.urls import path
from .views import QuestionCreateView, QuestionDetailView

urlpatterns = [
    path('', QuestionCreateView.as_view(), name='create_question'),
    path('/<int:pk>', QuestionDetailView.as_view(), name='detail_question'),
]
