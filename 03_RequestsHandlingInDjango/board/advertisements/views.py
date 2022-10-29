from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic import TemplateView


class Advertisements(View):
    get_counter = 0
    post_counter = 0

    def get(self, request):
        advertisements = ['Фотосъемка',
                          'Разработка ПО',
                          'Тестирование ПО',
                          'Ремонт ноутбуков',
                          'Ремонт телефонов',
                          'Услуги экскаватора-погрузчика, гидромолота, ямобура'
                          ]

        Advertisements.get_counter += 1

        return render(request, 'advertisements/advertisements.html', {'advertisements': advertisements,
                                                                      'get_counter': Advertisements.get_counter,
                                                                      'post_counter': Advertisements.post_counter})

    def post(self, request):
        form_advertisement_message = 'Объявление успешно создано!'
        Advertisements.post_counter += 1
        return HttpResponse(form_advertisement_message)


class Main(View):
    def get(self, request):
        categories = ['личные вещи',
                      'транспорт',
                      'хобби и отдых'
                      ]

        regions = ['Алтайский край',
                   'Краснодарский край',
                   'Московская область',
                   'Ленинградская область'
                   ]

        return render(request, 'advertisements/main.html', {'categories': categories,
                                                            'regions': regions})

    def post(self, request):
        main_form_ad_message = 'Объявление успешно найдено!'
        return HttpResponse(main_form_ad_message)


class Contacts(TemplateView):
    template_name = 'advertisements/contacts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['address'] = 'г. Краснодар, ул. Красная, д. 5'
        context['phone'] = '8-800-708-19-45'
        context['email'] = 'sales@company.com'

        return context


class About(TemplateView):
    template_name = 'advertisements/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about_title'] = 'Бесплатные объявления'
        context['about_description'] = 'Бесплатные объявления в вашем городе!'

        return context


def categories_list(request, *args, **kwargs):
    categories = ['личные вещи',
                  'транспорт',
                  'хобби и отдых'
                  ]

    return render(request, 'advertisements/categories_list.html', {'categories': categories})


class Regions(View):
    def get(self, request):
        regions = ['Алтайский край',
                   'Краснодарский край',
                   'Московская область',
                   'Ленинградская область'
                   ]

        return render(request, 'advertisements/regions.html', {'regions': regions})

    def post(self, request):
        form_region_message = 'Регион успешно создан!'
        return HttpResponse(form_region_message)
