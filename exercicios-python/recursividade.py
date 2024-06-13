# def recursiva(inicio = 0, fim = 10):
#     print(inicio, fim)
#     # Caso base
#     if inicio >= fim:
#         return fim

#     # Caso recursivo
#     # contar até chegar ao final
#     inicio += 1
#     return recursiva(inicio, fim)

# print(recursiva())

def factorial(n):
    if n == 1 or n == 0:
        return 1
    
    return n * factorial(n -1)

print(factorial(5))
print(factorial(10))
    