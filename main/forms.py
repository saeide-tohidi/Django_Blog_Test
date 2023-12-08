from django import forms
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
