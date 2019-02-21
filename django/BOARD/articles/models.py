from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.TextField()
    content = models.TextField()
    
    def __repr__(self):
        return f"<{self.id}, {self.title} : {self.content}>"
        
    def __str__(self): # for print
        return f"<{self.id}, {self.title} : {self.content}>"

class Comment(models.Model):
    content = models.TextField()
    # 속한 글의 ForeignKey, 속한 글이 지워졌을 경우 모든 comment 삭제
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="comments")