# # Exercício - sistema de perguntas e respostas

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '2', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5+5?',
        'Opções': ['25', '55', '10', '15', '51'],
        'Resposta': '10',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

contador = 0

for pergunta in perguntas:
    print(f'Pergunta: {pergunta["Pergunta"]}')
    for i, opcao in enumerate(pergunta['Opções']):
        print(f'{i}) {opcao}')
    escolha = int(input('Escolha uma opção: '))
    print()
    print(pergunta['Opções'][escolha])
    print()
    if pergunta['Opções'][escolha] == pergunta['Resposta']:
        contador += 1
        print('Acertou!')
    else:
        print('Errou!')

print(f'Parabéns, você acertou {contador} de {len(perguntas)} perguntas.')
