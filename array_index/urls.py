from django.urls import path

from . import views
from array_index import views


urlpatterns = [
    path('array/', views.gen, name='array_idex'),
    

]
