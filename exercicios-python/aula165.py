# def criar_funcao(func):
#     def interna(*args, **kwargs):
#         for arg in args:
#             print(arg)
#             e_string(arg)
#         resultado = func(*args, **kwargs)
#         return resultado
#     return interna

# def inverte_string(string):
#     return string[::-1]

# def e_string(param):
#     if not isinstance(param, str):
#         raise TypeError('param deve ser uma string')

# inverte_string_checando_parametro = criar_funcao(inverte_string)
# invertida = inverte_string_checando_parametro('123')
# print(invertida)

def criar_funcao(func):
    def interna(*args, **kwargs):
        if args:
            for arg in args:
                e_string(arg)

        if kwargs:
            for kwarg in kwargs.values():
                e_string(kwarg)

        return func(*args, **kwargs)
    return interna

def inverte_string(*args, **kwargs):

    ab1 = [v[::-1] for v in args] if args else []
    ab2 = {k: v[::-1] for k, v in kwargs.items()} if kwargs else {}

    if args and kwargs:
        return ab1, ab2
    elif args:
        return ab1
    else:
        return ab2



def e_string(param):
    if not isinstance(param, str):
        raise TypeError('param deve ser uma string')


inverte_string_checando_parametro = criar_funcao(inverte_string)
lista = inverte_string_checando_parametro('alan', 'pereira', 'christian', valor="teste")
print(lista)


# dicionario = {'nome': 'alan', 
#               'sobrenome': 'pereira'}
# def teste(**kwargs):
#     novoDicionarioInvertido = {k: v[::-1]  for k, v in kwargs.items()}
#     return novoDicionarioInvertido


# print(teste(nome='alan', sobrenome='pereira'))