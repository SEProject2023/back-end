from django.db import models
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.

class Question(models.Model):
    user = models.ForeignKey(User, related_name='questions', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    tags = models.CharField(max_length=200)

    def __str__(self):
        return self.title
