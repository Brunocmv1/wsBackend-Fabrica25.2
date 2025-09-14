from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DeleteView, DetailView
from .omdb_client import buscar_filme_por_titulo
from django.urls import reverse_lazy, reverse
from django.shortcuts import render, redirect
from .forms import AtorForm, FilmeForm
from .models import Ator, Filme

#//--CRUD dos filmes

#Direciona para o template home que tem o input de pesquisa
class Home(TemplateView):
    template_name = "home.html"

#O form do input retorna o metodo get ao apertar buscar enviando o titulo do filme
def ShowFilme(request):
    titulo = request.GET.get("titulo").strip() #Pega o resultado do input retirando o uso de espaços no inicio ou no final
    dados = None
    if titulo:
        dados = buscar_filme_por_titulo(titulo) #referenciando a função do arquivo de config. do omdb ele manda o titulo recebido como parâmetro
    return render(request, "showFilme.html", {"dados": dados})

#Na pagina do filme ao clicar em salvar o form do template retorna post pegando as informações da API
def CriarFilme(request):
    if request.method == "POST":
        titulo = request.POST.get("titulo")
        ano_lancamento = request.POST.get("ano_lancamento")
        sinopse = request.POST.get("sinopse")

        if titulo:
            Filme.objects.get_or_create(titulo=titulo, #Faz com que o usuario não adicione mais de um filme igual
                defaults={"ano_lancamento": ano_lancamento,
                "sinopse": sinopse})
        return redirect(reverse("list_f"))
    return redirect(reverse("home"))

#Lista os filmes salvos
class ListFilmes(ListView):
    model = Filme
    template_name = "listFilmes.html"
    context_object_name = "filmes"

#Ao clicar em "ℹ️" na pagina listar filme abre uma pagina onde mostra sinopse e atores associados do filme
class ListDetalhes(DetailView):
    model = Filme
    template_name = "listDetalhes.html"
    context_object_name = "filme"

#Dentro de detalhes ao clicar no "🗑️" retorna um post com o id do ator e exclui
def DeleteAtorFilme(request, pk):
    filme = Filme.objects.get(pk=pk)

    if request.method == "POST":
        idAtor = request.POST.get("idAtor")
        ator = Ator.objects.get(pk=idAtor)
        filme.atores.remove(ator)
        return redirect("delete_af", pk=filme.id) 
    
    return render(request, "listDetalhes.html", {"filme": filme})

#Em detalhes ao clicar em "✏️", o user é direcionado pra uma lista de atores para associar um ator cadastrado no sistema
def UpdateFilmes(request, pk):
    filme = Filme.objects.get(pk=pk)

    if request.method == "POST":
        idAtor = request.POST.get("idAtor")
        if idAtor:
            ator = Ator.objects.get(pk=idAtor)
            filme.atores.add(ator)
            return redirect("update_f", pk=filme.id)

    atoresFilme = filme.atores.all() 
    atoresNfilme = Ator.objects.exclude(id__in = atoresFilme.values_list("id", flat=True)) #Evita de mostrar atores ja cadastrados na lista pra adicionar

    return render(request, "updateFilmes.html", {"filme": filme, "atoresnfilme": atoresNfilme})

#Ao clicar "🗑️" na pagina da lista, ele direciona para uma pagina de confirmação junto com a pk e apaga
class DeleteFilme(DeleteView):
    model = Filme
    template_name = "deleteFilmes.html"
    context_object_name = "filme"
    success_url = reverse_lazy("list_f")

#//--CRUD dos atores

#Pergunta ao usuario nome, idade e nacionalidade do ator
class CreateAtores(CreateView):  
    model = Ator
    form_class = AtorForm
    template_name = "createAtores.html"
    success_url = reverse_lazy("list_a")

#Lista os atores
class ListAtores(ListView):
    model = Ator
    template_name = "listAtores.html"
    context_object_name = "atores"

#Na pagina de listar atores o botao "✏️" direciona pro form do ator via pk
class UpdateAtores(UpdateView):
    model = Ator
    form_class = AtorForm
    template_name = "createAtores.html"
    success_url = reverse_lazy("list_a")

#Na mesma lista no botão "🗑️" direciona para pagina de confirmação junto com a pk, que retorna metodo post e exclui
class DeleteAtores(DeleteView):
    model = Ator
    template_name = "deleteAtores.html"
    context_object_name = "ator"
    success_url = reverse_lazy("list_a")












