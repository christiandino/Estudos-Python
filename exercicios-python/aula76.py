"""
Jogo da palavra secreta versão do professor
"""
import os

palvra_secreta = 'perfume'
letras_acertadas = ''
numero_tentativas = 0

while True:
    

    letra_digitada = input('Digite uma letra: ')
    numero_tentativas += 1

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra.')
        continue

    if letra_digitada in palvra_secreta:
        letras_acertadas += letra_digitada
    
    palavra_formada = ''

    for letra_secreta in palvra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
    
    print('Palavra formada: ', palavra_formada)

    if palavra_formada == palvra_secreta:
        os.system('cls')
        print("Você ganhou, Parabéns!")
        print('A palavra era ', palvra_secreta)
        print("Tentativas: ", numero_tentativas)
        letras_acertadas = ''
        numero_tentativas = 0



"""
Jogo da palavra secreta minha versão
"""
# palvra_secreta = 'futebol'
# tentativas = 0
# saida = ''
# formando_palavra = ['*','*','*','*','*','*','*']
# formatar = ''

# while saida != palvra_secreta:
#     letra = input('Digite um caractere da palavra secreta: ')
#     if len(letra) > 1 or len(letra) == 0:
#         print("Por favor digite apenas uma letra")
#     elif letra in palvra_secreta:
#         index_letra = palvra_secreta.index(letra)
#         formando_palavra[index_letra] = letra    
#     else:
#         print(f'O caracter "{letra}" digitado não está dentro da palavra secreta, tente novamente')
#     tentativas += 1

#     print(''.join(formando_palavra))


# print(f"Parabéns você completou a palavra secreta em {tentativas} tentativas")

    