from django.test import TestCase
from main.forms import ContactForm

from main.models import ContactUs


class TestContactUsForm(TestCase):
    @classmethod
    def setUpTestData(cls):
        ContactUs.objects.create(
            name="sara", email="sara@gmail.com", message="test message"
        )

    def test_valid_data(self):
        form = ContactForm(
            data={"name": "sara", "email": "saraaa@gmail.com", "message": "messsssss"}
        )
        self.assertTrue(form.is_valid())

    def test_empty_data(self):
        form = ContactForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 3)

    def test_exist_email(self):
        form = ContactForm(
            data={"name": "saraa", "email": "sara@gmail.com", "message": "messsssss"}
        )
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 1)
        self.assertTrue(form.has_error("email"))
