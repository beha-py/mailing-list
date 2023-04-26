from django.contrib import admin
from django.urls import include, path

from mail.views import IndexView

# пути urls
urlpatterns = [
    path('admin/', admin.site.urls),  # админка 
    path('mail/', include('mail.urls', namespace='mail')),  # основной функционал: отправка почты
    path('companies/', include('companies.urls', namespace='companies')),  # регистрация/логин компаний
    path('', IndexView.as_view(), name='index')  # приветствие 
]
