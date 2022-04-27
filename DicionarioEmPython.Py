import os
os.system('cls||clear')

banda0 = {
    "nome" : "JesusCrize",
    "numero_integrantes" : 7,
    "ranking" : 1,
    "Musica" : "Rap"
}

banda1 = {
    "nome" : "Mc Joelzinho",
    "numero_integrantes" : 9,
    "ranking" : 4,
    "Musica" : "Sertanejo"
}

banda2 = {
    "nome" : "LoliNightCore",
    "numero_integrantes" : 4,
    "ranking" : 5,
    "Musica" : "K-POP"
}

banda3 = {
    "nome" : "XinXouShou",
    "numero_integrantes" : 3,
    "ranking" : 2,
    "Musica" : "Bage"
}

banda4 = {
    "nome" : "BandaDoPagode",
    "numero_integrantes" :2,
    "ranking" : 3,
    "Musica" : "Funk"
}

Bandas = [banda0,banda1,banda2,banda3,banda4]
#print(len(Bandas))

for x in  range(len(Bandas)):
    #print(Bandas[x].get("ranking"))
    if Bandas[x].get("ranking") == 3:
        NomeRank = Bandas[x].get("nome")
SD= 0
for y in range(len(Bandas)):
    F = Bandas[y].get("numero_integrantes")
    SD = SD + F 
    #print(SD)
    
print('------------------------------------------')
print("\t\tNome Das Bandas\n")
for x in range(len(Bandas)):
    print(f"Banda {x+1} - " + Bandas[x].get("nome"))

print(f"\nBanda em 3º Lugar é {NomeRank}")

print((f"\nSoma De Todos Os Integrantes é : {SD}"))

print('-----------------------------------------')