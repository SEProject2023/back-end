from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Q
from user_auth.models import User
from questions.models import Question
from answers.models import Answer
# Create your views here.


def search(request):
    search_term = request.GET.get('search_term', '')

    question_results = Question.objects.filter(Q(title__icontains=search_term) | Q(content__icontains=search_term)).values('id', 'title', 'user__username')
    answer_results = Answer.objects.filter(content__icontains=search_term).values('id', 'content', 'user__username')
    user_results = User.objects.filter(username__icontains=search_term).values('id', 'username')

    results = [
        *format_results(question_results, 'Question'),
        *format_results(answer_results, 'Answer'),
        *format_results(user_results, 'User'),
    ]

    return JsonResponse({'search_results': results}, json_dumps_params={'ensure_ascii': False})

def format_results(queryset, category):
    return [
        {
            'category': category,
            'id': item['id'],
            'title/content': item.get('title', '') or item.get('content', ''),
            'user': item.get('user__username', '') or item['username'],
        }
        for item in queryset
    ]
