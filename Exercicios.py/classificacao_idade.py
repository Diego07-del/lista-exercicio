print('-'*15, 'FASES DA VIDA', '-'*15)

idade = int(input('Informe sua idade: '))

if idade <= 12:
    print('Você ainda é uma CRIANÇA')
elif idade > 12 and idade <= 16:
    print('Você já é um(a) ADOLESCENTE.')
elif idade > 16 and idade <= 40:
    print('Você é um ADULTO JOVEM')
elif idade > 40:
    print('Você é um ADULTO')
