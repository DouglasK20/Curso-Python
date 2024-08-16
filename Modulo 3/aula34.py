# condicao = True

# while condicao:
#     nome = input('Qual o seu nome: ')
#     print(f'Seu nome é {nome}')

#     if nome == 'sair':
#         break

# print('Acabou')

# Continue faz a função de pular.

contador = 0

while contador <=100:
    contador += 1

    if contador == 6:
        print('Não vou mostrar o 6.')
        continue

    print(contador)

    if contador == 40:
        break