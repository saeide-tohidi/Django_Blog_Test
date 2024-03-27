from django.urls import reverse
from django.views import View
from django.shortcuts import render, redirect
from .forms import ContactForm


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
        if request.user.is_authenticated:
            return redirect(reverse("blog_list"))
        else:
            context = {}
            return render(request, "main/index.html", context)


def contact_us(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect("/")
    else:
        form = ContactForm()
    return render(request, "main/contact_us.html", {"form": form})
