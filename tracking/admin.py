from django.contrib import admin
from .models import APIRequestLog


class APIRequestLogAdmin(admin.ModelAdmin):
    date_hierarchy = "requested_at"
    list_display = (
        "id",
        "requested_at",
        "response_ms",
        "status_code",
        "user",
        "view_method",
        "path",
        "remote_addr",
        "host",
        "query_params",
    )
    ordering = ("-requested_at",)
    list_filter = ("view_method", "status_code")


admin.site.register(APIRequestLog, APIRequestLogAdmin)
