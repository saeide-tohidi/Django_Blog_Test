from django.test import SimpleTestCase
from django.urls import reverse, resolve

from blog.views import BlogList, BlogSingle


class TestUrls(SimpleTestCase):
    def test_blog_list(self):
        url = reverse("blog_list")

        self.assertEqual(resolve(url).func.view_class, BlogList)

    def test_blog_single(self):
        url = reverse("blog_single", args=("first_blog",))
        print(resolve(url))
        self.assertEqual(resolve(url).func.view_class, BlogSingle)
