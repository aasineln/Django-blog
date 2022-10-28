from time import time
from django.core.exceptions import PermissionDenied


class StopDDOSMiddleware5RequestsMinute:
    def __init__(self, get_response):
        self.get_response = get_response
        self.from_ip_requests_count_dict = {}
        self.max_count_requests = 5
        self.period_for_max_count_requests = 20


    def __call__(self, request):
        ip = request.META.get('REMOTE_ADDR')

        # Проверка, есть ли ip в словаре from_ip_requests_count_dict
        # Да: +1 запрос, нет: добавляем ip в словарь и фиксируем время запроса.
        if self.from_ip_requests_count_dict.get(ip):
            self.from_ip_requests_count_dict[ip]['count'] += 1
            # Проверка периода self.period_for_max_count_requests, за какое время кол-во запросов достигло
            # self.max_count_requests. Если за указанный период, то обнуление и ошибка, если дольше, то просто обнулить.
            if self.from_ip_requests_count_dict[ip]['count'] == self.max_count_requests\
                    and time() - self.from_ip_requests_count_dict[ip]['time'] < self.period_for_max_count_requests:
                self.from_ip_requests_count_dict[ip]['count'] = 0
                self.from_ip_requests_count_dict[ip]['time'] = time()
                raise PermissionDenied
            elif self.from_ip_requests_count_dict[ip]['count'] == self.max_count_requests\
                    and time() - self.from_ip_requests_count_dict[ip]['time'] > self.period_for_max_count_requests:
                self.from_ip_requests_count_dict[ip]['count'] = 0
                self.from_ip_requests_count_dict[ip]['time'] = time()
        else:
            self.from_ip_requests_count_dict[ip] = {}
            self.from_ip_requests_count_dict[ip]['count'] = 0
            self.from_ip_requests_count_dict[ip]['time'] = time()

        response = self.get_response(request)

        return response
