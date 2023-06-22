from rest_framework import serializers
from .models import Question
from .models import User

class QuestionSerializer(serializers.ModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(source='user', queryset=User.objects.all())

    class Meta:
        model = Question
        fields = ['user_id', 'title', 'description', 'tags']
