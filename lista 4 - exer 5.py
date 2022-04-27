import os
os.system('cls||clear')

p= 0
i= 0

print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
y = int(input('Digite um Quantos Numeros Desejar: ')) 
print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")

for x in range(0,y):

    valor = int(input('Valor : '))

    if valor %2==0:
        p=p+1
    else:
        i=i+1
print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
print(f'O codigo tem:\n {p} Numeros Pares \n {i} Numeros Impares')
print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
