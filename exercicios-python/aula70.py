frase = 'O Python é uma linguagem de programação multiparadigma. Python foi criado por Guido Van Rossum'.lower().replace(' ', '')
frase1 = 'tcesctsccecscs'

# Qual a letra apareceu mais vezes na frase? # versao do prof

i = 0
qtd_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''

while i < len(frase):
    letra_atual = frase[i]
    qtd_apareceu_mais_vezes_atual = frase.count(letra_atual)

    if qtd_apareceu_mais_vezes < qtd_apareceu_mais_vezes_atual:
        qtd_apareceu_mais_vezes = qtd_apareceu_mais_vezes_atual
        letra_apareceu_mais_vezes = letra_atual

    i += 1

print(
    'A letra que apareceu mais vezes foi '
    f'"{letra_apareceu_mais_vezes}" que apareceu '
    f'{qtd_apareceu_mais_vezes}x'
)

#minha versao

# letra_aux = ''
# letra_repetida_aux = ''
# cont_aux = 0
# cont = 0
# letra_repetida_correta = ''

# while cont < len(frase):
#     letra = frase[cont] # no primeiro momento letra é igual a 't'

#     while cont_aux < len(frase):
#         #print(letra, frase[cont_aux])
#         if letra == frase[cont_aux]:
#             letra_repetida_aux += letra
#         cont_aux += 1

#     if len(letra_repetida_aux) > len(letra_repetida_correta):
#         letra_repetida_correta = letra_repetida_aux
#     letra_repetida_aux = ''
#     cont_aux = 0
#     cont += 1


# print(letra_repetida_correta)
    
