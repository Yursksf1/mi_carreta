from django.urls import path

# importing views from views..py
from myapp import views
from django.views.generic import TemplateView

app_name = "app"
urlpatterns = [
    path('demo/', TemplateView.as_view(template_name="demo.html")),

    path('weather/today', views.weather_today, name='weather-today'),
    path('weather/history', views.weather_history, name='weather-history'),
    path('weather/add', views.WeatherCreateView.as_view(), name='weather-add'),
    path('', views.dashboard, name='dashboard'),


    path(
        route='sheeps',
        view=views.SheepsFeedView.as_view(),
        name='feed'
    ),

    path(
        route='sheep/new/',
        view=views.CreateSheepView.as_view(),
        name='create'
    ),

    path(
        route='sheep/<uuid:pk>/',
        view=views.SheepDetailView.as_view(),
        name='detail'
    )
]
