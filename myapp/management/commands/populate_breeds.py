# Django
from django.core.management.base import BaseCommand

# Multi Tenants

# Models
from myapp.models import Breed

BREEDS = [
    ['DORPER', 'DP', 'blue-dark', 
    'Dorper es una raza ovina de Sudáfrica, desarrollada en el año de 1930. Más tarde en 1946 se lleva a cabo el cruce entre la Dorset Horn y la oveja persa Blackhead, de ahí proviene el nombre Dorper'],

    ['CRIOLLO', 'CR', 'brown', 
    'some description here'],

    ['KATAHDIN', 'KT', 'fucsia', 
    'El borrego Katahdin es un tipo de oveja que tiene sus inicios a finales de los años de 1950, siendo creada por Michael Piel, ​ en Estados Unidos, nombrada así por el Monte Katahdin en Maine'],

    ['HAMPSHIRE', 'HS', 'green', 
    'Hampshire es una raza de ovinos lograda en 1880 al sur de Inglaterra, en el condado de Hampshire. Se logró gracias a la mezcla de distintas razas, entre ellas la Bershire Knot, Hampshire Old y Willshire Horn. El Hampshire es fuerte, muy estilizado y de gran adaptación al clima variado. No debe tener rasgos de tosquedad ni aparentar debilidad. Es un animal carnicero con buena masa muscular, profundo, corto y ancho, (la profundidad está dada por la distancia de la cruz a la cinchera[aclaración requerida]). Su cabeza es más ancha que larga, el cuello es ancho, no tiene cuernos, sus orejas son largas y el pelaje es oscuro. Esto se repite en la cara y en los miembros anterior y posterior desde las rodillas y garrones hasta las pezuñas, respectivamente. Los ojos están libres de lana. El largo de los miembros debe ser armónico con el cuerpo.'],

    ['HAMPSHIRE DOWN', 'HS', 'green', 
    'Hampshire es una raza de ovinos lograda en 1880 al sur de Inglaterra, en el condado de Hampshire. Se logró gracias a la mezcla de distintas razas, entre ellas la Bershire Knot, Hampshire Old y Willshire Horn. El Hampshire es fuerte, muy estilizado y de gran adaptación al clima variado. No debe tener rasgos de tosquedad ni aparentar debilidad. Es un animal carnicero con buena masa muscular, profundo, corto y ancho, (la profundidad está dada por la distancia de la cruz a la cinchera[aclaración requerida]). Su cabeza es más ancha que larga, el cuello es ancho, no tiene cuernos, sus orejas son largas y el pelaje es oscuro. Esto se repite en la cara y en los miembros anterior y posterior desde las rodillas y garrones hasta las pezuñas, respectivamente. Los ojos están libres de lana. El largo de los miembros debe ser armónico con el cuerpo.'],

    ['EAST FRIESIAN', 'EF', 'light-green', 
    'La East Friesian es una raza de ovejas lecheras originarias de Frisia Oriental en el norte de Alemania Producción de El friso oriental produce aproximadamente 300-600 litros de leche, sobre una lactancia de 200 a 300 días. Hay informes de animales individuales con rendimiento de leche que alcanzan los 900 litros, contando la leche succionada por los corderos, así como el ordeño por máquina. Para proporcionar un alto rendimiento de leche, el ewe debe recibir una dieta de alta calidad. Otra atracción de la raza es un número promedio relativamente alto de corderos nacidos por ewe. Los frisos orientales se utilizan como una raza de ordeño de pura raza o como una raza travesía para otras ovejas ordeñadoras. Pueden aumentar el número promedio de corderos nacidos, así como la producción de leche, cuando se cruzan con otras razas de ovejas lechera. No son una raza muy resistente o adaptable, pero sus razas cruzadas pueden serlo. Cruzarlos con la raza Awassi ha sido un éxito notable en entornos mediterráneos o semiáridos. Los frisones orientales cruzados con la raza Lacaune han sido un éxito en el medio ambiente de Wisconsin. Los frisos orientales no se introdujeron en América del Norte hasta la década de 1990, pero desde entonces, debido a su alto rendimiento de leche, se han convertido rápidamente en la raza preferida entre los productores comerciales de leche de oveja, aunque generalmente no en forma de pura raza.'],

    ['PELIBUEY', 'PB', 'light-yellow', 
    'La pelibuey (también conocida como Cubano Rojo por la FAO u oveja de pelo canaria) es una raza de oveja doméstica nativa del Norte de África y de las Islas Canarias, llevada al Caribe y América Central por los españoles. La pelibuey es una raza de oveja que por lo general no cría lana (deslanada); esta adaptación la hace especialmente útil en regiones intertropicales donde las ovejas con lana no sobreviven. Los machos carecen de cuernos, al contrario que las ovejas de lana. Se trata de una raza criada especialmente en climas calurosos para el consumo de su carne y la obtención de estiércol de primera calidad.'],

    ['SUFFOLK', 'SF', 'lila', 
    'Suffolk es una raza de ovejas de cara negra, originaria de Inglaterra, es una raza multipropósito, criadas por su carne y por la lana, esta raza se logró con el cruce de la raza southdown y Norfolk Horn.  Son en su mayoría criadas para la producción de lana y carne, especialmente cuando son cruzadas con la progenie de una oveja Welsh Mountain. Por ejemplo, una oveja upland de raza pura como una oveja Welsh Mountain podría ser criada con un macho Bluefaced Leicester. Este será un Welsh Mule, uno de muchos diferentes tipos de ovejas hembras de raza media. El cordero producido cuando una oveja hembra de raza media es cruzada con un macho Suffolk (tanto como con otras razas como Texel, Beltex, o Charollais) es considerado ideal para la producción de carne por su buena conformación. El cordero tiene los beneficios de cuidado fácil de una oveja de montaña y el crecimiento excelente de un macho Suffolk. La raza Suffolk también es más resistente a la fotosensibilización causada por el consumo de Narthecium ossifragum. La luz del sol empeora la condición, pero las cabezas y orejas negras del Suffolk limitan la luz que llega a la piel.'],

    ['ROMNEY MARSH', 'RM', 'orange', 
    'Su origen es británico, se la cría con doble propósito, su vellón es de lana media, notable prolificidad, pudiendo en muchos casos ser mellicera, es robusta, puede vivir en zonas de mucha humedad, de climas templados. Los productores buscan ejemplares sin lana en la cara, sus vellones son semiabiertos y da mechas de puntas largas, el diámetro de las mismas es de 33 a 35 micrones, el peso de un macho desarrollado está entre los 85 y 90 kg y el peso de las hembras maduras es de 75 a 80 kg.'],

    ['DORSET', 'DO', 'sky-blue', 
    'El origen de la raza Dorset es en el sur de Inglaterra, en el Condado de Dorset y de Somerset, como consecuencia de una prolongada selección, a partir de razas muy antiguas de la región y no es consecuencia del cruzamiento con otras razas. a oveja Dorset es prolífica, produce abundante leche, posee longevidad y produce corderos fuertes de crecimiento y madurez mediana, con una canal con un desarrollo muscular importante. Se trata por lo tanto de una raza típica de doble propósito. Existe el tipo Dorset Down, derivada de la Hampshire Down mejorada con la Southdown; sin embargo su diferencia con la Hampshire Down es mínima. Se caracteriza por la mejor calidad de su lana. Su utilización ha disminuido en los últimos años.'],

    ['MORA', 'MR', 'violet', 
    'La oveja mora colombiana, se caracteriza por su color oscuro en el vellón, es más, algunas pueden dar crías con el vellón completamente negro, café o gris, vellones que son muy apreciados por el pequeño productor, pues el trabajarlos no necesita color y, de hecho, permanecerá así para toda la vida, a diferencia de la lana de otros ejemplares. El color negro recesivo es producido por dos pares de genes recesivos para el negro, cualquiera de los cuales, - un caso de homocigocidad - producirá ese color. De los machos, el reproductor orinal era un mora, con sangre 5/8 criollo negro y 3/8 corriedale, por tanto, se ha conservado la sangre de criollo con corriedale en los reproductores. La producción de carne y lana es bastante similar a la del criollo, pero la lana del moro tiene mayor grado de finura'],

    ['CHAROLLAIS', 'CL', 'yellow', 
    'Charollais es una raza de ovino, procedente de Francia, se originó en el año 1800. Se ha exportado a nivel internacional, y se utiliza comúnmente en el Reino Unido para producir corderos. Los machos, en la madurez, pesan 135 kg, y las hembras pesan 90 kg. La raza tiene buena protección para el frío. Usados como doble propósito, carne y Lana. Su cara es de color rosado, producen entre 2 y 2,5 kg de lana, las mechas miden hasta 6 cm, y su finura llega a las 60 micras.'],
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
