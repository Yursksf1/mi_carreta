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
        route='sheeps_with_weigh',
        view=views.SheepsFeedView.as_view(template_name='sheep_list_with_weights.html'),
        name='feed_with_weight'
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
    ),
    path(
        route='sheep/<uuid:pk>/history',
        view=views.SheepDetailHistoryView.as_view(),
        name='detail_history'
    ),
    path(
        route='sheep/<uuid:pk>/weigh',
        view=views.SheepWeighView.as_view(),
        name='add-weigh'
    ),

    path(
        route='observations',
        view=views.ObservationsView.as_view(),
        name='observations'
    ),
    path(
        route='observations/<uuid:pk>/check',
        view=views.observations_check,
        name='check-observations'
    ),
    path('acciones_bloque/', TemplateView.as_view(template_name="acciones_bloque.html"), name='acciones_bloque'),

    ## ACCIONES EN BLOQUE

    path(
        route='acciones_bloque/pluviometer/download',
        view=views.pluviometer_download,
        name='pluviometer_download'
    ),
    path(
        route='acciones_bloque/pluviometer/import',
        view=views.pluviometer_import,
        name='pluviometer_import'
    ),

    path(
        route='acciones_bloque/weather/download',
        view=views.weather_download,
        name='weather_download'
    ),
    path(
        route='acciones_bloque/weather/import',
        view=views.weather_import,
        name='weather_import'
    ),
    path(
        route='acciones_bloque/weight/download',
        view=views.weight_download,
        name='weight_download'
    ),
    path(
        route='acciones_bloque/weight/import',
        view=views.weight_import,
        name='weight_import'
    ),
    path(
        route='acciones_bloque/weights/download',
        view=views.weights_download,
        name='weights_download'
    ),
    path(
        route='acciones_bloque/weights/import',
        view=views.weights_import,
        name='weights_import'
    ),
    path(
        route='acciones_bloque/sheep/download',
        view=views.sheep_download,
        name='sheep_download'
    ),
    path(
        route='acciones_bloque/sheep/import',
        view=views.sheep_import,
        name='sheep_import'
    ),
    path(
        route='acciones_bloque/sheep_breeds/download',
        view=views.sheep_breeds_download,
        name='sheep_breeds_download'
    ),
    path(
        route='acciones_bloque/sheep_breeds/import',
        view=views.sheep_breeds_import,
        name='sheep_breeds_import'
    ),

]
