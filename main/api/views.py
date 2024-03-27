from rest_framework.response import Response
from rest_framework.views import APIView

from tracking.mixins import LoggingMixin


class HomeApiView(LoggingMixin, APIView):
    def get(self, request):
        return Response("Hello")
