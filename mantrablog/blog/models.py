from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class Post(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=70)
    content = models.TextField()

    # highlight=models.CharField(max_length=250)
    # img=models.ImageField(upload_to='postimg')
    date=models.DateTimeField(auto_now_add=True)



class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='comment_likes', blank=True)



