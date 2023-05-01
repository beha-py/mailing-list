from django import forms

# форма на гл.странице
class SendMailForm(forms.Form):
    subject = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите заголовок'}))  # поле "заголовок"
    text = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите имя'}))  # поле "текст"
    file = forms.FileField()  # поле "файл"

