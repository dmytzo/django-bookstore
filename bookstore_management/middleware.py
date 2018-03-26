from django.utils.deprecation import MiddlewareMixin

from bookstore_management.models import RequestLog


class RequestLogMiddleware(MiddlewareMixin):

    def process_request(self, request):
         RequestLog.objects.create(url=request.get_full_path())
