from rest_framework import serializers
from .models import Answer, ChatglmAnswer
from .models import User
from questions.models import Question


class AnswerCreateSerializer(serializers.ModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(source='user', queryset=User.objects.all())
    question_id = serializers.PrimaryKeyRelatedField(source='question', queryset=Question.objects.all())
    class Meta:
        model = Answer
        fields = ['user_id', 'question_id', 'content']


class AnswerSerializer(serializers.ModelSerializer):
    responder = serializers.StringRelatedField(source='user.username') 
    class Meta:
        model = Answer
        fields = ['content', 'responder', 'time'] # 'user_id', 'question_id', 


class ChatglmAnswerSerializer(serializers.ModelSerializer):
    response = serializers.CharField(source='content')
    status = serializers.SerializerMethodField()
    class Meta:
        model = ChatglmAnswer
        fields = ['response', 'status', 'time']

    def get_status(self, obj):
        return 200  # 这里假设大模型服务器的状态码总是200