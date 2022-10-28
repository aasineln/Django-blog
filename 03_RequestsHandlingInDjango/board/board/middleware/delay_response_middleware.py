import time


class DelayHttpResponse:
    def __init__(self, _get_response):
        self._get_response = _get_response
        self._delay = 1

    def __call__(self, request):
        time.sleep(self._delay)
        response = self._get_response(request)

        return response
