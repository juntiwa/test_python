from django.urls import path

from . import views
from send.views import send_email_api

urlpatterns = [
    path('sendemail/', send_email_api, name='send_email'),
]
