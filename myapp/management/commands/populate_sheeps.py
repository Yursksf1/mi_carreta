# Django
from django.core.management.base import BaseCommand
from django.utils import timezone

# importing datetime module
from datetime import datetime

# creating an instance of
# datetime.date


# Multi Tenants

# Models
from myapp.models import Sheep, Breed, SheepBreed, SheepPhoto, HistoryWeight

SHEEP_CHOICES = [
    ['567', '13', 'jeronimo', '', 'M', '21/03/2019', '', '', 'FALSE'],
    ['2326', '127', 'Francois', '', 'M', '11/09/2014', '', '', 'TRUE'],
    ['2825', '', 'dorper', '', 'M', '5/05/2017', '', '', 'TRUE'],
    ['774943', '', 'Diamante', '', 'M', '17/08/2015', '', '', 'TRUE'],
    ['275219', '', 'Simba', '', 'M', '2/09/2016', '', '', 'TRUE'],
    ['275210', '666', 'Diabla', '', 'H', '11/12/2016', '', '', 'TRUE'],
    ['126', '334048', 'Bella', '', 'H', '12/04/2020', '', '', 'TRUE'],
    ['264', '', '3 rojo', '', 'H', '21/03/2020', '', '', 'TRUE'],
    ['081', '', 'hija de diabla', '', 'H', '2/01/2021', '', '275210', 'TRUE'],
    ['619', '', 'hijo de 3', '', 'M', '30/03/2021', '264', '567', 'TRUE'],
    ['275473', '', 'mangani', '', 'M', '17/08/2018', '', '', 'TRUE'],
    ['1224', '', 'Navidad', '', 'M', '17/08/2020', '', '', 'TRUE'],
    ['601', '', 'Dia de Reyes', '', 'M', '17/08/2020', '', '', 'TRUE'],
]

SHEEP_BREEDS = [
    ['567', 'HS', 100.00],
    ['2326', 'CL', 100.00],
    ['2825', 'DP', 100.00],
    ['774943', 'HS', 100.00],
    ['275219', 'HS', 100.00],
    ['275210', 'HS', 100.00],
    ['126', 'HS', 100.00],
    ['264', 'HS', 100.00],
    ['081', 'HS', 100.00],
    ['619', 'HS', 100.00],
    ['275473', 'HS', 100.00],
    ['1224', 'RM', 100.00],
    ['601', 'RM', 100.00],
]

SHEEP_PICTURE = [
    ['275219', 'media/Simba_c.jpg', 'FALSE'],
    ['275219', 'media/Sinba.jpg', 'TRUE'],
    ['2825', 'media/Dorper_c.jpg', 'FALSE'],
    ['2825', 'media/Dorper.jpg', 'TRUE'],
    ['2326', 'media/Francois_c.jpg', 'FALSE'],
    ['2326', 'media/Francois.jpg', 'TRUE'],
    ['275473', 'media/Mangani_c.jpg', 'FALSE'],
    ['275473', 'media/Mangani.jpg', 'TRUE'],
    ['1224', 'media/Navidad.jpg', 'TRUE'],
    ['601', 'media/Reyes.jpg', 'TRUE'],
    ['774943', 'media/Diamante.jpg', 'TRUE'],
]

class Command(BaseCommand):
    def handle(self, *args, **options):
        for sheep in SHEEP_CHOICES:
            if not Sheep.objects.filter(identification_number=sheep[0]).exists():

                birthday_date = datetime.strptime(sheep[5], '%d/%m/%Y')
                birthday = timezone.make_aware(birthday_date, timezone.get_default_timezone())

                print('birthday', birthday)

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
            sheep = Sheep.objects.filter(identification_number=sheep_picture[0]).first()
            validate = SheepPhoto.objects.filter(
                sheep=sheep, 
                upload=sheep_picture[1]
            ).exists()
            
            if not validate:
                SheepPhoto.objects.create(
                    sheep=sheep,
                    upload=sheep_picture[1],
                    is_principal=sheep_picture[2] == 'TRUE'
                )