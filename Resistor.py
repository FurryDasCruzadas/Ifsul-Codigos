import os
os.system('cls||clear')

print('-----------------------------------')
print('Preto  = 0 \nMarrom = 1\nVermelho = 2\nLaranja = 3\nAmarelo = 4\nVerde = 5\nAzul = 6\nVioleta = 7\nCinza = 8\nBranco = 9')
cor1 = input('Cor Da Faixa 1 : ')
cor2 = input('Cor Da Faixa 2 : ')
cor3 = int(input('Cor Da Faixa 3 : '))

print('-----------------------------------')
print('Dourado = 1\nPrata = 2\nSem Cor = 3')
cor4 = int(input('Cor Da Faixa 4 : '))
print('-----------------------------------')

corf = cor1 + cor2
corf = int(corf)

for x in range(10):
    if cor3 == x:
        resistor = corf * (pow(10, x-1))

if cor4 == 1:
    final = 5
if cor4 == 2:
    final = 10
if cor4 == 3:
    final = 20

resistorFinal = resistor * (final / 100)
resistorMaxi = resistor + resistorFinal
resistorMino = resistor - resistorFinal

print(f'O Valor Do Resistor Sera {resistor}Ω ,com Torelancia De {final}%\nTorelancia Minima = {resistorMino}\nTorelancia Maxima = {resistorMaxi}')
