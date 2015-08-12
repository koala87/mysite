from django.contrib import admin

# Register your models here.

from news.models import News, Comment

admin.site.register(Comment)

admin.site.register(News)
