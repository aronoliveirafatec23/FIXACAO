A = 2.90
G = 3.30

álcool = float(input('\nquantidade de álcool:'))
gasolina = float(input('\nquantidade de gasolina'))

if álcool <= 20:
    valora = álcool*(A*0.3)

else:
    valora = álcool*(A*0.5)


if gasolina <= 20:
    valorg = gasolina*(G*0.5)

else:
    valorg = gasolina*(G*0.5)

print(f'\nValor a pagar: R$ {valora:.2f}')
print(f'\nValor a pagar: R$ {valorg:f}')
print('\n')



