"""
Operação ternária (condicional de uma linha)
<valor> if <condicao>> else <outro valor>

"""

# print('Valor' if True else 'Outro valor') # Valor
# print('Valor' if False else 'Outro valor') # Outro valor

# condicao = 10 == 10
# condicao2 = 10 == 11
# variavel = 'Valor' if condicao2 else 'Outro valor'
# print(variavel)

#digito = 9
#novo_digito = digito if digito <= 9 else 0
# novo_digito = 0 if digito > 9 else digito
# print(novo_digito)

print('Valor' if True else 'Outro valor' if True else 'Fim') # Valor
print('Valor' if False else 'Outro valor' if True else 'Fim') # Outro valor
print('Valor' if False else 'Outro valor' if False else 'Fim') # Fim