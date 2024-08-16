"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""

numero = input('Informe um número: ')

try:
    numero_float = float(numero)
    print('Float:', numero_float)
    print(f'O dobro de {numero} é {numero_float * 2:.f}')
except:
    print('Isso não é um numero')