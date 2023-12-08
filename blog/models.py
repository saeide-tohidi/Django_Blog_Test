from django.db import models
from ckeditor.fields import RichTextField
from django.conf import settings
from django.utils.translation import gettext_lazy as _


class BlogCategory(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, allow_unicode=True)


class BlogTag(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, allow_unicode=True)


class BlogPost(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)
    header_image = models.ImageField()
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, allow_unicode=True)
    description = RichTextField()
    content = RichTextField()
    publish_at = models.DateTimeField()
    category = models.ForeignKey(
        "blog.BlogCategory", models.SET_NULL, null=True, blank=True, related_name="post"
    )
    tags = models.ManyToManyField("blog.BlogTag", related_name="post")
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_("Author"),
        related_name="blog_posts",
        on_delete=models.CASCADE,
    )
