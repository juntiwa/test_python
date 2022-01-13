from django.urls import path

from . import views
from factorial import views


urlpatterns = [
    path('factorial/', views.createForm, name='input'),
    path('fac/',views.fact,name='show')
    
]
