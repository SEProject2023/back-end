from rest_framework import serializers
from .models import Question
from .models import User

class QuestionSerializer(serializers.ModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(source='user', queryset=User.objects.all())
    user_name = serializers.StringRelatedField(source='user.username')
    class Meta:
        model = Question
        #下面就是api给前端的返回值
        fields = ['user_id', 'user_name', 'title', 'description', 'tags']  # 
