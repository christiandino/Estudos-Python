# aumente o preço dos produtos a seguir em 10%
# gere novos_produtos por deep copy (cópia profunda)

# import copy

# from dados import produtos

# novos_produtos = [
#     {**p, 'preco': round(p['preco'] * 1.1, 2)} 
#     for p in copy.deepcopy(produtos)
# ]
# # print(*produtos, sep='\n')
# # print()
# # print(*novos_produtos, sep='\n')

# produtos_ordenados_por_nome = sorted(
#     copy.deepcopy(produtos),
#     key= lambda p:p['nome'],
#     reverse= True
# )

# # print(*produtos, sep='\n')
# # print()
# # print(*produtos_ordenados_por_nome, sep='\n')

# produtos_ordenados_por_preco = sorted(
#     copy.deepcopy(produtos_ordenados_por_nome),
#     key=lambda p:p['preco']
# )

# # print(*produtos, sep='\n')
# # print()
# # print(*produtos_ordenados_por_preco, sep='\n')

# print(*produtos, sep='\n')
# print()
# print(*novos_produtos, sep='\n')
# print()
# print(*produtos_ordenados_por_nome, sep='\n')
# print()
# print(*produtos_ordenados_por_preco, sep='\n')

################################
################################

import copy

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

novos_produtos = produtos.copy()
for i in novos_produtos:
    i['preco'] = (i['preco']) * 1.10

print(*novos_produtos, sep='\n')
print()
produtos_ordenados_por_nome = (novos_produtos).copy()
produtos_ordenados_por_nome = sorted(
    produtos_ordenados_por_nome,
    key=lambda produto: produto['nome'],
    reverse=True
)
print(*produtos_ordenados_por_nome, sep='\n')
print()

produtos_ordenados_por_preco = produtos_ordenados_por_nome.copy()
produtos_ordenados_por_preco = sorted(
    produtos_ordenados_por_preco,
    key=lambda preco: preco['preco']
)

print(*produtos_ordenados_por_preco, sep='\n')
print()

