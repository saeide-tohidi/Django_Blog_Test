from django.contrib import admin
from blog.models import BlogCategory, BlogTag, BlogPost


admin.site.register(BlogCategory)
admin.site.register(BlogTag)
admin.site.register(BlogPost)
