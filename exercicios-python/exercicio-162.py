# def soma(x, y):
#     return x + y

# def multiplica(x, y):
#     return x * y

# def criar_funcao(funcao, x):
#     def interna(y):
#         return funcao(x,y)
#     return interna

def titulo(str):
    return str.title()

def minusculo(frase):
    return frase.lower()




# def concatenar(primeira_frase, funcao = None):
#         def interna(segunda_frase): 
#             if funcao:  
#             #return (funcao(primeira_frase + ' ' + segunda_frase))
#                 return funcao(primeira_frase + ' ' + segunda_frase)
#             return (primeira_frase + ' ' + segunda_frase)
#         return interna




def concatenar(primeira_frase:str, funcao = None):
        def interna(segunda_frase:str): 
            frase = primeira_frase + ' ' + segunda_frase
            if funcao:
                 return funcao(frase)
            return frase
        return interna


def criar_funcao(funcao, x):
    def interna(y):
         return funcao(x + y)
    return interna
          
def verificar_str(frase):
    if type(frase) != str:
        raise TypeError(f'Por favor digite caracteres, voce digitou "{frase}"')

def concatenar(primeira_frase, funcao = None):
        verificar_str(primeira_frase)
        def interna(segunda_frase:str):
            verificar_str(segunda_frase) 
            frase = primeira_frase + ' ' + segunda_frase
            return funcao(frase) if funcao else frase
        return interna
    

variavel = concatenar('christian')
print(variavel(2))

# variavel = criar_funcao(titulo, 'christian')
# print(variavel('santos'))



# frase_nova = concatenar('10')
# print(frase_nova('Teste'))

# frase_nova = concatenar('CHRISTIAN', minusculo)
# print(frase_nova('SANTOS'))

#frase2 = concatenar(minusculo,'CHRISTIAN')
#print(frase2('SANTOS'))

# frase = concatenar(titulo,'christian')
# print(frase('santos'))



# soma_com_cinco = criar_funcao(soma, 5)
# multiplica_por_dez = criar_funcao(multiplica, 10)


# print(soma_com_cinco(10))
# print(multiplica_por_dez(10))

