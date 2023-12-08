from django.urls import path, include

from main.views import (
    Header,
    Footer,
    Home,
)

urlpatterns = [
    path("header", Header.as_view(), name="header"),
    path("footer", Footer.as_view(), name="footer"),
    path("", Home.as_view(), name="home"),
]
