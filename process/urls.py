from django.urls import path
from . import views
app_name = 'process'


urlpatterns = [
    path('form/',views.process_form, name='form'),
    path('getcsrf/', views.get_csrf, name='getcsrf'),
]