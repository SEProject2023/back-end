from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Answer(models.Model):
    user = models.ForeignKey(User, related_name='answers', on_delete=models.CASCADE)
    question = models.ForeignKey('questions.Question', related_name='answers', on_delete=models.CASCADE)
    content = models.TextField()
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content
