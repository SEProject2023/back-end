from rest_framework import serializers
from .models import Answer
from .models import User
from questions.models import Question


class AnswerSerializer(serializers.ModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(source='user', queryset=User.objects.all())
    question_id = serializers.PrimaryKeyRelatedField(source='question', queryset=Question.objects.all())
    class Meta:
        model = Answer
        fields = ['user_id', 'question_id', 'content']
