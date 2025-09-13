from django import forms
from .models import Ator

class AtorForm(forms.ModelForm):
    class Meta:
        model = Ator
        fields = ["nome", "idade", "nacionalidade"]
