# List comprehensio é uma forma rápida para criar listas
# a partir de iteráveis.
import pprint

def p(v):
    pprint.pprint(v, sort_dicts=False, width=40)

#print(list(range(10)))
# lista = []
# for numero in range(10):
#     lista.append(numero)
# # print(lista)

# #lista = [numero for numero in range(10)]
# lista = [
#     numero * 2
#     for numero in range(10)
# ]
#print(lista)

###############################################

# Mapeamento de dados em list comprehension
# produtos = [
#     {'nome': 'p1', 'preco': 20, },
#     {'nome': 'p2', 'preco': 10, },
#     {'nome': 'p3', 'preco': 30, },
# ]

# novos_produtos = [
#     #produto['preco']
#     #{'nome': produto['nome'], 'preco': produto['preco']}
#     {**produto, 'preco': produto['preco'] * 1.05} 
#     if produto['preco'] > 20 else {**produto}
#     for produto in produtos
# ]
# #print(novos_produtos)
# print(*novos_produtos, sep='\n')

###############################################

# Filter
# produtos = [
#     {'nome': 'p1', 'preco': 20, },
#     {'nome': 'p2', 'preco': 10, },
#     {'nome': 'p3', 'preco': 30, },
# ]

# novos_produtos = [
#     #produto['preco']
#     #{'nome': produto['nome'], 'preco': produto['preco']}
#     {**produto, 'preco': produto['preco'] * 1.05} 
#     if produto['preco'] > 20 else {**produto}
#     for produto in produtos
#     if (produto['preco'] >= 20 and produto['preco'] * 1.05) > 10
# ]
#print(novos_produtos)
#print(*novos_produtos, sep='\n')
#pprint.pprint(novos_produtos, sort_dicts=False, width=40)
#p(novos_produtos)

#lista = [n for n in range(10) if n < 5]
#print(lista)

#p(novos_produtos)

###############################################

# List comprehension com mais de um for

# lista = []
# for x in range(3):
#     for y in range(3):
#         lista.append((x,y))

# lista = [
#     (x,y) 
#     for x in range(3)
#     for y in range(3)
# ]
# lista = [
#     [letra for letra in 'Luiz']
#     for x in range(3)
# ]

# print(lista)

###################################
# # # # # # # TREINO # # # # # # # 
###################################

# numeros = [1,2,3,4,5,6,7,8,9,10]
# novos_numeros = [numero for numero in numeros if numero > 5]
# impares = [numero for numero in numeros if numero % 2 != 0]
# pares = [numero for numero in numeros if numero % 2 == 0]
# outro_if = [
#     numero
#     if numero != 6 else 600
#     for numero in pares
# ]

# print(numeros)
# print(novos_numeros)
# print(impares)
# print(pares)
# print(outro_if)

#####################################
####### FOR LINHAS E COLUNAS ########
##################################### 

# linhas_e_colunas = [
#     (x, y)
#     if y != 2 else (x *1000, y*1000)
#     for x in range(1, 11)
#     for y in range(1, 6)
#     if x != 2
# ]
# print(linhas_e_colunas)

######################################
######################################
######################################

# string = 'Otávio Miranda'
# numero_de_letras = 2
# nova_string = '.'.join([
#     string[indice:indice + 2]
#     for indice in range(0, len(string), numero_de_letras)
# ])
# print(nova_string)

######################################
######################################
######################################

nomes = ['luiz', 'maria', 'helena', 'joana', 'felipe']
novos_nomes = [
    f'{nome[:-1].lower()}{nome[-1].upper()}'
    for nome in nomes
]
#print(novos_nomes) 
# ['luiZ', 'mariA', 'helenA', 'joanA', 'felipE']

######################################
######################################
######################################

numeros = [[numero, numero ** 2] for numero in range(10)]
flat = [y for x in numeros for y in x]
print(numeros)
print(flat)