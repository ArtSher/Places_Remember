from django.forms import ModelForm
from .models import Remember
from django import forms


class RememberModels(ModelForm):
    class Meta:
        model = Remember
        fields = ('address', 'comment')
        labels = {'address': 'Место', 'comment': 'Воспоминание'}
        widgets = {
            'addres': forms.TextInput(attrs={'placeholder': 'Место'})
        }