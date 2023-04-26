from django.conf import settings
from django.core.mail import send_mail


def handle_uploaded_file(emails, file_name): 
    # path += str(file_name)
    # path += '.txt'
    path = f'media\mail\{file_name}'  # путь сохранения файла с почтами 

    with open(path, 'wb+') as file:  # создаём файл и построчно добавляем почты
        for n in emails: 
            file.write(n)


def s_mail(text, file_name, user_email):
    path = f'media\mail\{file_name}'  # путь к файла с почтами

    with open(path, 'r') as file1:
        file = file1.readlines()  # читаем файл построчно 

        emails = []
        for line_text in file:  
            emails.append(line_text.strip())  # добавляем почты в список 

        # отправляем письмо 
        send_mail( 
            subject='Subject here',  # заголовок 
            message=text,  # текст письма
            from_email=user_email,  # имейл отправителя 
            recipient_list=emails,  # имейл получателей 
            fail_silently=False,
        )
