def mostrar_menu():
    print("\nOpções:")
    print("1. Adicionar item à lista")
    print("2. Remover item da lista")
    print("3. Mostrar lista de compras")
    print("4. Sair")

def adicionar_item(lista):
    item = input("Digite o nome do item para adicionar: ")
    lista.append(item)
    print(f"{item} foi adicionado à lista.")

def remover_item(lista):
    try:
        index = int(input("Digite o número do item que deseja remover: ")) - 1
        if 0 <= index < len(lista):
            item = lista.pop(index)
            print(f"{item} foi removido da lista.")
        else:
            print("Índice inválido.")
    except ValueError:
        print("Por favor, insira um número válido.")
    except IndexError:
        print("Índice fora dos limites da lista.")

def mostrar_lista(lista):
    if lista:
        print("\nSua lista de compras:")
        for i, item in enumerate(lista, 1):
            print(f"{i}. {item}")
    else:
        print("Sua lista de compras está vazia.")

def main():
    lista_de_compras = []
    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            adicionar_item(lista_de_compras)
        elif opcao == '2':
            remover_item(lista_de_compras)
        elif opcao == '3':
            mostrar_lista(lista_de_compras)
        elif opcao == '4':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
