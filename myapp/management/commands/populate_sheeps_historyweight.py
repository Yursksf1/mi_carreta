# Django
from django.core.management.base import BaseCommand
from django.utils import timezone

# importing datetime module
from datetime import datetime

# creating an instance of
# datetime.date


# Multi Tenants

# Models
from myapp.models import Sheep, HistoryWeight


SHEEP_HISTORY_WEIGHT_CHOICES = [
    ['275219', 138.0, '06/03/2021'],
    ['275219', 141.0, '14/03/2021'],
    ['275219', 141.5, '19/03/2021'],
    ['275219', 138.5, '26/03/2021'],
    ['275219', 139.0, '02/04/2021'],
    ['275219', 134.5, '16/04/2021'],
    ['275219', 142.5, '27/04/2021'],
    ['275219', 134.0, '12/05/2021'],
    ['275219', 132.0, '30/05/2021'],
    ['275219', 130.0, '15/06/2021'],
    ['275219', 129.5, '30/06/2021'],
]


class Command(BaseCommand):
    def handle(self, *args, **options):
        for sheep in SHEEP_HISTORY_WEIGHT_CHOICES:

            birthday_date = datetime.strptime(sheep[2], '%d/%m/%Y')
            create_at = timezone.make_aware(birthday_date, timezone.get_default_timezone())
            sheepId = Sheep.objects.filter(identification_number=sheep[0]).first()

            s = HistoryWeight.objects.create(
                sheep=sheepId,
                weight=sheep[1],
            )
            s.create_at = create_at
            s.save()
