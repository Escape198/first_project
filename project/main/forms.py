from django import forms
from django.core import validators

class NameForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Enter your email again!')
    text = forms.CharField(widget=forms.Textarea,
    validators=[validators.MaxLengthValidator(500)])

def clean(self):
    cleaned_data = super().clean()
    email = cleaned_data['email']
    vmail = cleaned_data['verify_email']

    if email != vmail:
        raise forms.ValidationError('Make shure email match')
    return cleaned_data
