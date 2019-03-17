from django.db import models

# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=20)

class Choice(models.Model):
    content = models.CharField(max_length=10)
    votes = models.IntegerField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="choices")

    def __str__(self):
        return f'content: {self.content}, votes: {self.votes}'