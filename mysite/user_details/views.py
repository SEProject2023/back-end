from django.http import JsonResponse
from django.core import serializers
from user_auth.models import User  
from questions.models import Question 
from answers.models import Answer   

# Create your views here.

def get_user_details(request, user_id):
    if request.method == 'GET':
        user = User.objects.get(id=user_id)
        user_info = {
            'user_id': user.id,
            'username': user.username
        }
        user_questions = list(Question.objects.filter(user_id=user.id).values('id', 'title'))
        user_answers = list(Answer.objects.filter(user_id=user.id).values('id', 'content'))
        
        return JsonResponse({
            'user_info': user_info,
            'user_questions': user_questions,
            'user_answers': user_answers
        }, json_dumps_params={'ensure_ascii': False}
        )