from django.urls import path

# importing views from views..py
from myapp import views

app_name = "app"
urlpatterns = [
    path('weather_today', views.weather_today),
    path('', views.WeatherFormView.as_view()),
]