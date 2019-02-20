from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.TextField()
    content = models.TextField()
    
    def __repr__(self):
        return f"<{self.id}, {self.title} : {self.content}>"
        
    def __str__(self): # for print
        return f"<{self.id}, {self.title} : {self.content}>"