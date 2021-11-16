from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required

from todo_app import views
import classviews



urlpatterns = [

    url(r'^accounts/', include('django.contrib.auth.urls'),{"template_name":"login.html"}),
    url(r'^$',login_required(views.index) ),

    url(r'^lists/$', login_required(views.get_list), name = 'list_details'),
    url(r'^lists/listitem(?P<id>[0-9]+)/$', login_required(views.get_list_items), name = "list_item_details"),
    url(r'^lists/createlist',login_required(classviews.ListCreateView.as_view()),name='list_create'),
    url(r'^lists/(?P<id>[0-9]+)/updatelist$',login_required(classviews.ListUpdateView.as_view()),name='list_update'),
    url(r'^lists/(?P<pk>[0-9]+)/deletelist$',login_required(classviews.ListDeleteView.as_view()),name='list_delete'),
    url(r'^lists/(?P<id>[0-9])/(?P<pk>[0-9]+)/updateitem',login_required(classviews.ItemUpdateView.as_view()),name='item_update'),
    url(r'^lists/(?P<id>[0-p]+)/(?P<pk>[0-9]+)/deleteitem',login_required(classviews.ItemDeleteView.as_view()),name='item_delete'),
    url(r'^lists/(?P<pk>[0-9]+)/createitem',classviews.ItemCreateView.as_view(), name='item_create'),



]
