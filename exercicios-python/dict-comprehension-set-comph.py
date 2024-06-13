produto = {
    'nome': 'Canela Azul',
    'preco': 2.5,
    'categoria': 'Escritório',
}

# print(produto.items())
# for chave, valor in produto.items():
#     print(chave, valor)

# dc = {
#     chave: valor.upper()
#     if isinstance(valor, str) else valor
#     for chave, valor
#     in produto.items()
# }

# print(dc)

# dc = {
#     chave: valor
#     if isinstance(valor, (int, float)) else valor.upper()
#     for chave, valor
#     in produto.items()
# }

# print(dc)

# dc = {
#     chave: valor.upper()
#     if isinstance(valor, str) else valor
#     for chave, valor
#     in produto.items()
#     if chave != 'categoria'
# }

# print(dc)

lista = [
    ('a', 'valor a'),
    ('b', 'valor a'),
    ('c', 'valor a'),
]

# dc = {
#     chave: valor
#     for chave, valor in lista
# }

print(dict(lista))
#print(dc)

s1 = {i ** 2 for i in range(10)}
print(s1)
