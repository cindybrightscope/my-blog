from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class MyUser(User):
    is_writer = models.BooleanField(default=False)
    is_editor = models.BooleanField(default=False)
    is_logged_in_user = models.BooleanField(default=False)

    class Meta:
        permissions = (
            ('comment_article', 'Can comment article'),
            ('create_article', 'Can create article'),
            ('publish_article', 'Can publish article'),
        )

    def writer_status(self):
        return self.is_writer

    def editor_status(self):
        return self.is_editor


class Article(models.Model):
    writer = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='writer')
    editor = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='editor', null=True, blank=True)

    title = models.CharField(max_length=200)
    text = models.TextField()

    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Comment(models.Model):
    article = models.ForeignKey('blog.Article', related_name='comments')
    author = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    text = models.TextField()

    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=True)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
