from concurrent.futures import as_completed
from requests_futures.sessions import FuturesSession
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic.base import View
from django.contrib.auth.mixins import LoginRequiredMixin
from checker.models import Link, Interval


class Index(LoginRequiredMixin, View):
    login_url = '/admin/'

    @staticmethod
    def get(request):
        args = {
            'links': Link.objects.filter(pause=False),
            'interval': Interval.get_milliseconds()
        }
        return render(request, 'index.html', args)


class RequestUrl(LoginRequiredMixin, View):
    login_url = '/admin/'

    @staticmethod
    def response_hook(response, *args, **kwargs):
        response.data = response.json()

    def get(self, request):
        urls = [link.url for link in Link.objects.filter(pause=False)]
        result = []
        with FuturesSession() as session:
            futures = [session.get(url) for url in urls]

            for i, future in enumerate(as_completed(futures)):
                try:
                    response = future.result()
                    result.append({'url': response.url, 'code': response.status_code})
                except Exception as e:
                    url = urls[::-1][i]
                    result.append({'url': url, 'code': 500})

        return JsonResponse({'status': 'ok', 'result': result})
