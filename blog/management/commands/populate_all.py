from django.core.management.base import BaseCommand
from blog.models import MyUser, Article, Comment
from django.contrib.auth.models import Permission
import random


class Command(BaseCommand):
    help = 'Populates dummy data into the models'

    writer_list = []
    editor_list = []
    login_user_list = []
    article_list = []

    def populate_user(self):
        for i in range(20, 30):
            user = self.create_user(i)
            user.save()

            if user.is_editor:
                create_perm = Permission.objects.get(codename='create_article')
                publish_perm = Permission.objects.get(codename='publish_article')
                comment_perm = Permission.objects.get(codename='comment_article')
                user.user_permissions.add(create_perm, publish_perm, comment_perm)
                self.writer_list.append(user)
                self.editor_list.append(user)
            elif user.is_writer:
                create_perm = Permission.objects.get(codename='create_article')
                comment_perm = Permission.objects.get(codename='comment_article')
                user.user_permissions.add(create_perm, comment_perm)
                self.writer_list.append(user)
            else:
                comment_perm = Permission.objects.get(codename='comment_article')
                user.user_permissions.add(comment_perm)

            self.login_user_list.append(user)

    def create_user(self, index):
        if index <= 5:
            my_user, created = MyUser.objects.get_or_create(username='LoggedInUser{}'.format(index),
                                                            password='TestingUserPw{}'.format(index),
                                                            email='TestUser{}@fakeemail.com'.format(index),
                                                            is_logged_in_user=True
                                                            )
        elif 5 < index <= 10:
            my_user, created = MyUser.objects.get_or_create(username='WriterUser{}'.format(index),
                                                            password='TestingUserPw{}'.format(index),
                                                            email='TestUser{}@fakeemail.com'.format(index),
                                                            is_writer=True)
        else:
            my_user, created = MyUser.objects.get_or_create(username='EditorUser{}'.format(index),
                                                            password='TestingUserPw{}'.format(index),
                                                            email='TestUser{}@fakeemail.com'.format(index),
                                                            is_editor=True)


        return my_user

    def create_article(self):
        for i in range(5, 15):
            article = Article.objects.create(writer=random.choice(self.writer_list),
                                             editor=random.choice(self.editor_list),
                                             title='Test Title{}'.format(i),
                                             text='Test text{}'.format(i))
            self.article_list.append(article)
            article.publish()
            article.save()

    def create_comment(self):
        for i in range(8, 18):
            comment = Comment.objects.create(article=random.choice(self.article_list),
                                             author=random.choice(self.login_user_list),
                                             text='Test comment {}'.format(i))
            comment.save()

    def handle(self, *args, **options):
        self.populate_user()
        self.create_article()
        self.create_comment()