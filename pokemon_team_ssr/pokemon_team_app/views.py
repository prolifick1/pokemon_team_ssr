from django.shortcuts import render
import requests
import os
from requests_oauthlib import OAuth1
import random
from dotenv import load_dotenv
# Create your views here.
load_dotenv()
def index(request):
    randnum = random.randint(1, 100)
    r = requests.get(f'https://pokeapi.co/api/v2/pokemon/{randnum}')
    response_json = r.json()
    poke_data = {
        'name' : response_json["types"][0]["type"]["name"],
        'image_url': response_json["sprites"]["front_default"]
    }
    return render(request, 'pages/index.html', poke_data)
