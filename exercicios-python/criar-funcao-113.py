# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variavel e mostre o valor
# da variavel

# crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar

def multiplicacao(*args):
    total = 1
    for i in args:
        total *= i
    return(total)

print(multiplicacao(5,6,2,3)) #180


def impar_par(numero):
    return 'par' if numero % 2 == 0 else 'impar'
        
print(impar_par(6))