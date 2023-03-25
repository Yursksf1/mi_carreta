from django.db import models
import uuid

from django.utils import timezone
from datetime import datetime
import pytz
from tzlocal import get_localzone
from dateutil import relativedelta as rdelta
# Create your models here.
from django.urls import reverse
from django.utils.timezone import now
from django.db.models import Q


class Sheep(models.Model):

    GENDER = [
        ("H", 'Hembra'),
        ("M", 'Macho'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    identification_number = models.fields.CharField(max_length=100, null=True, blank=True,  verbose_name="Id 1")
    identification_number_2 = models.fields.CharField(max_length=100, null=True, blank=True,  verbose_name="Id 2")
    name = models.fields.CharField(max_length=100, null=True, blank=True, verbose_name="Nombre")
    description = models.fields.CharField(max_length=300, null=True, blank=True, verbose_name="Descripción")

    gender = models.CharField(
        max_length=1,
        choices=GENDER,
         verbose_name="Genero",
    )
    birthday = models.DateTimeField(default=now, editable=True,  verbose_name="Nacimiento")

    parentDadId = models.ForeignKey('Sheep', null=True, blank=True, related_name='dad', on_delete=models.SET_NULL, verbose_name="Padre Id")
    parentMomId = models.ForeignKey('Sheep', null=True, blank=True,  related_name='mom', on_delete=models.SET_NULL, verbose_name="Madre Id")

    active = models.fields.BooleanField(default=True)

    def __str__(self):
        return self.full_name()

    def full_name(self):
        if self.identification_number_2:
            return '{} - {} ({})'.format(self.identification_number, self.name, self.identification_number_2)

        return '{} - {}'.format(self.identification_number, self.name)

    def breed_name(self):
        breeds = SheepBreed.objects.filter(
            sheep=self
        )

        if not breeds.exists():
            return None

        breeds = breeds.order_by('percent').all()

        return breeds[0].breed.name

    def breeds(self):
        breeds = SheepBreed.objects.filter(
            sheep=self
        )

        if not breeds.exists():
            return 'None'

        breeds = breeds.order_by('percent').all()

        return breeds

    def weight(self):
        weight = HistoryWeight.objects.filter(
            sheep=self
        )

        if not weight.exists():
            return 'N/A'

        weight = weight.order_by('-create_at').first()

        return '{} kg'.format(str(weight.weight)[:-1])


    def last_weight(self):
        weight = HistoryWeight.objects.filter(
            sheep=self
        )

        if not weight.exists():
            return 'N/A'

        weight = weight.order_by('-create_at').first()

        return '{}'.format(str(weight.weight)[:-1])

    def last_weight_comparative(self):
        result = "no cambia"
        weight = HistoryWeight.objects.filter(
            sheep=self
        )

        if not weight.exists():
            return result

        weight_list = weight.order_by('-create_at').all()
        if len(weight_list) == 1:
            return "sube"

        weight_new = weight_list[0]
        weight_anterior = weight_list[1]
        if weight_new.weight == weight_anterior.weight:
            result = "no cambia"
        elif weight_new.weight > weight_anterior.weight:
            result = "sube"
        elif weight_new.weight < weight_anterior.weight:
            result = "baja"

        return result


    def last_body_condition(self):
        body_condition = HistoryBodyCondition.objects.filter(
            sheep=self
        )

        if not body_condition.exists():
            return 'N/A'

        body_condition = body_condition.order_by('-create_at').first()

        return '{}'.format(str(body_condition.body_condition)[:-1])


    def last_famacha(self):
        famacha = HistoryFamacha.objects.filter(
            sheep=self
        )

        if not famacha.exists():
            return 'N/A'

        famacha = famacha.order_by('-create_at').first()

        return '{}'.format(str(famacha.famacha)[:-1])

    def age(self):
        local_tz = get_localzone()
        now = datetime.now(local_tz)
        birthday = self.birthday
        rd = rdelta.relativedelta(now, birthday)
        if rd.years:
            name_year = 'años'
            name_months = 'meses'
            if rd.years == 1:
                name_year = 'año'

            if rd.months == 1:
                name_months = 'mes'

            return "{0.years} {name_year} {0.months} {name_months}".format(
                rd,
                name_year=name_year,
                name_months=name_months
            )

        else:
            name_months = 'meses'
            name_days = 'días'
            if rd.months == 1:
                name_months = 'mes'

            if rd.days == 1:
                name_days = 'día'
            return "{0.months}  {name_months}, {0.days} {name_days}".format(
                rd,
                name_months=name_months,
                name_days=name_days
            )

    def prncipal_photo(self):
        sheep_photo = SheepPhoto.objects.filter(
            sheep=self, is_principal=True
        )

        if not sheep_photo.exists():
            return None

        sheep_photo = sheep_photo.first()

        return sheep_photo

    def children(self):
        sheep = None
        if self.gender == 'H':
            sheep = Sheep.objects.filter(
                parentMomId=self
            )
        elif self.gender == 'M':
            sheep = Sheep.objects.filter(
                parentDadId=self
            )
        else:
            sheep = Sheep.objects.filter(
                Q(parentMomId=self) |
                Q(parentDadId=self)
            )

        if not sheep.exists():
            return []

        sheeps = sheep.order_by('birthday').all()

        return sheeps

    def get_absolute_url(self):
        return reverse('app:detail', kwargs={'pk': str(self.id)} )
    
    class Meta:
        verbose_name = "Oveja"
        verbose_name_plural = "Ovejas"

class Breed(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.fields.CharField(max_length=100, verbose_name="Nombre")
    acronym = models.fields.CharField(max_length=100, verbose_name="Acronimo")
    color = models.fields.CharField(max_length=100)
    description = models.fields.CharField(max_length=300, verbose_name="Descripción")

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Raza"
        verbose_name_plural = "Razas"

class Group(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.fields.CharField(max_length=100, verbose_name="Nombre")
    slug = models.SlugField(max_length=100, default="")
    active = models.fields.BooleanField(default=True, verbose_name="Activo")
    description = models.fields.CharField(max_length=300, verbose_name="Descripción")

    def count(self):
        sh = SheepGroup.objects.filter(group_id=self.id).all()
        return len(sh)


    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Grupo"
        verbose_name_plural = "Grupos"

class SheepBreed(models.Model):
    breed = models.ForeignKey(
        Breed,
        on_delete=models.CASCADE,
        related_name='sheep',
         verbose_name="Raza"
    )
    sheep = models.ForeignKey(
        Sheep,
        on_delete=models.CASCADE,
        related_name='breed',
        verbose_name="Oveja"
    )
    percent = models.DecimalField(max_digits=5, decimal_places=2,  verbose_name="Porcentaje")

    def __str__(self):
        return '{} - {} - {}'.format(self.sheep, self.percent, self.breed.name)
    class Meta:
        verbose_name = "Oveja Raza"
        verbose_name_plural = "Ovejas Razas"

class SheepGroup(models.Model):
    group = models.ForeignKey(
        Group,
        on_delete=models.CASCADE,
        related_name='sheep',
        verbose_name="Grupo"
    )
    sheep = models.ForeignKey(
        Sheep,
        on_delete=models.CASCADE,
        related_name='group',
        verbose_name="Oveja"
    )
    date_start = models.DateTimeField(auto_now_add=True)
    date_end = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return '{} - {}'.format(self.sheep, self.group)
    class Meta:
        verbose_name = "Oveja Grupo"
        verbose_name_plural = "Ovejas Grupos"

class Service(models.Model):
    sheep_hembra = models.ForeignKey(
        Sheep,
        on_delete=models.CASCADE,
        related_name='service_hembra'

    )
    sheep_macho = models.ForeignKey(
        Sheep,
        on_delete=models.CASCADE,
        related_name='service_macho'

    )
    date_start = models.DateTimeField(default=now, editable=True)
    date_end = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return '{} - {} - {}'.format(self.sheep_macho.name, self.sheep_hembra.name, self.date_start)


class Mancha(models.Model):
    service = models.ForeignKey(
        Service,
        on_delete=models.CASCADE,
        related_name='service_hembra'

    )
    date_start = models.DateTimeField(default=now, editable=True)
    def __str__(self):
        return '{} - {}'.format(self.date_start, self.service)


class SheepPhoto(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sheep = models.ForeignKey(
        Sheep,
        on_delete=models.CASCADE,
        verbose_name="Oveja"
    )
    upload = models.FileField(upload_to='media/', verbose_name="Grupo")
    create_at = models.DateTimeField(auto_now_add=True)
    is_principal = models.fields.BooleanField(default=True, verbose_name="es principal?")

    def __str__(self):
        return '{} - {}'.format(self.sheep, self.is_principal)

    def take_ago(self):
        local_tz = get_localzone()
        now = datetime.now(local_tz)
        create_at = self.create_at
        rd = rdelta.relativedelta(now, create_at)
        if rd.years:
            return "{0.years} Años {0.months} meses".format(rd)
        else:
            return "{0.months} meses, {0.days} dias".format(rd)

    class Meta:
        ordering = ['-is_principal']
        verbose_name = "Foto Oveja"
        verbose_name_plural = "Fotos Oveja"

class Observations(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sheep = models.ForeignKey(
        Sheep,
        on_delete=models.CASCADE,
        verbose_name="Oveja"
    )
    description = models.fields.CharField(max_length=100, verbose_name="Descripción")
    active = models.fields.BooleanField(default=True, verbose_name="Activo")
    create_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Observacion"
        verbose_name_plural = "Observaciones"

class HistorySheep(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sheep = models.ForeignKey(
        Sheep,
        on_delete=models.CASCADE,
        verbose_name="Oveja"
    )
    description = models.fields.CharField(max_length=500, verbose_name="Descripción")
    create_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['-create_at']
        verbose_name = "Historico Oveja"
        verbose_name_plural = "Historicos Oveja"

class HistoryFamacha(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    sheep = models.ForeignKey(
        Sheep,
        on_delete=models.CASCADE,
    )
    famacha = models.DecimalField(max_digits=7, decimal_places=2)
    create_at = models.DateTimeField(default=now, editable=True)


class HistoryBodyCondition(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    sheep = models.ForeignKey(
        Sheep,
        on_delete=models.CASCADE,
    )
    body_condition = models.DecimalField(max_digits=7, decimal_places=2)
    create_at = models.DateTimeField(default=now, editable=True)


class HistoryWeight(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    sheep = models.ForeignKey(
        Sheep,
        on_delete=models.CASCADE,
    )
    weight = models.DecimalField(max_digits=7, decimal_places=1)
    create_at = models.DateTimeField(default=now, editable=True)

    def get_conversion(self):
        number = 0
        all_w = HistoryWeight.objects.filter(sheep=self.sheep).all().order_by("create_at").all()
        index = list(all_w).index(self)
        indice_anterior = index - 1
        if indice_anterior < 0:
            return 0

        w2 = all_w[indice_anterior]

        diff_w = self.weight-w2.weight
        diff_d = (self.create_at-w2.create_at).days

        if diff_w == 0 or diff_d==0:
            return 0

        number = (diff_w/diff_d) * 1000
        return round(number, 0)


    class Meta:
        ordering = ['create_at']

class HistoryWeather(models.Model):
    LOCATION = [
        ("N", 'Nevera'),
        ("L", 'Laboratorio'),
        ("A", 'Aprisco'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    humidity = models.DecimalField(max_digits=7, decimal_places=2)
    temperature = models.DecimalField(max_digits=7, decimal_places=2)

    create_at = models.DateTimeField(auto_now_add=True)

    location = models.CharField(
        max_length=1,
        choices=LOCATION,
    )


class HistoryPluviometer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    measure = models.PositiveIntegerField()
    create_at = models.DateField()