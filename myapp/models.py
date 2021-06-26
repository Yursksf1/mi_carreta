from django.db import models
import uuid

# Create your models here.


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
