lista = []

def adicionar_item(item):
    lista.append(item)
    print("item adicionado.")
def remover_item(item):
    if item in lista:
        lista.remove(item)
        print("item removido!")
    else:
        print(" item nao encontrado!")
    

while True:
    print("1 - adicionar")
    print('2 - remover')
    print("3 - exibir")
    print("4 - sair")

    escolha = input("escolha uma opção:\n")

    if escolha == "1":
        item = input("digite o item a ser adicionado:\n ")
        adicionar_item(item)
    elif escolha == "2":
        print(lista)
        item = input("digite o item a ser removido:\n ")
        remover_item(item)
    elif escolha == "3":
        print(lista)
    elif escolha == "4":
        break
    else:
        print("Esse número é invalido.")