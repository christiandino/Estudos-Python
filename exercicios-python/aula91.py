"""
Faça uma lista de compras com listas
O usuário deve ter a possibilidade de 
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com
erros de índices inexistentes na lista

"""
import os
lista = []
indice = 0

while True:
    print('Selecione uma opção')
    print('Digite "sair" para fechar o programa')
    opcao = input(f'[i]nserir [a]pagar [l]istar: ')

    if opcao != 'i' and opcao != 'a' and opcao != 'l':
        os.system('cls')
        if opcao == 'sair':
            break
        else:
            print('Por favor digite uma opção valida')
        continue

    if opcao == 'i':
        os.system('cls')
        item = input(f'Valor: ')
        while len(item) == 0:
            digitado = input('Digite pelo menos um caractere: ')
            if len(digitado) == 0:
                continue
            else:
                lista.append(digitado)
                break
        else:
            lista.append(item)

    elif opcao == 'a':
        os.system('cls')
        if len(lista) == 0:
            print('Lista Vazia')
        else:
            try:
                indice = int(input('Digite o indice do item na lista: '))
                lista.pop(indice)
                print('Item retirado da lista')
            except:
                print('Este indice não consta na lista')

    elif opcao == 'l':
        os.system('cls')
        if len(lista) == 0:
            print('Lista vazia')
        else:
            for i, j in enumerate(lista):
                print(str(i) + " - " + j)