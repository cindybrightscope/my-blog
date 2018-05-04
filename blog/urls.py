from django.conf.urls import url
from django.conf import settings
from . import views
from django.conf.urls.static import static


urlpatterns = [
    #url(r'^$', views.post_list, name='post_list'),
    #url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail')
    url(r'^api$', views.api_root, name='api_root'),
    url(r'^api/post$', views.PostListAPI.as_view(), name='post_list'),
    url(r'^api/post/(?P<pk>\d+)/$', views.PostDetailAPI.as_view(), name='post_detail'),
    url(r'^api/comment/$', views.CommentListAPI.as_view(), name='comment_list'),
    url(r'^api/comment/(?P<pk>\d+)/$', views.CommentDetailAPI.as_view(), name='comment_detail')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)