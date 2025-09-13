from django.urls import path
from .views import Home, ListAtores

urlpatterns = [
    path('', Home.as_view(), name="home"),
    path('listarAtores', ListAtores.as_view(), name="list_a" ),
]