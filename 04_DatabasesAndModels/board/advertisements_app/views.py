from django.shortcuts import render
from django.db import models
from django.views import generic
from advertisements_app.models import Advertisement
import random


class AdvertisementListView(generic.ListView):
    model = Advertisement
    template_name = 'advertisement_list.html'
    context_object_name = 'advertisement_list'
    queryset = Advertisement.objects.all()


class AdvertisementDetailView(generic.DetailView):
    model = Advertisement

#
# def advertisements_list(request, *args, **kwargs):
#     advertisements = Advertisement.objects.all()
#     return render(request, 'advertisements/advertisement_list.html', {'advertisements': advertisements})


# def random_advertisement(request, *args, **kwargs):
#     advertisements = Advertisement.objects.all()
#     random_adv = random.choice(advertisements)
#     print(random_adv, random_adv.title)
#     return render(request, 'advertisements/random_advertisement.html', {'advertisement': random_adv})
