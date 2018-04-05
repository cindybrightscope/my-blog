from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail')
    # url(r'^$', views.api_root, name='api_root'),
    # url(r'^post$', views.PostListAPI.as_view(), name='post_list'),
    # url(r'^post/(?P<pk>\d+)/$', views.PostDetailAPI.as_view(), name='post_detail'),
    # url(r'^comment/$', views.CommentListAPI.as_view(), name='comment_list'),
    # url(r'^comment/(?P<pk>\d+)/$', views.CommentDetailAPI.as_view(), name='comment_detail')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)