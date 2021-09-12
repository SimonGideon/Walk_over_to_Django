from django import forms


class Contact(forms.Form):
    name = forms.CharFields()
    email = forms.Emailfield(label='E-Mail')
    category = forms.ChoiceField(choices=('question', 'Question'))
    subject = forms.CharField(required=False)
    body = forms.CharField(widget=forms.Textarea)
