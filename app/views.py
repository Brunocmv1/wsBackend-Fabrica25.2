from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DeleteView, DetailView
from .models import Ator, Filme
from .forms import AtorForm


class Home(TemplateView):
    template_name = "home.html"

class CreateAtores(CreateView):
    model = Ator
    form_class = AtorForm
    template_name = "createAtores.html"
    success_url = reverse_lazy("list_a")

class ListAtores(ListView):
    model = Ator
    template_name = "listAtores.html"
    context_object_name = "atores"

class UpdateAtores(UpdateView):
    model = Ator
    form_class = AtorForm
    template_name = "createAtores.html"
    success_url = reverse_lazy("list_a")

class DeleteAtores(DeleteView):
    model = Ator
    template_name = "deleteAtores.html"
    context_object_name = "ator"
    success_url = reverse_lazy("list_a")

class ListFilmes(ListView):
    model = Filme
    template_name = "listFilmes.html"
    context_object_name = "filmes"

class ListDetalhes(DetailView):
    model = Filme
    template_name = "listDetalhes.html"
    context_object_name = "filme"