from django.db import models
from django.utils import timezone


class Post(models.Model):
  author_id = models.IntegerField()
  title = models.CharField(max_length=100)
  content = models.TextField(max_length=5000)
  publish_date = models.DateTimeField(default=timezone.now)

  # likes , favourties make fields ManyToMany
  #likes = models.ManyToManyField(User) ==> لااستطيع عمل جدول كون اليوزر في مكان اخر 

  def total_likes(self):
    return PostLikes.objects.filter(post=self).count()

  def total_comments(self):
    return Comment.objects.filter(post=self).count()
  

  def __str__(self):
    return self.title


class PostLikes(models.Model):
  post = models.ForeignKey(Post,related_name='post_likes',on_delete=models.CASCADE)
  user_id = models.IntegerField()

  def __str__(self):
    return str(self.post)
  

class Comment(models.Model):
  user_id = models.IntegerField()
  post = models.ForeignKey(Post,related_name='post_comment',on_delete=models.CASCADE)
  content = models.TextField(max_length=500)
  publish_date = models.DateTimeField(default=timezone.now)

  def __str__(self):
    return str(self.post)