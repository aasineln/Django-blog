from django.contrib.sites import requests
from django.shortcuts import render
from django.db import models
from django.views import generic
from advertisements_app.models import Advertisement
from django.http import HttpResponse, HttpRequest


class AdvertisementListView(generic.ListView):
    model = Advertisement
    template_name = 'advertisement_list.html'
    context_object_name = 'advertisement_list'
    queryset = Advertisement.objects.all()


class AdvertisementDetailView(generic.DetailView):
    model = Advertisement
    queryset = Advertisement.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['price_to_dollar'] = Advertisement.objects.get(pk=context[self.pk_url_kwarg]).price

        return context

