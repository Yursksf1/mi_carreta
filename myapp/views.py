from django.shortcuts import render

# Create your views here.
from myapp.forms import WeatherForm
from django.views.generic.edit import FormView
from myapp.models import HistoryWeather
from myapp.serializers import HistoryWeatherSerialize
from datetime import date

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
        weathers_today.append(current_weather)


    print('weathers_today', weathers_today)
    return render(
        request,
        'weather_today.html',
        {
            'weathers_today': weathers_today,
        }
    )


class WeatherFormView(FormView):
    template_name = 'weather_form.html'
    form_class = WeatherForm
    success_url = '/weather_today/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.save()
        return super().form_valid(form)