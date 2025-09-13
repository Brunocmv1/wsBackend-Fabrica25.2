import requests
from django.conf import settings

def buscar_filme_por_titulo(titulo):
    url = "http://www.omdbapi.com/"
    params = {"apikey": settings.OMDB_API_KEY, "t": titulo}
    resposta = requests.get(url, params=params)
    
    return resposta.json()
