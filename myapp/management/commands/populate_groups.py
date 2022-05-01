# Django
from django.core.management.base import BaseCommand

# Multi Tenants

# Models
from myapp.models import Group

import csv

path = './data/groups.csv'
BREEDS = []
cont = 0
with open(path, newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';')
    for row in spamreader:
        if cont:
            BREEDS.append(row)
        cont = cont+1

    print('Ingresar {} registros'.format(cont))


class Command(BaseCommand):
    def handle(self, *args, **options):
        for breed in BREEDS:
            if not Group.objects.filter(name=breed[0]).exists():
                Group.objects.create(
                    name=breed[0].upper(),
                    slug=breed[1],
                    active=True,
                    description=breed[2],
                )
