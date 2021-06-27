from django.shortcuts import render

# Create your views here.
from django.views.generic.edit import FormView
from myapp.models import HistoryWeather
from myapp.serializers import HistoryWeatherSerialize
from datetime import date
from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse

IMAGEN_LOCATION = {
    'N': 'img/nevera.png',
    'L': 'img/laboratorio.png',
    'A': 'img/aprisco.png',
}

def weather_today(request):
    weathers_today = []

    for locations in HistoryWeather.LOCATION:
        current_weather = HistoryWeather.objects.filter(
            location=locations[0],
            create_at__day=date.today().day,
            create_at__year=date.today().year,
            create_at__month=date.today().month,
        ).first()

        serializer = HistoryWeatherSerialize(current_weather)
        current_weather = serializer.data
        current_weather['location'] = locations[1]
        current_weather['image_location'] = IMAGEN_LOCATION.get(locations[0])
        weathers_today.append(current_weather)


    print('weathers_today', weathers_today)
    return render(
        request,
        'weather_today.html',
        {
            'weathers_today': weathers_today,
        }
    )


def weather_history(request):
    nevera_date = []
    nevera_data = []
    laboratorio_date = []
    laboratorio_data = []
    aprisco_date = []
    aprisco_data = []

    query = HistoryWeather.objects.filter(
        location='N'
    )
    if query.exists():
        results = query.order_by('create_at').all()[:100]
        for result in results:
            nevera_date.append(str(result.create_at.date()))
            nevera_data.append(float(result.temperature))

    query = HistoryWeather.objects.filter(
        location='L'
    )
    if query.exists():
        results = query.order_by('create_at').all()[:100]
        for result in results:
            laboratorio_date.append(str(result.create_at.date()))
            laboratorio_data.append(float(result.temperature))

    query = HistoryWeather.objects.filter(
        location='A'
    )
    if query.exists():
        results = query.order_by('create_at').all()[:100]
        for result in results:
            aprisco_date.append(str(result.create_at.date()))
            aprisco_data.append(float(result.temperature))
    print(nevera_date)
    print(aprisco_data)
    return render(
        request,
        'weather_history.html',
        {
            'nevera_date': nevera_date,
            'nevera_data': nevera_data,

            'laboratorio_date': laboratorio_date,
            'laboratorio_data': laboratorio_data,

            'aprisco_date': aprisco_date,
            'aprisco_data': aprisco_data,
        }
    )


class WeatherCreateView(CreateView):
    template_name = 'weather_form.html'
    model = HistoryWeather
    fields = ['humidity', 'temperature', 'location']

    def get_success_url(self):
        return reverse('app:weather-today')
