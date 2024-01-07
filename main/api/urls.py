from django.urls import path
from main.api.views import HomeApiView

urlpatterns = [
    path("home/", HomeApiView.as_view(), name="home_api"),
]
