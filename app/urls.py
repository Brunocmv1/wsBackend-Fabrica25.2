from django.urls import path
from .views import Home, CreateAtores, ListAtores, UpdateAtores, DeleteAtores, ListFilmes, ListDetalhes, UpdateFilmes, DeleteAtorFilme, ShowFilme, CriarFilme, DeleteFilme

urlpatterns = [
    path('', Home.as_view(), name="home"),
    path('mostrarFilme/', ShowFilme, name="show_f"),
    path('deletarFilme/<int:pk>/', DeleteFilme.as_view(), name="delete_f"),
    path("criarFilme/", CriarFilme, name="create_f"),
    path('criarAtores/', CreateAtores.as_view(), name="create_a"),
    path('listarAtores/', ListAtores.as_view(), name="list_a" ),
    path('atualizarAtores/<int:pk>/', UpdateAtores.as_view(), name="update_a"),
    path('deletarAtores/<int:pk>/', DeleteAtores.as_view(), name="delete_a"),
    path('listarFilmes/', ListFilmes.as_view(), name="list_f"),
    path('listarDetalhes/<int:pk>/', ListDetalhes.as_view(), name="list_d"),
    path('atualizarFilmes/<int:pk>/atores/', UpdateFilmes, name="update_f"),
    path('deletarAtorFilme/<int:pk>/', DeleteAtorFilme, name="delete_af")
]