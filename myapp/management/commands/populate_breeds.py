# Django
from django.core.management.base import BaseCommand

# Multi Tenants

# Models
from myapp.models import Breed

import csv

path = './data/breeds.csv'
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
            if not Breed.objects.filter(name=breed[0]).exists():
                Breed.objects.create(
                    name=breed[0].upper(),
                    acronym=breed[1],
                    color=breed[2],
                    description=breed[3],
                )
