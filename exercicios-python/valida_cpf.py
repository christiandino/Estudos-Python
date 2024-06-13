"""

Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros digitos do CPF
multiplicando cada um dos valores por uma contagem
regressiva começando do 10

Ex.: 746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados:
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrario disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7

Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros digitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma contagem
regressiva começando do 11

Ex.: 746.824.890-70 (746824890)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7
   77  40 54 64 14 24 40 36 0 14
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta
"""
# cpf = '36440847007' # Esse CPF gera o primeiro dígito como 10(0)

# cpf = input("Digite o cpf: ")
# cpf = cpf.replace(".","").replace("-","")
import re


cpf = input('Digite o CPF: ')
cpf = re.sub(
    r'[^0-9]',
    '',
    cpf
)

#print(f'O CPF digitado foi: {cpf}')
cpf_nove_digitos = cpf[:9]
soma_cpf = 0
soma_cpf2 = 0
regressiva_1 = 10
regressiva_2 = 11

for i in cpf_nove_digitos:
    soma_cpf += int(i) * regressiva_1
    regressiva_1 -= 1

digito_1 = (soma_cpf * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0

#print('O primeiro dígito do CPF é:', digito_1 if digito_1 < 9 else 0)
digito_1 = str(digito_1)

cpf_dez_digitos = cpf[:9] + digito_1 if int(digito_1) <= 9 else '0'


for i in cpf_dez_digitos:
    soma_cpf2 += int(i) * regressiva_2
    regressiva_2 -= 1


digito_2 = (soma_cpf2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 10 else 0

#print('O segundo dígito do CPF é:', digito_2 if digito_2 <= 10 else 0)

cpf_gerado_pelo_calculo = f'{cpf_nove_digitos}{digito_1}{digito_2}'

if cpf == cpf_gerado_pelo_calculo:
    print(f'{cpf} é válido')
else:
    print('CPF inválido')

# if (cpf[9:12]) == str(digito_1) + str(digito_2):
#     print('CPF válido')
# else:
#     print('CPF inválido')