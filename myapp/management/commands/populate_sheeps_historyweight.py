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


import csv

path = './data/sheep_history_weight.csv'
# path = '/Users/yurley.sanchez/Desktop/yurley/mi_carreta/data/sheep_history_weight.csv'
SHEEP_HISTORY_WEIGHT_CHOICES = []
cont = 0
headers = []
with open(path, newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';')
    for row in spamreader:
        if cont:
            for index, date in enumerate(headers[2:]):
                if row[index+2] and row[index+2].strip():
                    new_row = []
                    new_row.append(row[1])
                    new_row.append(row[index+2].replace(',','.'))
                    new_row.append(date)
                    SHEEP_HISTORY_WEIGHT_CHOICES.append(new_row)
        else:
            for r in row:
                headers.append(r)
        cont = cont+1

    print('Ingresar {} registros'.format(cont))
    print(SHEEP_HISTORY_WEIGHT_CHOICES)

class Command(BaseCommand):
    def handle(self, *args, **options):
        for sheep in SHEEP_HISTORY_WEIGHT_CHOICES:

            birthday_date = datetime.strptime(sheep[2], '%d/%m/%Y')
            create_at = timezone.make_aware(birthday_date, timezone.get_default_timezone())
            sheepId = Sheep.objects.filter(identification_number=sheep[0]).first()
            if sheepId:
                s = HistoryWeight.objects.create(
                    sheep=sheepId,
                    weight=sheep[1],
                )
                s.create_at = create_at
                s.save()
