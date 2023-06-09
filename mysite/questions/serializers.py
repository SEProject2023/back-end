from rest_framework import serializers
from .models import Question, User
from answers.models import Answer
from answers.serializers import AnswerSerializer

# class QuestionSerializer(serializers.ModelSerializer):
#     asker = serializers.StringRelatedField(source='user.username')  # 将字段名从user_name改为asker
#     answers = AnswerSerializer(many=True, read_only=True)  # 一对多关系，所以要加上many=True
#     class Meta:
#         model = Question
#         #下面就是api给前端的返回值
#         fields = ['asker', 'title', 'description', 'answers'] 

class QuestionSerializer(serializers.ModelSerializer):
    asker_id = serializers.PrimaryKeyRelatedField(source='user', queryset=User.objects.all())
    answers = AnswerSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ['asker_id', 'title', 'description', 'answers', 'tags']