from django.urls import path
from .views import Home, CreateAtores, ListAtores, UpdateAtores, DeleteAtores

urlpatterns = [
    path('', Home.as_view(), name="home"),
    path('criarAtores', CreateAtores.as_view(), name="create_a"),
    path('listarAtores', ListAtores.as_view(), name="list_a" ),
    path('atualizarAtores/<int:pk>', UpdateAtores.as_view(), name="update_a"),
    path('deletarAtores/<int:pk>', DeleteAtores.as_view(), name="delete_a"),

]