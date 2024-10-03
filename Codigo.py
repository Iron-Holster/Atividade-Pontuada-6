"""
Integrantes da dupla:
- Victor Andrade Costa Pinto
- Fabrício Silvany de Jesus
"""

import os
os.system("cls || clear") 
from dataclasses import dataclass

lista_pessoas = []
lista_salarios = []
lista_idade = []

#Contador
quantidade_pessoas = 0
quantidade_mulheres_renda_alta = 0

@dataclass 
class Pessoa:
    nome: str
    idade: int
    genero: str
    salario: float

#Banco de dados
nome_do_arquivo = "pesquisa_habitantes.txt"

while True:
    opcao = int(input("""
    1 || Adicionar pessoa
    2 || Exibir dados
    3 || Sair
    """))
    os.system("cls || clear")

    

    match (opcao):
        case 1:

            pessoa = Pessoa(
            nome = input("Digite seu nome: "),
            idade = int(input("Digite sua idade: ")),
            genero = input("Digite seu gênero (M ou F): ").upper(),
            salario = float(input("Digite seu salário: "))
            )
            os.system("cls || clear")

            lista_pessoas.append(pessoa)
            lista_idade.append(pessoa.idade)
            lista_salarios.append(pessoa.salario)

            if pessoa.genero == "F" and pessoa.salario >= 5000:
                quantidade_mulheres_renda_alta += 1

            quantidade_pessoas += 1

            #Abrindo arquivo
            with open(nome_do_arquivo, "a") as arquivo_pessoas:
                for pessoa in lista_pessoas:
                    arquivo_pessoas.write(f"Nome: {pessoa.nome}, Idade: {pessoa.idade}, Gênero: {pessoa.genero}, Renda mensal: {pessoa.salario}\n")
            
            print("Dados salvos.")

        case 2:
            print("=== DADOS ARMAZENADOS ===")
            for pessoa in lista_pessoas:
              print(f"Nome: {pessoa.nome}")
              print(f"Idade: {pessoa.idade}")
              print(f"Gênero: {pessoa.genero}")
              print(f"Salário: {pessoa.salario}\n")

        case 3:
            break


print(f"""
Média de salário do grupo: {sum(lista_salarios)/quantidade_pessoas:.2}
Maior idade registrada: {max(lista_idade)}
Menor Idade registrada: {min(lista_idade)}
Quantidade de mulheres com salário a partir de 5 mil reais: {quantidade_mulheres_renda_alta}
""")