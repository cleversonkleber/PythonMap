import requests
import json
from itertools import chain
from collections import defaultdict

def  aip():
    url  = 'http://api.salic.cultura.gov.br/v1/projetos?format=json'
    r = requests.get(url=url)
    if r.status_code == 200:
        dados = json.loads(r.content.decode('utf8'))
    return dados
dados = aip()
teste =[]
for l in dados['_embedded']['projetos']:
    teste.append(l)

# dados

print([x for x in teste[0].keys()])
