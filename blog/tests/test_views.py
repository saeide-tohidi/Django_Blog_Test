from django.test import TestCase, SimpleTestCase, Client
from django.urls import reverse
from users.models import User


class TestHome(SimpleTestCase):
    def test_fail(self):
        self.assertFalse(1 == 2)

    def test_true(self):
        self.assertTrue(1 == 1)


class TestBlogListView(TestCase):
    def setUp(self):
        User.objects.create_user(email="test@gmail.com", password="testpass")
        self.client = Client()
        self.client.login(email="test@gmail.com", password="testpass")

    def test_blog_list_GET(self):
        response = self.client.get(reverse("blog_list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "blog/blog_list.html")
