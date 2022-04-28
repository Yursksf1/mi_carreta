from django.contrib import admin
from myapp.models import Sheep, Breed, HistoryWeight, SheepPhoto, SheepBreed
from myapp.models import Group, SheepGroup, Service, HistorySheep
# Register your models here.
from django.utils import timezone
from datetime import datetime
import pytz
from tzlocal import get_localzone
from dateutil import relativedelta as rdelta
from django.urls import reverse
from django.utils.html import format_html
from datetime import date, timedelta



class RangeDayListFilter(admin.SimpleListFilter):
    # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = 'rago de dias'

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'range days'

    def lookups(self, request, model_admin):
        """
        Returns a list of tuples. The first element in each
        tuple is the coded value for the option that will
        appear in the URL query. The second element is the
        human-readable name for the option that will appear
        in the right sidebar.
        """
        return (
            ('C1', 'Cordero 1'),
            ('C2', 'Cordero 2'),
            ('B1', 'Borrego 1'),
            ('B2', 'Borrego 2'),
            ('OVEJA', 'Oveja'),
        )

    def queryset(self, request, queryset):
        """
        Returns the filtered queryset based on the value
        provided in the query string and retrievable via
        `self.value()`.
        """
        # Compare the requested value (either '80s' or '90s')
        # to decide how to filter the queryset.
        today = date.today()
        if self.value() == 'C1':
            date_delta = today - timedelta(days=90)
            return queryset.filter(
                birthday__gte=date_delta,
                birthday__lte=today,
            )
        if self.value() == 'C2':
            date_delta_1 = today - timedelta(days=180)
            date_delta_2 = today - timedelta(days=90)
            return queryset.filter(
                birthday__gte=date_delta_1,
                birthday__lte=date_delta_2,
            )
        if self.value() == 'B1':
            date_delta_1 = today - timedelta(days=270)
            date_delta_2 = today - timedelta(days=180)
            return queryset.filter(
                birthday__gte=date_delta_1,
                birthday__lte=date_delta_2,
            )
        if self.value() == 'B2':
            date_delta_1 = today - timedelta(days=360)
            date_delta_2 = today - timedelta(days=270)
            return queryset.filter(
                birthday__gte=date_delta_1,
                birthday__lte=date_delta_2,
            )
        if self.value() == 'OVEJA':
            date_delta = today - timedelta(days=360)
            return queryset.filter(
                birthday__lte=date_delta,
            )

from django.utils.safestring import mark_safe

class PhotoInline(admin.TabularInline):
    model = SheepPhoto
    fields = ('render_image', 'upload', 'is_principal' )
    readonly_fields = ("render_image",)
    extra = 0


    def render_image(self, obj):
        return mark_safe("""<img style="width: 60px; height: 50px;" src="{}" />""".format(obj.upload.url))

class MembershipInline(admin.TabularInline):
    model = SheepBreed
    extra = 0


class SheepGroupInline(admin.TabularInline):
    model = SheepGroup
    extra = 0


class SheepAdmin(admin.ModelAdmin):
    list_display = ('idd',  'imagen', 'identification_number', 'name', 'gender', 'age', 'nacimiento', 'breeds', 'parentDadId', 'parentMomId', 'active')
    list_filter = (RangeDayListFilter, 'active', 'gender' )
    search_fields = ('name', 'identification_number')
    inlines = [
        PhotoInline,
        MembershipInline,
        SheepGroupInline
    ]
    def imagen(self, obj):
        url = obj.get_absolute_url()
        url_img = '/static/img/sheep_default.jpg'

        if obj.prncipal_photo():
            url_img = obj.prncipal_photo().upload.url

        return format_html('<a href="{0}"><img style="width: 60px; height: 50px;" src="{1}" /></a>'.format(
            url,
            url_img
        ))

    def idd(self, obj):
        return str(obj.id)[:6]

    def age(self, obj):
        return obj.age()

    def nacimiento(self, obj):
        return obj.birthday.strftime("%Y/%m/%d")

    def breeds(self, obj):
        breeds = ''
        for breed in obj.breeds():
            if type(breed) == str:
                breeds = '{} {};'.format(breeds, breed)
            else:
                breeds = '{} {};'.format(breeds, breed.breed.name)
        return breeds

admin.site.register(Sheep, SheepAdmin)


class BreedAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    # fields = ('name', 'amount', 'category',  'active', 'description')
    search_fields = ('name', 'description')

admin.site.register(Breed, BreedAdmin)

# admin.site.register(SheepPhoto)
# admin.site.register(SheepBreed)


admin.site.register(Group)
# admin.site.register(SheepGroup)
admin.site.register(Service)
admin.site.register(HistorySheep)

