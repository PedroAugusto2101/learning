"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

# def impar_ou_par(numero):
#     if numero // 1 == numero:
#         if numero % 2 == 0:
#             print("Par")
#         else:
#             print("Ímpar")
#     else:
#         print("Não inteiro")

# numero = input("Digite um número inteiro: ")
# impar_ou_par(numero)

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

# def time(hour):
#     if int(hour) >= 0 and int(hour) <=11:
#         print("Bom dia!")
#     elif int(hour) >= 12 and int(hour) <=17:
#         print("Bom tarde!")
#     elif int(hour) >= 18 and int(hour) <=23:
#         print("Bom noite!")

# hour = input("Digite a hora atual: ")
# time(hour)


"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

# def len_name(name):
#     if len(name) <= 4:
#         print("Your name is short")
#     elif len(name) >= 5 and len(name) <=6:
#         print("Your name is normal")
#     elif len(name) > 6:
#         print("Your name is very big")

# name = input("What is your name? ")
# len_name(name)