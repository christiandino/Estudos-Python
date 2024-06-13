# pessoa = {
#     'nome': 'Luiz Otávio',
#     'sobrenome': 'Miranda 3',
#     'idade': 900,
# }

# pessoa.setdefault('idade', 0)

# print(pessoa['idade'])
#print(pessoa.__len__()) #para saber quantas chaves tem dentro do dict

# print(len(pessoa))
# print(tuple(pessoa.keys()))
# print(list(pessoa.values()))
# print(list(pessoa.items()))
# print()

# for chave in pessoa.keys():
#     print(chave)

# for chave in pessoa.values():
#     print(chave)

# for chave, valor in pessoa.items():
#     print(chave, valor)


##############################
##############################
# import copy

# d1 = {
#     'c1': 1,
#     'c2': 2,
#     'l1': [0,1,2],
# }

# #d2 = d1
# #d2 = copy.copy(d1)
# #d2 = copy.deepcopy(d1)

# d2 = d1.copy()

# d2['c1'] = 1000
# d2['l1'][1] = 999999

# print(d1)
# print(d2)

##############################
##############################

p1 = {
    'nome':'Luiz',
    'sobrenome':'Miranda',
}

#print(p1.get('nome'))

# fazendo com o que ele pegue o conteudo, e tire a chave nome de p1
#nome = p1.pop('nome') 

# fazendo com que ele tire a ultima chave inserida
#ultima_chave = p1.popitem()

#print(ultima_chave)
#print(nome)

# p1.update({
#     'nome': 'novo valor',
#     'idade': 30,
# })

#p1.update(nome='novo valor', idade=30)

#tupla = (('nome', 'novo valor'), ('idade', 30))
# lista = [['nome', 'novo valor'], ['idade', 30]]
# p1.update(lista)
# #p1.update(tupla)
# print(p1)




