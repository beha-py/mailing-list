from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic.base import TemplateView

from mail.forms import SendMailForm
from mail.logic import handle_uploaded_file, s_mail


# Create your views here.
class IndexView(TemplateView):
    template_name = 'mail/index.html'  # вывод шаблона на страницу с описанием сервиса


def main(request):
    if request.method == 'POST':  # если запрос POST
        form = SendMailForm(request.POST, request.FILES)  # форма 
        if form.is_valid():  # если форма заполнена правильно
            file_name = request.FILES['file'].name  # из файла который отправил пользователь берём имя
            user_email = request.user.email  # имейл пользователя

            handle_uploaded_file(request.FILES['file'], file_name)  # save txt file with emails
            s_mail(request.POST['text'], file_name, user_email)  # send_mails

            return HttpResponseRedirect(reverse('mail:main'))  # отправляем на гл.страницу
    else:
        form = SendMailForm()  # если запрос не POST то выводит обычную форму

    return render(request, 'mail/main.html', {'form': form})
