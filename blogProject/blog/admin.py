# coding: utf-8

from django.contrib import admin

from blogProject.blog.models import Entry, Tag
from django_markdown.admin import MarkdownModelAdmin

class EntryAdmin(MarkdownModelAdmin):
    list_display = ("title", "created_at")
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Entry, EntryAdmin)
admin.site.register(Tag)