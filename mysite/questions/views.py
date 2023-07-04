from django.shortcuts import render
import requests
from .models import Question
from answers.models import ChatglmAnswer
from answers.serializers import ChatglmAnswerSerializer
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


class GetChatglmAnswerView(APIView):
    def post(self, request, question_id, format=None):
        # 获取问题
        try:
            question = Question.objects.get(id=question_id)
        except Question.DoesNotExist:
            return Response({'error': 'Question not found.'}, status=status.HTTP_404_NOT_FOUND)

        # 将问题转换为查询语句
        prompt = question.title + ":\n" + question.description + "\n" 
        query = {"prompt": prompt, "history": []}

        # 向大模型服务器发送查询请求
        response = requests.post("http://222.200.185.183:23623", json=query)

        # 检查大模型服务器的回答
        if response.status_code == 200:
            data = response.json()
            answer = data.get('response')

            # 将大模型的回答保存在数据库中
            big_model_answer =ChatglmAnswer(question=question, content=answer)
            big_model_answer.save()

            # 创建序列化器
            serializer = ChatglmAnswerSerializer(big_model_answer, context={'status': response.status_code})

            # 返回大模型的回答给前端
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Error from Big Model Server.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)