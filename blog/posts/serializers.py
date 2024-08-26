from rest_framework import serializers
from .models import Post , PostLikes , Comment


class CommentSerializers(serializers.ModelSerializer):
  class Meta:
    model = Comment
    fields = ['id','user_id','post_id','content','publish_date']

class PostSerializers(serializers.ModelSerializer):
  comments = CommentSerializers(many=True,read_only=True)
  likes_count = serializers.SerializerMethodField()
  total_comments = serializers.SerializerMethodField()

  def get_likes_count(self,obj):
      return PostLikes.objects.filter(post=obj).count()
    #Vreturn obj.likes.count()
    
  def get_total_comments(self,obj):
      return Comment.objects.filter(post=obj).count()
  
  class Meta:
    model = Post
    fields = ['id','author_id','content','publish_date','likes_count','total_comments','comments']

    



class PostLikesSerializers(serializers.ModelSerializer):
  class Meta:
    model = PostLikes
    fields = ['id','post','user_id']

