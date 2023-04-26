from django.urls import path

from companies.views import login, logout, registration

# urls пути к регистрации/логин/выхода 
app_name = 'companies'

urlpatterns = [
    path('registration/', registration, name='registration'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout')
]
