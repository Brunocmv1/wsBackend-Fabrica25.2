from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DeleteView, DetailView
from .omdb_client import buscar_filme_por_titulo
from .models import Ator, Filme
from .forms import AtorForm, FilmeForm


class Home(TemplateView):
    template_name = "home.html"

def ShowFilme(request):
    titulo = request.GET.get("titulo", "").strip()
    dados = None
    if titulo:
        dados = buscar_filme_por_titulo(titulo)
    return render(request, "showFilme.html", {"dados": dados})

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

def UpdateFilmes(request, pk):
    filme = Filme.objects.get(pk=pk)

    if request.method == "POST":
        idAtor = request.POST.get("idAtor")
        if idAtor:
            ator = Ator.objects.get(pk=idAtor)
            filme.atores.add(ator)
            return redirect("update_f", pk=filme.id)

    atoresFilme = filme.atores.all() 
    atoresNfilme = Ator.objects.exclude(id__in = atoresFilme.values_list("id", flat=True))

    return render(request, "updateFilmes.html", {"filme": filme, "atoresfilme": atoresFilme, "atoresnfilme": atoresNfilme})

def DeleteAtorFilme(request, pk):
    filme = Filme.objects.get(pk=pk)

    if request.method == "POST":
        idAtor = request.POST.get("idAtor")
        ator = Ator.objects.get(pk=idAtor)
        filme.atores.remove(ator)
        return redirect("delete_af", pk=filme.id)
    
    return render(request, "listDetalhes.html", {"filme": filme})


