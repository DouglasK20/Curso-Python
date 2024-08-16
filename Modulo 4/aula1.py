# def saudacao(nome='Sem Nome'):  # Esta é uma definição de função para 'saudacao' com um parâmetro padrão 'nome' definido como 'Sem Nome'
#     print(f'Olá, {nome}!')  # Esta linha imprime uma mensagem de saudação com o valor de 'nome'

# saudacao('Douglas')  # Esta linha chama a função 'saudacao' com o argumento 'Douglas'

# ================================================================================================================

def multiplo_de(numero, multiplo):  # Esta é uma definição de função para 'multiplo_de' que recebe dois parâmetros 'numero' e 'multiplo'
    resultado = numero % multiplo == 0  # Esta linha verifica se 'numero' é divisível por 'multiplo' e atribui o resultado a 'resultado'
    print(f'{numero} é múltiplo de {multiplo}?', end=' ')  # Esta linha imprime os números sendo verificados para divisibilidade
    print(resultado)  # Esta linha imprime o resultado da verificação de divisibilidade
 
 
multiplo_de(16, 8)  # Esta linha chama a função 'multiplo_de' com os argumentos 16 e 8
multiplo_de(15, 3)  # Esta linha chama a função 'multiplo_de' com os argumentos 15 e 3
multiplo_de(10, 2)  # Esta linha chama a função 'multiplo_de' com os argumentos 10 e 2