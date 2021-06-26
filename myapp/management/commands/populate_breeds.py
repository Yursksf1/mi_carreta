# Django
from django.core.management.base import BaseCommand

# Multi Tenants

# Models
from myapp.models import Breed

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


class Command(BaseCommand):
    def handle(self, *args, **options):
        for role in ROLE_CHOICES:
            if not Breed.objects.filter(name=role[0]).exists():
                Breed.objects.create(
                    name=role[0].upper(),
                    description=role[1],
                )
