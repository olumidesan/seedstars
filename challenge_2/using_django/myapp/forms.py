from django import forms
from .models import Details

class NewDetailForm(forms.ModelForm):
    class Meta:
        model = Details
        fields = ('name', 'email_address')
        widgets = {
            'name':
            forms.TextInput(attrs={
                'class': 'input',
                'placeholder': "A name"
            }),
            'email_address':
            forms.EmailInput(attrs={
                'class': 'input',
                'placeholder': 'you@domain.com'
            }),
        }
