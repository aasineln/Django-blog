from django.shortcuts import render
from django.http import HttpResponse

def advertisements_list(request, *args, **kwargs):
    return render(request, 'advertisements/advertisements_list.html', {})

def item_1(request, *args, **kwargs):
    return render(request, 'advertisements/item_1.html', {})

def item_2(request, *args, **kwargs):
    return render(request, 'advertisements/item_2.html', {})

def item_3(request, *args, **kwargs):
    return render(request, 'advertisements/item_3.html', {})

def item_4(request, *args, **kwargs):
    return render(request, 'advertisements/item_4.html', {})

def item_5(request, *args, **kwargs):
    return render(request, 'advertisements/item_5.html', {})
