from django.contrib import admin
from django.contrib.auth.models import Permission
from .models import Article, Comment, MyUser


admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(MyUser)
admin.site.register(Permission)