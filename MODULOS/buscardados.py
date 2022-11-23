import requests
from bs4 import BeautifulSoup
from requests.auth import HTTPProxyAuth

cp = input("Digite seu cep: ")





request = requests.get(f'https://h-apigateway.conectagov.estaleiro.serpro.gov.br/api-cep/v1/consulta/cep/{cp}')



logradouro = (format(request['endereco']))
print(logradouro)
bairro = (format(request['bairro']))
print(bairro)
estado = (format(request['cidade']))
print(estado)
uf = (format(request['uf']))
print(uf)
