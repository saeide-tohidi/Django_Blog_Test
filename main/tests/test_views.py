from django.test import Client, TestCase
from django.urls import reverse, resolve

from main.forms import ContactForm
from main.models import ContactUs


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
