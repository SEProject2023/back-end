from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Q
from user_auth.models import User
from questions.models import Question
from answers.models import Answer, ChatglmAnswer
# Create your views here.


def search(request):
    search_term = request.GET.get('search_term', '')
    search_results = []

    # 在问题标题和描述中搜索
    q1 = Q(title__icontains=search_term) | Q(description__icontains=search_term)
    questions = Question.objects.filter(q1)

    for question in questions:
        search_results.append({
            'category': 'question',
            'id': question.id,
            'title': question.title,
            'user': question.user.username,
        })

    # 在用户答案内容中搜索
    q2 = Q(content__icontains=search_term)
    answers_user = Answer.objects.filter(q2)

    for answer in answers_user:
        search_results.append({
            'category': 'answer',
            'id': answer.id,
            'content': answer.content,
            'user': answer.user.username,
        })

    # 在大模型答案内容中搜索
    q3 = Q(content__icontains=search_term)
    answers_chatglm = ChatglmAnswer.objects.filter(q2)

    for answer in answers_chatglm:
        search_results.append({
            'category': 'answer_chatglm',
            'id': answer.id,
            'content': answer.content,
        })

    # 在用户名中搜索
    users = User.objects.filter(username__icontains=search_term)
    for user in users:
        search_results.append({
            'category': 'user',
            'id': user.id,
            'username': user.username,
        })

    return JsonResponse({'search_results': search_results} 
                        , json_dumps_params={'ensure_ascii': False})

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
