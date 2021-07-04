# Django
from django.core.management.base import BaseCommand

from datetime import datetime

# Models
from myapp.models import HistoryWeather
import csv

path = './data/weather.csv'
WEATHERS = []
cont = 0
with open(path, newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';')
    for row in spamreader:
        if cont:
            WEATHERS.append(row)
        cont = cont+1

    print('Ingresar {} registros'.format(cont))

class Command(BaseCommand):
    def handle(self, *args, **options):
        for weathers in WEATHERS:
            date_take_weather = datetime.strptime(weathers[0], '%d/%m/%Y %H:%M')

            if not HistoryWeather.objects.filter(
                    create_at__day=date_take_weather.day,
                    create_at__month=date_take_weather.month,
                    create_at__year=date_take_weather.year,
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
