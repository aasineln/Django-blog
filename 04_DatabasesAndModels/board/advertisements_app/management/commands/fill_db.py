from django.core.management import BaseCommand
from advertisements_app.models import Advertisement


class Command(BaseCommand):
    help = u'Заполнение БД 500к записей'

    def handle(self, *args, **options):
        objs = (Advertisement(
            title=f'Объявление {i_adv}',
            description=f'Описание объявления {i_adv}',
        ) for i_adv in range(500000))

        Advertisement.objects.bulk_create(objs)
