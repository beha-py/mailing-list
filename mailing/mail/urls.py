from django.urls import path

from mail.views import main

app_name = 'mail'

urlpatterns = [
    path('', main, name='main')  # путь до сервиса отправки почты ../mail/ 
]
