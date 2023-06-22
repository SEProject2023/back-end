from django.shortcuts import render
from .models import Answer
from .serializers import AnswerSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import  Http404

# Create your views here.

class AnswerCreateView(APIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            answer = serializer.save()
            return Response({'answer_id': answer.id, 'status': 'Answer created successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AnswerDetailView(APIView):
    def get_object(self, pk):
        try:
            return Answer.objects.get(pk=pk)
        except Answer.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        answer = self.get_object(pk)
        serializer = AnswerSerializer(answer)
        return Response(serializer.data)
