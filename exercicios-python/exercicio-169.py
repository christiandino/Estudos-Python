# lista1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
# lista2 = ['BA', 'SP', 'MG', 'RJ']

# def zipper(lista1, lista2):
#     lista_geral = []
#     for i, v in enumerate(lista1):
#         lista_geral.append((lista1[i],lista2[i]))
#     return (lista_geral)

# def zipper(lista1, lista2):
#     return [(lista1[i], lista2[i]) for i, v in enumerate(lista1)]

# def zipper(lista1, lista2):
#     intervalo = min(len(lista1), len(lista2))
#     return [
#         (lista1[i], lista2[2]) for i in range(intervalo)
#     ]

# print(zipper(lista1, lista2))

# resultado esperado
#[('Salvador', 'BA'),('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]




lista1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
lista2 = ['BA', 'SP', 'MG', 'RJ']

lista_geral = []

for i, v in enumerate(lista1):
    lista_geral.append((lista1[i], lista2[i]))

print(lista_geral)
