matriz = [0]*4
cont = 0
for i in range(len(matriz)):
    matriz[i]= input(f"Digite valores para a matriz[{i}]: ")
    matriz[i] = int(matriz[i])  
for i in range(len(matriz)):
    if matriz[i] >0:
        print(matriz[i])
        
    else:
        cont +=1
        print()
print(f" A quantidade de valores negativos é {cont}")
