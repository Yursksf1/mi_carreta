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
    ['CRIOLLA',
     'No Tengo idea de que sea'],

    ['SUFFOLK',
     'Es una raza de origen inglés, utilizada para aprovechar las praderas de las colinas. Es un animal ágil y caminador. Se ha utilizado para mejorar razas criollas.'],

    ['HAMPSHIRE DOWN',
     'Es una raza formada en Inglaterra, adaptada para terrenos planos. Es un animal precoz y muy buen productor de carne.'],

    ['FINNISH LANDRACE ó FINNSHEEP',
     'Es de origen Finlandés. Es una raza de alta prolificidad, con un potencial de 200% de tasa de parición (dos animales por oveja en cada parto) y muy precoz, estas características hacen que esta raza pueda reemplazar rápidamente a otras razas dentro del rebaño.'],

    ['TEXEL',
     'Raza de origen holandés desarrollada de la cruza de varias razas criollas a fines del siglo XIX e inicios del siglo XX. Dentro de las razas para carne es la que presenta las mejores aptitudes, obteniéndose corderos de alta tasa de crecimiento y muy magros llegando a peso óptimo de faena a los 40 kilos, 10 kilos más que un cordero Corriedale.'],

    ['BORDER LEICESTER',
     'Raza originaria de la ciudad de Leicestershire, Inglaterra. Es la responsable del mejoramiento y desarrollo de las razas de lana larga. De rápido crecimiento y por lo tanto de rápida presencia de los corderos en el mercado.'],

]

SHEEP_CHOICES = [
    ['666', 'La Diabla', 'Es grande y tiene mal genio', 'H', '31/01/2020', '', '', 'True'],
    ['656', 'La no tan Diabla', 'Es grande y peluda', 'H', '31/01/2020', '', '', 'True'],

    ['600', 'Navidad', 'Parece una ovejita de navidad', 'M', '28/02/2020', '', '', 'True'],
    ['601', 'Dia de Reyes', 'Parece navidad pero no tanto', 'M', '28/02/2020', '', '', 'True'],
    ['602', 'Diamante', 'Es el nombre del Wifi', 'M', '15/01/2020', '', '', 'True'],

    ['701', 'Oveja Pilincho 1', 'es una oveja pequena', 'H', '15/03/2021', '602', '656', 'True'],
    ['702', 'Oveja Pilincho 2', 'es una oveja pequena', 'M', '15/03/2021', '602', '666', 'True'],
    ['703', 'Oveja Pilincho 3', 'es una oveja pequena', 'H', '20/06/2021', '600', '656', 'True'],
    ['704', 'Oveja Pilincho 4', 'es una oveja pequena', 'H', '20/06/2021', '600', '666', 'True'],

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
