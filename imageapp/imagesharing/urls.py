from django.conf.urls import url
from django.contrib import admin
from classviews import UserCreateView, UserUpdateView, UserDeleteView

from .views import (
post_create,
post_delete,
post_detail,
post_list,
post_update,
user_list,
posts_ids,
postsids,

)

urlpatterns = [
    url(r'^$',user_list ,name='user_list'),
    url(r'^create/$',UserCreateView.as_view()),
    url(r'^(?P<pk>[0-9]+)/update/$',UserUpdateView.as_view()),
    url(r'^(?P<pk>[0-9]+)/delete/$',UserDeleteView.as_view()),
    url(r'^posts/$', post_list, name='list'),
    url(r'^posts/user/(?P<id>\d+)/$',posts_ids),
    url(r'^posts/(?P<id>\d+)/user/$',postsids),
    url(r'^posts/create/$', post_create),
    url(r'^posts/(?P<id>\d+)/$', post_detail, name='detail'),
    url(r'^posts/(?P<id>\d+)/edit/$', post_update),
    url(r'^posts/(?P<id>\d+)/delete/$', post_delete),

    #url(r'^posts/$', "appname.views.function_name")
]
