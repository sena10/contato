from django.urls import path
from .views import detalhar, index

urlpatterns = [
    path('detalhar/', detalhar, name='detalhar'),
    path('index/', index, name='index'),

]