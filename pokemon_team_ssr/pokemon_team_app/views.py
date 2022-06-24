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
        "base_poke" : {
                "base_poke_type": response_json["types"][0]["type"]["name"],
                "base_poke_image_url": response_json["sprites"]["front_default"]
            },
        "support_poke" : []
    }
    typeurl = response_json["types"][0]["type"]["url"]
    r = requests.get(f'{typeurl}')
    response_json = r.json();
    support_poke = response_json["pokemon"]
    for i in range(1, 5):
        randnum = random.randint(0, len(support_poke) - 1)
        support_poke_url = support_poke[randnum]["pokemon"]["url"]
        r = requests.get(f'{support_poke_url}')
        response_json = r.json()
        
        poke_data["support_poke"].append({ "name": response_json["name"], "image_url": response_json["sprites"]["front_default"]})
    print(poke_data)
    return render(request, 'pages/index.html', poke_data)
