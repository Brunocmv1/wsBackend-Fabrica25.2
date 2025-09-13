from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Ator

class Home(TemplateView):
    template_name = "home.html"

class ListAtores(ListView):
    model = Ator
    template_name = "listAtores.html"
    context_object_name = "atores"

