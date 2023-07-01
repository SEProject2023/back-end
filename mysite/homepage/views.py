from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from questions.models import Question
from answers.models import Answer
from .serializers import QuestionListSerializer, AnswerListSerializer

# Create your views here.

class HomeView(APIView):
    def get(self, request, format=None):
        # 获取最近的10个问题
        recent_questions = Question.objects.order_by('-created_at')[:10]
        # 获取最近的10个答案
        recent_answers = Answer.objects.order_by('-created_at')[:10]
        # 使用刚刚定义的序列化器来格式化输出
        questions_serializer = QuestionListSerializer(recent_questions, many=True)
        answers_serializer = AnswerListSerializer(recent_answers, many=True)
        return Response({
            'questions': questions_serializer.data,
            'answers': answers_serializer.data
        })
