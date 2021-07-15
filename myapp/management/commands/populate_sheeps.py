# Django
from django.core.management.base import BaseCommand
from django.utils import timezone

# importing datetime module
from datetime import datetime

# creating an instance of
# datetime.date
import csv


# Multi Tenants

# Models
from myapp.models import Sheep, Breed, SheepBreed, SheepPhoto, HistoryWeight


path = './data/sheeps.csv'
SHEEP_CHOICES = []
cont = 0
with open(path, newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';')
    for row in spamreader:
        if cont:
            SHEEP_CHOICES.append(row)
        cont = cont+1
    print('Ingresar {} registros de sheeps'.format(cont))


path = './data/sheep_breeds.csv'
SHEEP_BREEDS = []
cont = 0
with open(path, newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';')
    for row in spamreader:
        if cont:
            SHEEP_BREEDS.append(row)
        cont = cont+1
    print('Ingresar {} registros de sheeps'.format(cont))



path = './data/sheep_picture.csv'
SHEEP_PICTURE = []
cont = 0
with open(path, newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';')
    for row in spamreader:
        if cont:
            SHEEP_PICTURE.append(row)
        cont = cont+1

    print('Ingresar {} registros de photos'.format(cont))



class Command(BaseCommand):
    def handle(self, *args, **options):
        for sheep in SHEEP_CHOICES:
            if not Sheep.objects.filter(identification_number=sheep[0]).exists():

                birthday_date = datetime.strptime(sheep[5], '%d/%m/%Y')
                birthday = timezone.make_aware(birthday_date, timezone.get_default_timezone())
                parentDadId = Sheep.objects.filter(identification_number=sheep[6]).first()
                parentMomId = Sheep.objects.filter(identification_number=sheep[7]).first()

                s = Sheep.objects.create(
                    identification_number=sheep[0],
                    identification_number_2=sheep[1],
                    name=sheep[2],
                    description=sheep[3],
                    gender=sheep[4],
                    parentDadId=parentDadId,
                    parentMomId=parentMomId,
                    active=sheep[8] == 'TRUE'
                )
                s.birthday = birthday
                s.save()

        for sheep_breed in SHEEP_BREEDS:
            if Sheep.objects.filter(identification_number=sheep_breed[0]).exists():
                print('sheep_breed', sheep_breed)
                sheep = Sheep.objects.filter(identification_number=sheep_breed[0]).first()
                breed = Breed.objects.filter(acronym=sheep_breed[1]).first()
                validate = SheepBreed.objects.filter(
                    sheep=sheep, 
                    breed=breed
                ).exists()

                if not validate:
                    SheepBreed.objects.create(
                        breed=breed,
                        sheep=sheep,
                        percent=sheep_breed[2]
                    )
        
        for sheep_picture in SHEEP_PICTURE:
            if Sheep.objects.filter(identification_number=sheep_picture[0]).exists():
                sheep = Sheep.objects.filter(identification_number=sheep_picture[0]).first()
                validate = SheepPhoto.objects.filter(
                    sheep=sheep, 
                    upload=sheep_picture[1]
                ).exists()
                
                if not validate:
                    create_at_date = datetime.strptime(sheep_picture[3], '%d/%m/%Y')
                    create_at = timezone.make_aware(create_at_date, timezone.get_default_timezone())
                    
                    sp = SheepPhoto.objects.create(
                        sheep=sheep,
                        upload=sheep_picture[1],
                        is_principal=sheep_picture[2] == 'TRUE'
                    )
                    sp.create_at = create_at
                    sp.save()