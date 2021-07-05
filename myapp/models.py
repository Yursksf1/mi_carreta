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
    identification_number = models.fields.CharField(max_length=100)
    identification_number_2 = models.fields.CharField(max_length=100)
    name = models.fields.CharField(max_length=100)
    description = models.fields.CharField(max_length=300)

    gender = models.CharField(
        max_length=1,
        choices=GENDER,
    )
    birthday = models.DateTimeField(default=now, editable=True)

    parentDadId = models.ForeignKey('Sheep', null=True, related_name='dad', on_delete=models.SET_NULL)
    parentMomId = models.ForeignKey('Sheep', null=True, related_name='mom', on_delete=models.SET_NULL)

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

        return '{} Kg'.format( str(weight.weight)[:-1])

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


class Breed(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.fields.CharField(max_length=100)
    acronym = models.fields.CharField(max_length=100)
    color = models.fields.CharField(max_length=100)
    description = models.fields.CharField(max_length=300)

    def __str__(self):
        return self.name


class SheepBreed(models.Model):
    breed = models.ForeignKey(
        Breed,
        on_delete=models.CASCADE,
        related_name='sheep'
    )
    sheep = models.ForeignKey(
        Sheep,
        on_delete=models.CASCADE,
        related_name='breed'

    )
    percent = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return '{} - {} - {}'.format(self.sheep, self.percent, self.breed.name)

class SheepPhoto(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sheep = models.ForeignKey(
        Sheep,
        on_delete=models.CASCADE,
    )
    upload = models.FileField(upload_to='media/')
    create_at = models.DateTimeField(auto_now_add=True)
    is_principal = models.fields.BooleanField(default=True)

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

class HistoryWeight(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    sheep = models.ForeignKey(
        Sheep,
        on_delete=models.CASCADE,
    )
    weight = models.DecimalField(max_digits=7, decimal_places=2)
    create_at = models.DateTimeField(auto_now_add=True)


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
