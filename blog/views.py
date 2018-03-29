from .models import Article, Comment
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from blog.serializers import ArticleSerializer, CommentSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import generics, permissions
from rest_framework.reverse import reverse


def post_list(request):
    posts = Article.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Article, pk=pk)
    comments = Comment.objects.filter(article=post, approved_comment=True)
    return render(request, 'blog/post_detail.html', {'post': post,
                                                     'comments': comments,
                                                     })


class PostListAPI(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)

class PostDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class CommentListAPI(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)


class CommentDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def api_root(request, format=None):
    return Response({
        'posts': reverse('post_list', request=request, format=format),
        'comments': reverse('comment_list', request=request, format=format)
})

