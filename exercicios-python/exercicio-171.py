lista_a = [1,2,3,4,5,6,7]
lista_b = [1,2,3,4]

lista_soma = [x + y for x, y in zip(lista_a, lista_b)]
print(lista_soma)


#lista_soma = []

# def zipper(lista1, lista2):
#     intervalo = min(len(lista1), len(lista2))

#     for i in range(intervalo):
#         lista_soma.append(lista1[i] + lista2[i])
#     return(lista_soma)

    # if len(lista1) < len(lista2):
    #     for i, v in enumerate(lista1):
    #         lista_soma.append(lista1[i] + lista2[i])
    # else:
    #     for i, v in enumerate(lista2):
    #         lista_soma.append(lista2[i] + lista1[i])
    # return(lista_soma)

#print(zipper(lista_a, lista_b))