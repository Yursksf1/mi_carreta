"""Sheep forms."""

# Django
from django import forms

# Models
from .models import Sheep


class SheepForm(forms.ModelForm):
    """Sheep model form."""

    class Meta:
        """Form settings."""

        model = Sheep
        fields = ('identification_number', 'name', 'gender', 'birthday')
    
    identification_number_2 = forms.CharField(required=False)
    name = forms.CharField(required=False)
    active = forms.BooleanField(required=False)
