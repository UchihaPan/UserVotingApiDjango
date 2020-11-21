from rest_framework import serializers
from .models import Post, Vote


class PostSerializer(serializers.ModelSerializer):
    # added ReadOnlyField for author and author_id so that a user cant change his identity
    author = serializers.ReadOnlyField(source='author.username')
    author_id = serializers.ReadOnlyField(source='author.id')
    # This is a read-only field. It gets its value by calling a method on the serializer class  'Meta' it is attached to.
    # It can be used to add any sort of data to the serialized representation of your object. Hence add Vote model to get total counts of votes on particular posts.
    votes = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'title', 'url', 'author', 'author_id', 'description', 'votes', 'created_at']

    def get_votes(self, p):
        return Vote.objects.filter(post=p).count()


class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ['id']
