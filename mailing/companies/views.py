from django.contrib import auth
# from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import HttpResponseRedirect, render
from django.urls import reverse

from companies.forms import UserLoginForm, UserRegistrationForm


# регистрация - если запрос POST, то проверяет форму на валидность, после сохраняет в БД
def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            # messages.success(request, "You've successfully registered!")
            return HttpResponseRedirect(reverse('companies:login'))
    else:
        form = UserRegistrationForm()


    context = {'form': form}

    return render(request, 'companies/registration.html', context=context)


# логин - если запрос POST, то проверяет форму на валидность, после берёт имя пользователя и пароль и авторизует через auth()
# и проверяет на наличии в БД
def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('mail:main'))
    else:
        form = UserLoginForm
    context = {'form': form}

    return render(request, 'companies/login.html', context=context)

# выход пользователя через auth.logout()
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))
        