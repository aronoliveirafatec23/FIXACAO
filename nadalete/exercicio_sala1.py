import math as m

A = float(input('\ndigite o comprimento do lado A:'))
B = float(input('\nDigite o comprimento do lado B:'))
C = float(input('\nDigite o comprimento do lado C:'))

if A < (B+C) and B < (C+A) and C < (A+B):
    print(f'\nIsso é um triângulo!')

    if (A == B and B == C and C == A):
        print(f'\nIsso é um Triângulo Equilátero!')

    elif (A == B and B != C and C != A):
        print(f'\nIsso é um Triângulo Isósceles!')

    elif (A != B and B != C and C != A):
        print (f'\nIsso é um Triângulo Escaleno')

else:   
    print ('\nNão compõe um triângulo')

print('\n')

    

