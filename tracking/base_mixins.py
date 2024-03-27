import ast
import ipaddress
import logging
import traceback

from django.db import connection
from django.utils.timezone import now


logger = logging.getLogger(__name__)


class BaseLoggingMixin(object):
    def initial(self, request, *args, **kwargs):
        return super(BaseLoggingMixin, self).initial(request, *args, **kwargs)

    def finalize_response(self, request, response, *args, **kwargs):
        return super(BaseLoggingMixin, self).finalize_response(
            request, response, *args, **kwargs
        )
