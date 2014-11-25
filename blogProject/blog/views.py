# coding: utf-8
from django.views import generic

from blogProject.blog.models import Entry, Tag

class BlogIndex(generic.ListView):
    queryset = Entry.objects.published()
    template_name = "home.html"
    paginate_by = 2