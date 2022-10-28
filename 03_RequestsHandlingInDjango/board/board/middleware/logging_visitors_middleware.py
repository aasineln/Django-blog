from datetime import datetime
from django.core.exceptions import PermissionDenied


class LoggingVisitorsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        host = request.META.get('HTTP_HOST') + request.META.get('PATH_INFO')
        request_method = request.META.get('REQUEST_METHOD')
        current_datetime = datetime.now()

        with open('logging_visitors.txt','a+', encoding='utf-8') as log_file:
            log_file.write(
                f'{current_datetime} {host} {request_method}\n'
            )

        response = self.get_response(request)

        return response
