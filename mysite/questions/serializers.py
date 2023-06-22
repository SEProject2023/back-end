from rest_framework import serializers
from .models import Question
from .models import User

class QuestionSerializer(serializers.ModelSerializer):
    asker = serializers.StringRelatedField(source='user.username')  # 将字段名从user_name改为asker
    class Meta:
        model = Question
        #下面就是api给前端的返回值
        fields = ['asker', 'title', 'description']  # 从fields中移除'user_id'和'tags'