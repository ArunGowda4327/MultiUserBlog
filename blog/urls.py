from django.conf.urls import url
from blog import views

urlpatterns = [

    url(r'^$', views.PostListView.as_view(), name='post_list'),
    url(r'^about/$', views.AboutView.as_view(), name='about'),
    url(r'^post/(?P<pk>\d+)$', views.PostDetailView.as_view(), name='post_detail'),
    url(r'^create/$', views.CreatePostView.as_view(), name='create'),
    url(r'^update/(?P<pk>\d+)/$', views.PostUpdateView.as_view(), name='update'),
    url(r'^remove/(?P<pk>\d+)/$', views.PostDeleteView.as_view(), name='remove'),
    url(r'^drafts/$', views.PostDraftListView.as_view(), name='draft_list'),

    url(r'^post_publish/(?P<pk>\d+)/$', views.post_publish, name='post_publish'),


    url(r'^comment/(?P<pk>\d+)/$', views.add_comment_to_post, name='comment'),
    url(r'^comment_approve/(?P<pk>\d+)/$', views.comment_approve, name='comment_approve'),
    url(r'^comment_remove/(?P<pk>\d+)/$', views.comment_remove, name='comment_remove'),


]
