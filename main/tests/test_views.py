from django.contrib.auth.models import AnonymousUser
from django.test import Client, TestCase, RequestFactory
from django.urls import reverse, resolve

from main.forms import ContactForm
from main.models import ContactUs
from main.views import Home
from users.models import User


class TestHomeView(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create_user(
            email="test@gmail.com", password="testpass"
        )
        self.factory = RequestFactory()

    def test_home_user_authenticated(self):
        request = self.factory.get(reverse("home"))
        request.user = self.user
        response = Home.as_view()(request)
        self.assertEqual(response.status_code, 302)

    def test_home_user_anonymous(self):
        request = self.factory.get(reverse("home"))
        request.user = AnonymousUser()
        response = Home.as_view()(request)
        self.assertEqual(response.status_code, 200)


class TestContactUsView(TestCase):
    def setUp(self):
        self.client = Client()

    def test_contact_us_GET(self):
        response = self.client.get(reverse("contact_us"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "main/contact_us.html")
        self.failUnless(response.context["form"], ContactForm)

    def test_contact_us_POST_valid(self):
        response = self.client.post(
            reverse("contact_us"),
            data={"name": "sara", "email": "saraaa@gmail.com", "message": "message"},
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("home"))
        self.assertEqual(ContactUs.objects.count(), 1)

    def test_contact_us_POST_invalid(self):
        response = self.client.post(
            reverse("contact_us"),
            data={"name": "sara", "email": "saraagmail", "message": "message"},
        )
        self.assertEqual(response.status_code, 200)
        self.failIf(response.context["form"].is_valid())
        self.assertFormError(
            response=response,
            form="form",
            field="email",
            errors=["Enter a valid email address."],
        )
