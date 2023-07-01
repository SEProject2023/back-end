from rest_framework import serializers
from questions.models import Question
from answers.models import Answer

class QuestionListSerializer(serializers.ModelSerializer):
    asker = serializers.StringRelatedField(source='user.username')

    class Meta:
        model = Question
        fields = ['id', 'title', 'asker']

class AnswerListSerializer(serializers.ModelSerializer):
    responder = serializers.StringRelatedField(source='user.username')

    class Meta:
        model = Answer
        fields = ['id', 'content', 'responder']

class ChatglmAnswerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['id', 'content']
