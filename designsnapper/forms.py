from django import forms
from designsnapper.models import Greeting

class CreateGreetingForm(forms.ModelForm):
    class Meta:
        model = Greeting
        exclude = ['author', 'date']