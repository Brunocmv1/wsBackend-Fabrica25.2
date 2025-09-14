from django.conf import settings
import requests

def buscar_filme_por_titulo(titulo):
    url = "http://www.omdbapi.com/" #Define a url base da API
    params = {"apikey": settings.OMDB_API_KEY, "t": titulo} #Coleta a key e coloca o t (metodo de pesquisa da API)
    resposta = requests.get(url, params=params)

    return resposta.json()
