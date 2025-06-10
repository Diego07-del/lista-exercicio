vetor = [0]*4
cont = 0
for i in range(len(vetor)):
    vetor[i]= int(input(f"Digite valores para a lista[{i}]: "))
    
for i in range(len(vetor)):
    if vetor[i] >0:
        print(vetor[i])
        
    else:
        cont +=1
        print()
print(f" A quantidade de valores negativos é {cont}")
