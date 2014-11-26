from django.contrib.syndication.views import Feed
from blogProject.blog.models import Entry

class LatestPosts(Feed):
    title = "Q Blog"
    link = "/feed/"
    description = "Latest Posts"

    def items(self):
        return Entry.objects.published()[:5]