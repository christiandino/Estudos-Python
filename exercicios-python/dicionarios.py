pessoa = {
    'nome': 'Luiz Otávio',
    'sobrenome': 'Miranda',
    'idade': 18,
    'altura': 1.8,
    'endereços': [
        {'rua': 'tal tal', 'numero': 123},
        {'rua': 'outra rua', 'numero': 321}
    ]
}

for chave in pessoa:
    print(chave, pessoa[chave])

# pessoa = {}

# chave = 'nome'

# pessoa[chave] = 'Luiz Otávio'
# pessoa['sobrenome'] = 'Miranda'

# print(pessoa[chave])

# pessoa[chave] = 'Maria'

# #del pessoa['sobrenome']

# print(pessoa)
# print(pessoa['nome'])

# if pessoa.get('sobrenome') is None:
#     print('Não existe')
# else:
#     print(pessoa['sobrenome'])

