# Desempacotamento em chamadas
# de métodos e funções

string = 'ABCD'
lista = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
tupla = 'Python', 'é', 'legal'

#a, b, c = lista

# a, b, c, *_ = lista
# print(a, c)
# p, b, *_, u = lista
# print(p, u)
# p, b, *_, ap, u = lista
# print(p, ap)

# for nome in lista:
#     print(nome, end=' ', sep=' ')

# print('Maria', 'Helena', 1, 2, 3, 'Eduarda')
# print(*lista)
# print(*string)
# print(*tupla)
# print(tupla)

salas = [
    # 0        1
    ['Maria', 'Helena', ], # 0
    # 0
    ['Elaine', ], # 1
    # 0       1       2
    [
    'Luiz', 
    'João', 
    'Eduarda'
    ]
]

#print(*salas, end='\n')
print(*salas, sep='\n')