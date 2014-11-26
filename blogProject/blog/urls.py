# coding: utf-8

from django.conf.urls import patterns, include, url
from blogProject.blog import views, feed
from . import views, feed

urlpatterns = patterns('',
    url(r'^$', views.BlogIndex.as_view(), name="index"),
    url(r'^feed/$', feed.LatestPosts(), name="feed"),
    url(r'^(?P<slug>\S+)$', views.BlogDetail.as_view(), name="entry_detail"),
)