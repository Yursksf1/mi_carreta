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

ROLE_CHOICES = [
    ['Hampshire',
     'No Tengo idea de que sea'],

    ['Hampshire dwon',
     'Es una raza de origen inglés, utilizada para aprovechar las praderas de las colinas. Es un animal ágil y caminador. Se ha utilizado para mejorar razas criollas.'],

    ['Charollais',
     'Es una raza formada en Inglaterra, adaptada para terrenos planos. Es un animal precoz y muy buen productor de carne.'],

    ['Dorper',
     'Es de origen Finlandés. Es una raza de alta prolificidad, con un potencial de 200% de tasa de parición (dos animales por oveja en cada parto) y muy precoz, estas características hacen que esta raza pueda reemplazar rápidamente a otras razas dentro del rebaño.'],

    ['Dorset',
     'Raza de origen holandés desarrollada de la cruza de varias razas criollas a fines del siglo XIX e inicios del siglo XX. Dentro de las razas para carne es la que presenta las mejores aptitudes, obteniéndose corderos de alta tasa de crecimiento y muy magros llegando a peso óptimo de faena a los 40 kilos, 10 kilos más que un cordero Corriedale.'],

    ['suffolk',
     'Raza originaria de la ciudad de Leicestershire, Inglaterra. Es la responsable del mejoramiento y desarrollo de las razas de lana larga. De rápido crecimiento y por lo tanto de rápida presencia de los corderos en el mercado.'],
    
    ['romney marsh',
     'Raza originaria de la ciudad de Leicestershire, Inglaterra. Es la responsable del mejoramiento y desarrollo de las razas de lana larga. De rápido crecimiento y por lo tanto de rápida presencia de los corderos en el mercado.'],

    ['Katahdin', 
    'El borrego Katahdin es un tipo de oveja que tiene sus inicios a finales de los años de 1950, siendo creada por Michael Pie'],

    ['Pelibuey', 
    'La pelibuey ​ es una raza de oveja doméstica nativa del Norte de África y de las Islas Canarias, llevada al Caribe y América Central por los españoles.​'],

    ['Criollo', 
    'some description here'],

    ['Mora', 
    'La oveja mora colombiana, se caracteriza por su color oscuro en el vellón'],

    ['East friesian', 
    'La East Friesian es una raza de ovejas lecheras originarias de Frisia Oriental en el norte de Alemania'],

]

SHEEP_CHOICES = [
    ['2326', 'Francois', '', 'M', '11/09/2014', '', '', 'True'],
    ['2825', 'dorper', '', 'M', '5/05/2017', '', '', 'True'],
    ['774943', 'Diamante', '', 'M', '17/08/2015', '', '', 'True'],
    ['275219', 'Simba', '', 'M', '2/09/2016', '', '', 'True'],
    ['275210', 'Diabla', '', 'H', '11/12/2016', '', '', 'True'],
    ['126', 'Bella', '', 'H', '12/04/2020', '', '', 'True'],
    ['264', '3 rojo', '', 'H', '21/03/2020', '', '', 'True'],
    ['081', 'hija de diabla', '', 'H', '2/01/2021', '', '275210', 'True'],
    ['619', 'hijo de 3', '', 'M', '30/03/2021', '774943', '264', 'True'],
]


class Command(BaseCommand):
    def handle(self, *args, **options):
        for sheep in SHEEP_CHOICES:
            if not Sheep.objects.filter(identification_number=sheep[0]).exists():

                birthday_date = datetime.strptime(sheep[4], '%d/%m/%Y')
                birthday = timezone.make_aware(birthday_date, timezone.get_default_timezone())

                print('birthday', birthday)

                parentDadId = Sheep.objects.filter(identification_number=sheep[5]).first()
                parentMomId = Sheep.objects.filter(identification_number=sheep[6]).first()

                s = Sheep.objects.create(
                    identification_number=sheep[0],
                    name=sheep[1],
                    description=sheep[2],
                    gender=sheep[3],
                    parentDadId=parentDadId,
                    parentMomId=parentMomId,
                    active=sheep[7] == 'True'
                )
                s.birthday = birthday
                s.save()
