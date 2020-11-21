from django.shortcuts import render
from .models import Post, Vote
from .serializers import PostSerializer, VoteSerializer
from rest_framework import generics, permissions, mixins
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework import status


class PostListView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,

    ]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostDestroy(generics.RetrieveDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,

    ]

    def delete(self, request, *args, **kwargs):
        post = Post.objects.filter(author=self.request.user, pk=self.kwargs['pk'])
        if post.exists():
            return self.destroy(request, *args, **kwargs)
        else:
            return Response("this post doesnt belong to you", status=status.HTTP_400_BAD_REQUEST)


class VoteListView(generics.CreateAPIView, mixins.DestroyModelMixin):
    serializer_class = VoteSerializer
    permission_classes = [
        permissions.IsAuthenticated,

    ]

    def get_queryset(self):
        user1 = self.request.user
        post = Post.objects.get(pk=self.kwargs['pk'])
        return Vote.objects.filter(user=user1, post=post)

    def perform_create(self, serializer):
        if self.get_queryset().exists():
            raise ValidationError('you voted already')
        else:
            serializer.save(user=self.request.user, post=Post.objects.get(pk=self.kwargs['pk']))

    def delete(self, request, *args, **kwargs):
        if self.get_queryset().exists():
            self.get_queryset().delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            raise ValidationError('you didnt voted for this shit')
