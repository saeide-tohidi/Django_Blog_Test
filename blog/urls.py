from django.urls import path
from .views import BlogList, BlogListCategory, BlogSingle, BlogListTag


urlpatterns = [
    # path("about-us/", AboutUs.as_view(), name="aboutus"),
    # path("contact/", Contact.as_view(), name="contact"),
    # path("category/<str:category>/", BlogListCategory.as_view(), name="blog_category"),
    # path("tag/<str:tag>/", BlogListTag.as_view(), name="blog_tag"),
    path("list/", BlogList.as_view(), name="blog_list"),
    path("<str:slug>/", BlogSingle.as_view(), name="blog_single"),
]
