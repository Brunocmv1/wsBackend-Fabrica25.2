from django import forms
from .models import Ator, Filme

class AtorForm(forms.ModelForm):
    class Meta:
        model = Ator
        fields = ["nome", "idade", "nacionalidade"]

class FilmeForm(forms.ModelForm):
    class Meta:
        model = Filme
        fields = ["titulo", "ano_lancamento", "sinopse"]