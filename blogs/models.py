from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title=models.CharField(max_length=200)
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    body=models.TextField()
    likes=models.ManyToManyField(User, related_name='blog_posts',blank=True) 
    
    def total_likes(self):
        return self.likes.count()
   
    def __str__(self):
     return  f"{self.title} | {self.author}"
  
    
    def get_absolute_url(self):
        return reverse('post-detail', args=[str(self.id)])
