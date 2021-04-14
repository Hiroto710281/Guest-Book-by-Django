from django import forms

from .models import Greeting


class GreetingForm(forms.ModelForm):

    class Meta:
        model = Greeting
        fields = ('name', 'comment',)