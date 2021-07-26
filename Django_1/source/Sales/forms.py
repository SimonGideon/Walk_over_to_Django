from django import forms
from .models import Sales


class SForm(forms.ModelForm):
    class Meta:
        model = Sales
        fields = [
            'title',
            'description',
            'price',
            'summary',
            'featured',
        ]
