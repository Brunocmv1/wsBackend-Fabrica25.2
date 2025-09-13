from django.urls import path
from .views import Home, CreateAtores, ListAtores

urlpatterns = [
    path('', Home.as_view(), name="home"),
    path('criarAtores', CreateAtores.as_view(), name="create_a"),
    path('listarAtores', ListAtores.as_view(), name="list_a" ),

]