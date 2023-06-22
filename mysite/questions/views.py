from django.shortcuts import render
from .models import Question
from .serializers import QuestionSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse, HttpResponseNotFound, Http404
# Create your views here.


class QuestionCreateView(APIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            question = serializer.save()  # `save` 方法返回模型实例
            return Response({
                'question_id': question.id,  # 获取问题ID
                'status': 'Question created successfully'  # 自定义状态信息
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class QuestionDetailView(APIView):
    def get_object(self, pk):
        try:
            return Question.objects.get(pk=pk)
        except Question.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        question = self.get_object(pk)
        serializer = QuestionSerializer(question)
        return Response(serializer.data)
