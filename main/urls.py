from django.urls import path, include

from main.views import Header, Footer, Home, contact_us

urlpatterns = [
    path("header", Header.as_view(), name="header"),
    path("footer", Footer.as_view(), name="footer"),
    path("", Home.as_view(), name="home"),
    path("contact_us/", contact_us, name="contact_us"),
]
