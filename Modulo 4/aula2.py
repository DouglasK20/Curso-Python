def soma(x, y, z): # Esta linha define a função 'soma' com 3 parâmetros
    print(f'x={x} y={y} z={z}', '|', 'x + y + z =', x + y + z) # Esta linha imprime os valores dos parâmetros e a soma deles
    
soma(1, 2, 3)  # Esta linha chama a função 'soma' com 3 argumentos
soma(1, y=2, z=5) # Esta linha chama a função 'soma' com 1 argumento posicional e 2 argumentos nomeados