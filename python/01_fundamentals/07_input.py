# nome = input('Qual o seu nome? ')
# print(f'O seu nome é {nome}') {nome=} mostra o nome da variável também

# numero_1 = int(input('Digite um número: ')) -> não é uma boa prática pois o usuário pode por uma letra
# e já quebrar o programa sem ter como checar o valor dessa variável

numero_1 = input('Digite um número: ')
numero_2 = input('Digite outro número: ')

int_numero_1 = int(numero_1)
int_numero_2 = int(numero_2)

print(f'A soma dos números é: {int_numero_1 + int_numero_2}')