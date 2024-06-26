from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static


urlpatterns = [
    path("grappelli/", include("grappelli.urls")),
    path("admin/", admin.site.urls),
    path("ckeditor/", include("ckeditor_uploader.urls")),
    path("accounts/", include("allauth.urls")),
    path("", include("main.urls")),
    path("api/", include("main.api.urls")),
    path("blog/", include("blog.urls")),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
