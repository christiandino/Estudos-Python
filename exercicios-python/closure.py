"""

Closure e funções que retornam outras funções

"""

###################################

# def carro():
#     print('Carro ligado...')
#     def acelerar(km):
#         return km
#     return acelerar

# status = carro()
# print(status(80))

###################################

# def criar_saudacao(saudacao):
#     def saudar(nome):
#         return f'{saudacao}, {nome}!'
#     return saudar

# falar_bom_dia = criar_saudacao("Bom dia")
# falar_boa_tarde = criar_saudacao("Boa tarde")
# # s3 = criar_saudacao("Boa noite")

# for nome in ['Maria', 'Joana', 'Luiz']:
#     print(falar_bom_dia(nome))
#     print(falar_boa_tarde(nome))

# print(s1('Luiz'))
# print(s2('Luiz'))
# print(s3('Luiz'))

# Crie funções que duplicam, triplicam e quadriplicam
# o número recebido como parâmetro

def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar
    
duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

print(duplicar(2))
print(triplicar(2))
print(quadruplicar(2))