from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import pytz
import datetime as dt
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView, ListView


class Header(View):
    def get(self, request):
        context = {}
        return render(request, "main/shared/header.html", context)

    def post(self, request, *args, **kwargs):
        return self.get(request, *args, **kwargs)


class Footer(View):
    def get(self, request):
        context = {}
        return render(request, "main/shared/footer.html", context)

    def post(self, request, *args, **kwargs):
        return self.get(request, *args, **kwargs)


class Home(View):
    def get(self, request):
        context = {}
        return render(request, "main/index.html", context)


from django.shortcuts import render
from .forms import ContactForm


def contact_us(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            print("form is valid")
            # Add logic here for sending emails, thank you messages, etc.
            # Redirect or render a success page
            return render(request, "main/contact_us.html", {"form": form})
    else:
        form = ContactForm()
    return render(request, "main/contact_us.html", {"form": form})
