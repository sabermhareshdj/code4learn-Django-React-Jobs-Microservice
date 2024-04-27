from django.urls import path
from . import views


urlpatterns = [
    path('', views.PostListAPI.as_view()),
    path('<int:pk>', views.PostDetailAPI.as_view()),
    path('add-like' , views.LikeCreateAPI.as_view()),
    path('add-comment' , views.CommentCreateAPI.as_view()),
    path('coments/<int:pk>' , views.CommentUpdateAPI.as_view()),
]
