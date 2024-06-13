"""

Listas em Python
Tipo list - Mutável
Métodos úteis:
    append, insert, pop, del, clear, extend, +
Create, Read, Update, Delete
Criar, Ler, alterar, apagar = lista[i] (CRUD)

"""

lista = [10, 20, 30, 40, 50, 60, 70]
lista[2] = 300
del lista[2]
print(lista)
lista.append(50)
lista.append(60)
lista.append(70)
lista.pop()
ultimo_valor = lista.pop(3)
print(lista, 'Removido, ', ultimo_valor)
lista.append('Luiz')
nome = lista.pop()
lista.append(1233)
del lista[-1]
lista.clear()
lista.insert(0, 5) # primeiro coloca em qual indice, e depois o valor
print(lista)
lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b
lista_d = lista_a.extend(lista_b) # incluiu valores dentro da lista_a
print(lista_a)
lista = ['Maria', 'Helena', 'Luiz']
for i, j in enumerate(lista):
    print(i, j)
indices = range(len(lista))
for indice in indices:
    print(indice, lista[indice], type(lista[indice]))
