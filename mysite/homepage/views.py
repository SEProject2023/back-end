from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from questions.models import Question
from answers.models import Answer, ChatglmAnswer
from .serializers import QuestionListSerializer, AnswerListSerializer, ChatglmAnswerListSerializer

# Create your views here.

class HomeView(APIView):
    def get(self, request, format=None):
        # 获取最近的10个问题
        recent_questions = Question.objects.order_by('-time')[:10]
        # 获取最近的10个用户答案
        recent_user_answers = Answer.objects.order_by('-time')[:10]
        # 获取最近的10个大模型答案
        recent_chatglm_answers = ChatglmAnswer.objects.order_by('-time')[:10]

        # 使用刚刚定义的序列化器来格式化输出
        questions_serializer = QuestionListSerializer(recent_questions, many=True)
        answers_serializer = AnswerListSerializer(recent_user_answers, many=True)
        chatglm_answers_serializer = ChatglmAnswerListSerializer(recent_chatglm_answers, many=True)

        return Response({
            'questions': questions_serializer.data,
            'answers': answers_serializer.data,
            'chatglm_answers': chatglm_answers_serializer.data,
        })
