# a= 18
# b = 0
# c = a / b
#b = 0
#print(b[0])
# string = 'Luiz'
# print(isinstance(string, str))

# try:
#     a= 18
#     b = 0
#     #print(b[0])
#     #print('Linha 1'[1000])
#     c = a / b
#     print('Linha 2')
# except ZeroDivisionError as e:
#     print(e.__class__.__name__)
#     print(e)
# except NameError:
#     print('Nome b não está definido')
# except (TypeError, IndexError) as error:
#     print('TypeError + IndexError')
#     print('MSG:', error)
#     print('Nome:', error.__class__.__name__)
# except Exception:
#     print('ERRO DESCONHECIDO.')


# print('CONTINUAR')

#######################################
#######################################
#######################################

try: 
    print(1)
    #8/0
except ZeroDivisionError: 
    print('DIVIDIU ZERO')
except IndexError as error:
    print('IndexError')
except (NameError, ImportError):
    print('NameError, ImportError')
else:
    print('Não deu erro')
finally:
    print(2)