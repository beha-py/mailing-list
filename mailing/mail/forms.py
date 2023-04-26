from django import forms

# форма на гл.странице
class SendMailForm(forms.Form):
    text = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите имя'}))  # поле "текст"
    file = forms.FileField()  # поле "файл"

