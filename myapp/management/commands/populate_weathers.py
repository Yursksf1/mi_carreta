# Django
from django.core.management.base import BaseCommand

from datetime import datetime

# Models
from myapp.models import HistoryWeather

WEATHERS = [
    ['01/02/2021 7:50', '0.5', '55.0', 'N'],
    ['01/02/2021 7:50', '1', '60.0', 'L'],
    ['01/02/2021 7:50', '0.7', '50.0', 'A'],

    ['02/02/2021 7:50', '0.5', '55.0', 'N'],
    ['02/02/2021 7:50', '1', '60.0', 'L'],
    ['02/02/2021 7:50', '0.7', '50.0', 'A'],

    ['27/06/2021 7:50', '0.7', '65.0', 'N'],
    ['27/06/2021 7:50', '2', '70.0', 'L'],
    ['27/02/2021 7:50', '1.7', '60.0', 'A'],

]


class Command(BaseCommand):
    def handle(self, *args, **options):
        for weathers in WEATHERS:
            date_take_weather = datetime.strptime(weathers[0], '%d/%m/%Y %H:%M')

            if not HistoryWeather.objects.filter(
                    create_at__day=date_take_weather.day,
                    location=weathers[3]
                ).exists():

                hs = HistoryWeather.objects.create(
                    humidity=weathers[2],
                    temperature=weathers[1],
                    location=weathers[3],
                    create_at=weathers[1],
                )

                hs.create_at = date_take_weather
                hs.save()
