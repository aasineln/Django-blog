from _csv import reader
from decimal import Decimal

from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import Item, File
from .forms import UploadPriceForm, DocumentForm, MultiFilesForm


def some_view(request):
    items = Item.objects.all()
    return render(request, 'app_goods/item_list.html', {'item_list': items})


def update_prices(request):
    if request.method == 'POST':
        upload_file_form = UploadPriceForm(request.POST, request.FILES)
        if upload_file_form.is_valid():
            query_info = {
                'updated_items': 0,
                'new_items': 0,
                'new_items_list': []
            }
            price_file = upload_file_form.cleaned_data['file'].read()
            price_str = price_file.decode('cp1251').split('\r\n')
            csv_reader = reader(price_str, delimiter=":", quotechar='"')
            for row in csv_reader:
                if len(row) == 2:
                    query = Item.objects.filter(code=row[0])
                    if query:
                        query.update(price=Decimal(row[1]))
                        query_info['updated_items'] += 1
                    else:
                        query.create(code=row[0], price=Decimal(row[1]))
                        query_info['new_items'] += 1
                        query_info['new_items_list'].append(row[0])

            return HttpResponse(content=f'Цены успешно обновлены<br>{query_info}', status=200)
    else:
        upload_file_form = UploadPriceForm()

    context = {
        'form': upload_file_form
    }

    return render(request, 'app_goods/upload_price_file.html', context=context)


def doc_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = DocumentForm()

    return render(request, 'app_goods/upload_doc_file.html', {'form': form})


def upload_files(request):
    if request.method == 'POST':
        form = MultiFilesForm(request.POST, request.FILES)
        if form.is_valid():
            files = request.FILES.getlist('file_field')
            for f in files:
                instance = File(file=f)
                instance.save()
            return redirect('/')
    else:
        form = MultiFilesForm()

    return render(request, 'app_goods/upload_doc_file.html', {'form': form})
