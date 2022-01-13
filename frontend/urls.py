from django.urls import path, include

from . import views
 
urlpatterns = [
    path('', views.home, name='home'),
    path('', include('todo.urls')),
    path('',include('send.urls')),
    path('', include('factorial.urls')),
   
    
]
