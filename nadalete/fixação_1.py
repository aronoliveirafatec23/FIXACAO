import math as m


altura = float(input('Qual sua altura?\nDigite sua altura:'))
sexo = input('Qual seu sexo? m = masculino e f = feminino\nDigite seu sexo:')


if (sexo.lower() == 'm'):
    homem = (72.7*altura)-58
    print(f'\nSeu peso ideal é {homem} kg')

elif (sexo.lower() == 'f'):
    mulher = (62.1*altura)-44.7
    print(f'\nSeu peso ideal é {mulher} kg')

else:
    print(f'\nOpção inválida')
print('\n')






    