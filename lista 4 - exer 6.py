import os
os.system('cls||clear')

z = 0
print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
y = int(input('Digite um Quantos Numeros Desejar: ')) 
print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
for x in range(0,y,1):
    y=int(input(f"Digite o Valor {x} : "))
    z=z+y 
print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
print(f'Somar dos valor é {z}')
