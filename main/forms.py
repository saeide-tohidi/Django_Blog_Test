from django import forms
from django.core.exceptions import ValidationError

from .models import ContactUs


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ["name", "email", "message"]
        widgets = {
            "message": forms.Textarea(
                attrs={"rows": 5}
            ),  # Customize the message field with a textarea
        }

    def clean_email(self):
        email = self.cleaned_data["email"]
        contact = ContactUs.objects.filter(email=email).exists()

        if contact:
            raise ValidationError("This email already exist")

        else:
            return email
