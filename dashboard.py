from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from grappelli.dashboard import modules, Dashboard


class CustomIndexDashboard(Dashboard):
    def init_with_context(self, context):
        self.children.append(
            modules.ModelList(
                title="User",
                column=1,
                models=("users.models.*",),
            )
        )
        self.children.append(
            modules.ModelList(
                title="Blog",
                column=1,
                models=("blog.models.*",),
            )
        )

        self.children.append(
            modules.ModelList(
                _("Administration"),
                column=1,
                models=("django.contrib.*",),
            )
        )
