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
