"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""

nome = input("Digite o seu nome: ")
idade = input("Digite a sua idade: ")

if nome and idade:
    print(f"\nSeu nome é {nome}\n")
    print(f"Seu nome invertido é {nome[::-1]}\n")

    if ' ' in nome:
        print(f"Seu nome contém espaços\n")
    else:
        print(f"Seu nome não contém espaços\n")
    print(f"Seu nome tem {len(nome)} letras\n")
    print(f"A primeira letra do seu nome e {nome[0]}\n")
    print(f"A última letra do seu nome e {nome[-1]}\n")
else:
    print("Desculpe, você deixou campos vazios.")