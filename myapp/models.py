from django.db import models
import uuid

from django.utils import timezone
from datetime import datetime
import pytz
from tzlocal import get_localzone
from dateutil import relativedelta as rdelta
# Create your models here.
from django.urls import reverse


class Sheep(models.Model):

    GENDER = [
        ("H", 'Hembra'),
        ("M", 'Macho'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    identification_number = models.fields.CharField(max_length=100)
    name = models.fields.CharField(max_length=100)
    description = models.fields.CharField(max_length=300)

    gender = models.CharField(
        max_length=1,
        choices=GENDER,
    )
    birthday = models.DateTimeField(auto_now_add=True)

    parentDadId = models.ForeignKey('Sheep', null=True, related_name='dad', on_delete=models.SET_NULL)
    parentMomId = models.ForeignKey('Sheep', null=True, related_name='mom', on_delete=models.SET_NULL)

    active = models.fields.BooleanField(default=True)

    def __str__(self):
        return self.name

    def breeds(self):
        breeds = SheepBreed.objects.filter(
            sheep=self
        )

        if not breeds.exists():
            return 'None'

        breeds = breeds.order_by('percent').all()

        return breeds[0].breed.name

    def age(self):
        local_tz = get_localzone()
        now = datetime.now(local_tz)
        birthday = self.birthday
        rd = rdelta.relativedelta(now, birthday)
        if rd.years:
            return "{0.years} Años {0.months} meses".format(rd)
        else:
            return "{0.months} meses, {0.days} dias".format(rd)


class Breed(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.fields.CharField(max_length=100)
    description = models.fields.CharField(max_length=300)

    def __str__(self):
        return self.name


class SheepBreed(models.Model):
    breed = models.ForeignKey(
        Breed,
        on_delete=models.CASCADE,
    )
    sheep = models.ForeignKey(
        Sheep,
        on_delete=models.CASCADE,
    )
    percent = models.DecimalField(max_digits=5, decimal_places=2)


class SheepPhoto(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sheep = models.ForeignKey(
        Sheep,
        on_delete=models.CASCADE,
    )
    upload = models.FileField(upload_to='media/')


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
