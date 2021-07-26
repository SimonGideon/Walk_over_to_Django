from django import forms
from .models import Sales


class SForm(forms.ModelForm):
    class Meta:
        model = Sales
        fields = [
            'title',
            'description',
            'price'
        ]
class RawSalesForm(forms.Form):
    title = forms.CharField()
    description = forms.CharField()
    price = forms.DecimalField()