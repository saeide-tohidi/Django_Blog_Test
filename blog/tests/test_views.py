from django.test import TestCase, SimpleTestCase

# Create your tests here.


class TestHome(SimpleTestCase):
    def test_fail(self):
        self.assertFalse(1 == 2)

    def test_true(self):
        self.assertTrue(1 == 1)
