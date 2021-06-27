from django.urls import path

# importing views from views..py
from myapp import views

app_name = "app"
urlpatterns = [
    path('weather/today', views.weather_today, name='weather-today'),
    path('weather/history', views.weather_history, name='weather-history'),
    path('weather/add', views.WeatherCreateView.as_view(), name='weather-add'),
]