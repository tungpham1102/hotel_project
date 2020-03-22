from django import forms

GENDER_CHOICES = (
        ('male', 'male'),
        ('female', 'female')
    )


class CheckoutForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    birthday = forms.DateField()
    gender = forms.ChoiceField(widget=forms.RadioSelect, choices = GENDER_CHOICES)
    phone = forms.IntegerField()