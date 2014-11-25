# coding: utf-8

from django.conf.urls import patterns, include, url
from blogProject.blog import views

urlpatterns = patterns('',
    url(r'^$', views.BlogIndex.as_view(), name="index"),
)