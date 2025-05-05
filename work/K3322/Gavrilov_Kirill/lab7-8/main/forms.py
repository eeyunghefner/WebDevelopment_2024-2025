from django import forms

SCORE_CHOICES = [(i, str(i)) for i in range(4)]
SERVICE_CHOICES = [
    ('www', 'Интернет'),
    ('city', 'Реклама в городе'),
    ('friend', 'Посоветовали друзья'),
]


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label='Имя')
    surname = forms.CharField(max_length=100, label='Фамилия')
    email = forms.EmailField(label='Email')
    message = forms.CharField(widget=forms.Textarea, label='Ваш комментарий')
    score = forms.ChoiceField(
        label="Ваша оценка сайта:",
        choices=SCORE_CHOICES,
        widget=forms.RadioSelect,
        required=False
    )

    service = forms.MultipleChoiceField(
        label="Где вы увидели информацию о нашем сайте?",
        choices=SERVICE_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=False
    )


