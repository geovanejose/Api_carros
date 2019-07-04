#Script para consumir API
#Linguagem utilizada : Python3
#Created by Jhonatas Rodrigues
#

import requests
import json
import os

# Request Area
data = requests.get('http://localhost:8000/api/carros')
binary = data.content
output = json.loads(binary)
# Menu Area
os.system('clear')
def menu():
        print("--> Bem vindo ao apipy 1.0 <--")
        print( "(Menu)")
        print( ">> Use (1) Para Ver Carros")
        print( ">> Use (2) Para Inserir Carros")
        print( ">> Use (3) Para Atualizar Carros")
        print( ">> Use (4) Para Deletar Carros")
        print( ">> Use (0) Para Abortar")
menu()
valor = input('Resposta :')
if valor == '1':
    os.system('clear')
    x = 0
    print("\n-----Carros encontrados-----\n")
    for item in output['data']:
        print('>> Id:',item['id'],'\n>> Nome: ', item['nome'], '\n>> Marca: ', item['marca'], '\n>>Modelo: ', item['modelo'], '\n>> Cor: ', item['cor'], '\n>>Ano: ', item['ano'], '\n>>Concessionaria :', item['concessionarias']['nome'],['pais'],['estado'],['cidade'],['logradouro'])
elif valor == '2' :
    os.system('clear')
    print(" >> Use (1) Concessionaria 1")
    print(" >> Use (2) Concessionaria 2")
    concessionaria = input('Digite o Número da Concessionaria: ')
    nome = input("Digite o Nome do Carro :")
    marca = input("Digite a marca do Carro :")
    modelo = input("Digite o modelo do Carro :")
    cor = input("Digite a cor do Carro :")
    ano = input("Digite o ano do Carro :")
    concessionaria = input("Digite a concessionaria do Carro :")
    requests.post('http://localhost:8000/api/carros', data = {'nome':nome, 'marca':marca,'modelo':modelo,'cor':cor,'ano':ano, 'concessionaria_id':concessionaria})
elif valor == '4':
    os.system('clear')
    print(" >> Use (1) Deletar Apenas Um Carro")
    print(" >> Use (2) Para Deletar Todos os Carros")
    print(" >> Use (0) Para Retornar ao Menu")
    resposta = input("Resposta :")
    if resposta == '1':
        carroId = input('Digite o Id do Carro :')
        requests.delete('http://localhost:8000/api/carros/' + carroId)
    elif resposta == '2':
        requests.delete('http://localhost:8000/api/carros')
    else :
        Menu()
elif valor == '3':
    os.system('clear')
    print(" >> Use (1) Concessionaria 1")
    print(" >> Use (2) Concessionaria 2")
    identifier = input('Digite o ID do Carro Que Você Deseja Alterar : ')
    concessionariaN = input('Nova Concessionaria: ')
    nome = input('Novo Nome : ')
    marca = input('Nova Marca : ')
    modelo = input('Nova Modelo : ')
    cor = input('Nova cor : ')
    ano = input('Novo Ano : ')
    requests.put('http://localhost:8000/api/carros/' + identifier , data = {'id': identifier, 'nome':nome, 'marca':marca,'modelo':modelo,'cor':cor,'ano':ano, 'concessionaria_id':concessionariaN})
else :
    print("By by :)")
#Percorrendo dados
