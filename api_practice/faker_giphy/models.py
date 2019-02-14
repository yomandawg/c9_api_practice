from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.TextField()
    content = models.TextField()
    
    def __repr__(self):
        return f"제목: {self.title}, 내용: {self.content}"
    
    def __str__(self): # print로 사용
        return f"제목: {self.title}, 내용: {self.content}"
        

class Job(models.Model):
    name = models.TextField()
    job = models.TextField()