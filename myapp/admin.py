from django.contrib import admin
from myapp.models import Sheep, Breed, HistoryWeight, SheepPhoto, SheepBreed
# Register your models here.
from django.utils import timezone
from datetime import datetime
import pytz
from tzlocal import get_localzone
from dateutil import relativedelta as rdelta

class SheepAdmin(admin.ModelAdmin):
    list_display = ('id', 'identification_number', 'name', 'gender', 'age', 'birthday', 'breeds', 'parentDadId', 'parentMomId', 'active')
    # fields = ('name', 'amount', 'category',  'active', 'description')
    list_filter = ('active', 'gender', 'birthday')
    search_fields = ('name', 'identification_number')

    def age(self, obj):
        return obj.age()

    def breeds(self, obj):
        return obj.breeds()

admin.site.register(Sheep, SheepAdmin)


class BreedAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    # fields = ('name', 'amount', 'category',  'active', 'description')
    search_fields = ('name', 'description')

admin.site.register(Breed, BreedAdmin)

admin.site.register(SheepPhoto)
admin.site.register(SheepBreed)