# Django
from django.core.management.base import BaseCommand

# Multi Tenants

# Models
from myapp.models import Breed

BREEDS = [
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
