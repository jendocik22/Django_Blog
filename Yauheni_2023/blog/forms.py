from django import forms


class CommentForm(forms.Form):
    # поле для ввода автора
    author = forms.CharField(
        max_length=60,
        widget = forms.TextInput({
            'class':'form-control',
            'placeholder': 'Ваше имя'
        }) # виджет-аргумент, кторый отвечает за вывод автора
    )
    # тело комментариря
    body = forms.CharField(
        widget=forms.Textarea({ #  можно вводить много текста
            'class': 'form-control',
            'placeholder': 'Ваш комментарий'
        })
    )