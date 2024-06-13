"""

Lista de listas e seus índices

"""

salas = [
    # 0        1
    ['Maria', 'Helena', ], # 0
    # 0
    ['Elaine', ], # 1
    # 0       1       2
    [
    'Luiz', 
    'João', 
    'Eduarda'#, 
    # (0,10,20,30,40),
    # {
    # 'Dic':150,
    # 'Ruas': [
    #             '23 de Outubro', 
    #             'Mesquita',
    #             'Afrânio'
    #         ]
    # }
], # 2
]

# print(salas[1][0])
# print(salas[0][1])
# print(salas[2][2])
# print(salas[2][3][2])
# print(salas[2][4]['Dic'])
# print(salas[2][4]['Rua'])
#print(salas[2][4]['Ruas'])
# for nomes in enumerate(salas[2][4]['Ruas']):
#     print(nomes)

for sala in salas:
    print(f'A sala é {sala}')
    for aluno in sala:
        print(aluno)
