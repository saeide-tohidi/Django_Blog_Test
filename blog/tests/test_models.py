from django.test import TestCase
from blog.models import BlogPost
from model_bakery import baker


class TestBlogPostModel(TestCase):
    def setUp(self) -> None:
        self.blog = baker.make(BlogPost, title="test title")

    def test_model_str(self):
        self.assertEqual(str(self.blog), "test title")
