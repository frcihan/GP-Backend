from django.contrib import admin
from .models import Category, Blog, Like, Comment, BlogView

admin.site.register(Category)
admin.site.register(Blog)
admin.site.register(BlogView)
admin.site.register(Like)
admin.site.register(Comment)

