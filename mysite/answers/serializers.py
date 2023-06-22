from rest_framework import serializers
from .models import Answer
from .models import User


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['user_id', 'question_id', 'content']
