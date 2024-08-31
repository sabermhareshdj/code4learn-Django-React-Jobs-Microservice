from rest_framework import generics , status
from rest_framework.response import Response
from .models import Post , PostLikes , Comment
from .serializers import PostLikesSerializers , PostSerializers , CommentSerializers
from .pagination import PostPagination

class PostListAPI(generics.ListAPIView):
  queryset = Post.objects.all()
  serializer_class = PostSerializers
  pagination_class = PostPagination

class PostDetailAPI(generics.RetrieveAPIView):
  queryset = Post.objects.all()
  serializer_class = PostSerializers


class CommentCreateAPI(generics.CreateAPIView):
  serializer_class = CommentSerializers

  def perform_create(self, serializer):
    post_id = self.request.data.get('post_id')
    user_id = self.request.data.get('user_id')
    try:
      post = Post.objects.get(id=post_id)
      serializer.save(post=post,user_id=user_id)
      return Response({'message':'comment was created successuly'},status=status.HTTP_201_CREATED)
    except Exception as e :
      return Response({f'message':{e}} , status=status.HTTP_400_BAD_REQUEST)


class LikeCreateAPI(generics.CreateAPIView):
  serializer_class = PostLikesSerializers
  def perform_create(self, serializer):
    post_id = self.request.data.get('post_id')
    user_id = self.request.data.get('user_id')

    try:
      post = PostLikes.objects.get(id=post_id)
      serializer.save(post=post,user_id=user_id)
      return Response({'message':'like  was added successuly'},status=status.HTTP_201_CREATED)
    
    except Exception as e :
      return Response({f'message':{e}} , status=status.HTTP_400_BAD_REQUEST)
    
class CommentUpdateAPI(generics.UpdateAPIView):
    serializer_class = CommentSerializers
    queryset = Comment.objects.all()



    