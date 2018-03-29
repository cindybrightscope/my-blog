from rest_framework import serializers
from blog.models import MyUser, Article, Comment


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('pk', 'writer', 'editor', 'title', 'text', 'created_date', 'published_date')


class CommentSerializer(serializers.ModelSerializer):
    #author = serializers.PrimaryKeyRelatedField(many=False, queryset=MyUser.objects.all())

    class Meta:
        model = Comment
        fields = ('pk', 'article', 'author', 'text', 'created_date')


class UserSerializer(serializers.ModelSerializer):
    posts = serializers.PrimaryKeyRelatedField(many=True, queryset=Article.objects.all())
    comments = serializers.PrimaryKeyRelatedField(many=True, queryset=Comment.objects.all())

    class Meta:
        model = MyUser
        fields = ('pk', 'username', 'email', 'posts', 'comments')