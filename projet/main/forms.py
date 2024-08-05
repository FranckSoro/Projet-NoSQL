from django import forms
from .models import Ouvrage


class OuvrageForm(forms.ModelForm):
    class Meta:
        model = Ouvrage
        fields = ['titre', 'date_publication', 'auteur', 'categorie']