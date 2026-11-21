# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 19:30:23 2026

@author: Diogo Costa
"""

import requests
url = "https://jsonplaceholder.typicode.com/users"
try:
    resposta = requests.get(url, timeout=10)
    resposta.raise_for_status()
    utilizadores = resposta.json()
    print("Total de utilizadores:", len(utilizadores))
    for pessoa in utilizadores:
        print(pessoa["name"], "-", pessoa["email"])
except requests.exceptions.RequestException as erro:
    print("Não foi possível consultar a API:", erro)
    

import csv
with open("utilizadores.csv", "w", newline="", encoding="utf-8-sig") as ficheiro:
    escritor = csv.DictWriter(ficheiro, fieldnames=["nome", "email"], delimiter=";")
    escritor.writeheader()
    for pessoa in utilizadores:
        escritor.writerow({"nome": pessoa["name"], "email": pessoa["email"]})
print("CSV de utilizadores criado")




# PARTE B - DESAFIO AUTÓNOMO: Opção A - Filtro de utilizadores
print("\n" + "-"*32)
print("\tPesquisa de Utilizadores")
print("-"*32)
pesquisa = input("Introduza o nome (ou parte do nome): ").lower()

encontrados = []
for pessoa in utilizadores:
    if pesquisa in pessoa["name"].lower():
        encontrados.append(pessoa)

if len(encontrados) == 1:
    print(f"\nFoi encontrado {len(encontrados)} resultado:")
    for p in encontrados:
        print(f"- {p['name']} ({p['email']})")
elif len(encontrados) > 1:
    print(f"\nForam encontrados {len(encontrados)} resultados:")
    for p in encontrados:
        print(f"- {p['name']} ({p['email']})")
else:
    print("\nNenhum utilizador encontrado.")