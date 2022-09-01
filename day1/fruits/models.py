from pyexpat import model
from django.db import models

# Create your models here.
# Article = 테이블 명

class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f'{self.title} {self.content}'