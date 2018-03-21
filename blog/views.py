from .models import Article, Comment
from django.utils import timezone
from django.shortcuts import render, get_object_or_404


def post_list(request):
    posts = Article.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Article, pk=pk)
    comments = Comment.objects.filter(article=post, approved_comment=True)
    return render(request, 'blog/post_detail.html', {'post': post,
                                                     'comments': comments,
                                                     })