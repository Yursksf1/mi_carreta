from django.contrib import admin
from myapp.models import Sheep, Breed, HistoryWeight
# Register your models here.
from django.utils import timezone
from datetime import datetime
import pytz
from tzlocal import get_localzone
from dateutil import relativedelta as rdelta

class SheepAdmin(admin.ModelAdmin):
    list_display = ('id', 'identification_number', 'name', 'gender', 'age', 'birthday', 'parentDadId', 'parentMomId', 'active')
    # fields = ('name', 'amount', 'category',  'active', 'description')
    list_filter = ('active', 'gender', 'birthday')
    search_fields = ('name', 'identification_number')

    def age(self, obj):
        local_tz = get_localzone()
        now = datetime.now(local_tz)
        birthday = obj.birthday
        rd = rdelta.relativedelta(now, birthday)
        if rd.years:
            return "{0.years} Años {0.months} meses".format(rd)
        else:
            return "{0.months} meses, {0.days} dias".format(rd)

admin.site.register(Sheep, SheepAdmin)


class BreedAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    # fields = ('name', 'amount', 'category',  'active', 'description')
    search_fields = ('name', 'description')

admin.site.register(Breed, BreedAdmin)
