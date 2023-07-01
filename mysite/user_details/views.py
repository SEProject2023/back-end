from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from questions.models import Question
from answers.models import Answer
from user_auth.models import User

# Create your views here.

def get_user_details(request, user_id):
    if request.method == 'GET':
        user = User.objects.get(id=user_id)
        user_info = {
            'user_id': user.id,
            'username': user.username
        }
        user_questions = serializers.serialize('json', Question.objects.filter(user_id=user.id))
        user_answers = serializers.serialize('json', Answer.objects.filter(user_id=user.id))
        
        return JsonResponse({
            'user_info': user_info,
            'user_questions': user_questions,
            'user_answers': user_answers
        })
