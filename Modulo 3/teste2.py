lista_compras = []

while True:
    print ("Selecione uma opção")
    opcao = input("[i]nserir [a]pagar [l]istar [s]air: ")

    if opcao == "i":
        lista_compras.append(input("Qual o nome do item que você deseja inserir? "))
    elif opcao == "a":
        try:
            posicao_item_remover = int(input("Qual o índice do item que você deseja apagar: "))
            item_remover = lista_compras[posicao_item_remover]
            lista_compras.remove(item_remover)
        except:
            print("Não foi possivel apagar esse índice.")
    elif opcao == "l":
        if len(lista_compras) > 0:
            for indice, nome in enumerate(lista_compras):
                print(indice, nome)
        else:
            print("Não há itens na lista.")
    elif opcao == "s":
        break
    else:
        print("Opção Inválida!")