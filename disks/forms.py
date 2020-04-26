from django import forms


class RechercheForm(forms.Form):
    con = forms.CharField(max_length=200)

