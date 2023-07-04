from django.urls import path
from .views import QuestionCreateView, QuestionDetailView, GetChatglmAnswerView

urlpatterns = [
    path('questions', QuestionCreateView.as_view(), name='create_question'),
    path('questions/<int:pk>', QuestionDetailView.as_view(), name='detail_question'),
    path('questions/<int:question_id>/get_chatglm_answer', GetChatglmAnswerView.as_view(), name='get_chatglm_answer'),
]
